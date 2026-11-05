"""map_limits.py [--mod MOD] [--rev REV] [--vanilla DIR] [--no-vanilla]

Counts the quantities behind HoI4's documented map limits and compares them with
the limit and with the base game's own map:
  bitmap: 24-bit, width and height multiples of 256, area <= 13,238,272 px
  provinces: id gaps, duplicate colours, colours missing from definition.csv
  borders: number of separate province border segments, every edge between two
           different provinces, with nothing excluded (wiki: more than 65,536
           stops being displayed; each disjointed stretch between the same two
           provinces counts on its own).
  province pixels: smallest provinces (MINIMUM_PROVINCE_SIZE_IN_PIXELS), boxes
           wider/taller than 1/8 of the map, 2x2 X-crossings of four provinces
--rev reads the mod's map files from git instead of the working tree.
"""
import argparse, io, re, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
AREA_LIMIT = 13_238_272
BORDER_LIMIT = 65_536

ap = argparse.ArgumentParser()
ap.add_argument("--mod", default="New-Horizons")
ap.add_argument("--rev")
ap.add_argument("--vanilla", default=r"D:\Program Files\SteamLibrary\steamapps\common\Hearts of Iron IV")
ap.add_argument("--no-vanilla", action="store_true")
a = ap.parse_args()


def reader(root, rev=None):
    root = Path(root).resolve()
    if rev:
        top = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True).stdout.strip()
        prefix = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-prefix"],
                                capture_output=True, text=True, check=True).stdout.strip()
        return lambda rel: subprocess.run(["git", "-C", top, "show", f"{rev}:{prefix}{rel}"],
                                          capture_output=True, check=True).stdout
    return lambda rel: (root / rel).read_bytes()


def borders(P, kind):
    """kind[id]: 0 land, 1 sea, 2 lake. Returns (all segments, drawn segments, pairs)."""
    H, W = P.shape
    ys, xs = np.nonzero(P != np.roll(P, -1, axis=1))
    va, vb = P[ys, xs], np.roll(P, -1, axis=1)[ys, xs]
    v1, v2 = ys * (W + 1) + (xs + 1), (ys + 1) * (W + 1) + (xs + 1)
    ys2, xs2 = np.nonzero(P[:-1] != P[1:])
    ha, hb = P[:-1][ys2, xs2], P[1:][ys2, xs2]
    h1, h2 = (ys2 + 1) * (W + 1) + xs2, (ys2 + 1) * (W + 1) + xs2 + 1
    A = np.concatenate([va, ha]); B = np.concatenate([vb, hb])
    V1 = np.concatenate([v1, h1]); V2 = np.concatenate([v2, h2])
    lo, hi = np.minimum(A, B), np.maximum(A, B)
    l, h, x1, x2 = lo.tolist(), hi.tolist(), V1.tolist(), V2.tolist()
    parent = list(range(len(l)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    first = {}
    for i in range(len(l)):
        pair = l[i] * 100003 + h[i]
        for v in (x1[i], x2[i]):
            j = first.setdefault((v, pair), i)
            if j != i:
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
    segments = sum(1 for i in range(len(l)) if find(i) == i)
    return segments, len(set(zip(l, h)))


def analyse(label, read):
    img = Image.open(io.BytesIO(read("map/provinces.bmp")))
    mode = img.mode
    C = np.array(img.convert("RGB")).astype(np.uint32)
    H, W = C.shape[:2]
    C = (C[..., 0] << 16) | (C[..., 1] << 8) | C[..., 2]
    rows, seen_col, dup_col, ids = [], {}, 0, []
    for ln in read("map/definition.csv").decode("utf-8-sig", "replace").splitlines():
        p = ln.split(";")
        if len(p) > 4 and p[0].isdigit():
            pid = int(p[0]); ids.append(pid)
            c = (int(p[1]) << 16) | (int(p[2]) << 8) | int(p[3])
            if pid == 0:
                continue
            if c in seen_col:
                dup_col += 1
            seen_col[c] = pid
            rows.append((pid, p[4]))
    n = max(ids)
    gaps = sorted(set(range(n + 1)) - set(ids))
    cols = np.array(sorted(seen_col), dtype=np.uint32)
    pid_of = np.array([seen_col[k] for k in sorted(seen_col)], dtype=np.int64)
    idx = np.searchsorted(cols, C).clip(0, len(cols) - 1)
    known = cols[idx] == C
    P = np.where(known, pid_of[idx], 0)
    kind = np.zeros(n + 1, dtype=np.int8)
    for pid, t in rows:
        kind[pid] = {"land": 0, "sea": 1, "lake": 2}.get(t, 0)
    cnt = np.bincount(P.ravel(), minlength=n + 1)
    empty = [pid for pid, _ in rows if cnt[pid] == 0]
    small = sorted((int(cnt[pid]), pid) for pid, _ in rows if 0 < cnt[pid] < 8)
    yy, xx = np.indices(P.shape)
    big = []
    order = np.argsort(P.ravel(), kind="stable")
    sp = P.ravel()[order]; sy = yy.ravel()[order]; sx = xx.ravel()[order]
    edge = np.searchsorted(sp, np.arange(n + 2))
    for pid, _ in rows:
        s, e = edge[pid], edge[pid + 1]
        if e > s and (sx[s:e].max() - sx[s:e].min() + 1 > W / 8 or sy[s:e].max() - sy[s:e].min() + 1 > H / 8):
            big.append(pid)
    q = np.stack([C[:-1, :-1], C[:-1, 1:], C[1:, :-1], C[1:, 1:]], axis=-1)
    q.sort(axis=-1)
    xcross = int(((q[..., 0] != q[..., 1]) & (q[..., 1] != q[..., 2]) & (q[..., 2] != q[..., 3])).sum())
    seg_all, pairs = borders(P, kind)
    return dict(label=label, mode=mode, W=W, H=H, area=W * H, provinces=len(rows), maxid=n, gaps=gaps,
                dup_col=dup_col, undefined_px=int((~known).sum()), empty=empty, small=small, big=big,
                xcross=xcross, seg_all=seg_all, pairs=pairs)


def report(r):
    ok = lambda b: "ok  " if b else "FAIL"
    print(f"== {r['label']}")
    print(f"  {ok(r['mode'] == 'RGB' or r['mode'] == 'P')} bitmap {r['W']}x{r['H']} mode {r['mode']}; multiples of 256: {r['W'] % 256 == 0 and r['H'] % 256 == 0}")
    print(f"  {ok(r['area'] <= AREA_LIMIT)} area {r['area']:,} px of {AREA_LIMIT:,} ({100 * r['area'] / AREA_LIMIT:.1f}%)")
    print(f"  provinces {r['provinces']:,} (max id {r['maxid']:,}); id gaps {len(r['gaps'])}; duplicate colours {r['dup_col']}; "
          f"pixels with no definition {r['undefined_px']}; provinces with no pixels {len(r['empty'])}")
    print(f"  {ok(r['seg_all'] <= BORDER_LIMIT)} border segments, every edge: {r['seg_all']:,} of {BORDER_LIMIT:,} ({100 * r['seg_all'] / BORDER_LIMIT:.1f}%)")
    print(f"  distinct province pairs {r['pairs']:,}")
    print(f"  provinces under 8 px: {len(r['small'])} {r['small'][:6]}; boxes over 1/8 map: {len(r['big'])} {r['big'][:6]}; X-crossings: {r['xcross']}")


results = [analyse(f"{a.mod}" + (f" @ {a.rev}" if a.rev else ""), reader(a.mod, a.rev))]
if not a.no_vanilla:
    results.append(analyse("vanilla", reader(a.vanilla)))
for r in results:
    report(r)
if len(results) == 2:
    m, v = results
    print(f"== versus vanilla: {m['provinces'] / v['provinces']:.2f}x provinces, {m['seg_all'] / v['seg_all']:.2f}x border segments, {m['area'] / v['area']:.2f}x area")
sys.exit(0 if all(r["seg_all"] <= BORDER_LIMIT and r["area"] <= AREA_LIMIT for r in results) else 1)
