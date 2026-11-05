#!/usr/bin/env python3
"""buildings_tool.py - audit and safely edit map/buildings.txt for any HoI4 mod.

Replacement for the in-game buildings nudger, which regenerates rows badly.
Rules come from the decompiled engine (mapbuildings.cpp, map.cpp, strategicair.cpp):

  * row = state;type;x;y;z;rotation;seazone     (7 fields, ';' separated)
  * the pixel (x, H-1-round(z)) of provinces.bmp must be LAND, and its province must
    belong to the row's state ("location is not within specified state")
  * port rows (naval_base_spawn) need seazone >= 1, a real sea province (not a lake)
  * every coastal land province needs a port row ("coastal but has no port building")
  * every state needs air_base / rocket_site_spawn / stronghold_network rows
    (strategicair.cpp: "no air base site / rocket site / gun emplacement for state N")
  * floating_harbor rows sit on sea pixels; their last field is the land province they serve

Usage (run from a mod root, or pass --mod):
    python tools/buildings_tool.py audit              # report only
    python tools/buildings_tool.py fix                # dry run: show what would change
    python tools/buildings_tool.py fix --apply        # write map/buildings.txt
Options: --mod PATH, --report FILE, --only CATEGORY[,CATEGORY]
Categories: rekey, invalid_port, dup, add_state, add_coast, add_land
Never touches provinces.bmp, definition.csv or state files.  Output file keeps
the file's own conventions (line ending detected, CRLF or LF), latin1, no trailing newline, 2-decimal numbers.
"""
import argparse, collections, glob, math, os, re, sys, zlib
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

# type -> rows per state, applied only to states that have NONE of that type
PER_STATE = {
    "air_base": 1, "rocket_site_spawn": 1, "stronghold_network": 1, "radar_station": 1,
    "synthetic_refinery": 1, "fuel_silo": 1, "nuclear_reactor_spawn": 1,
    "industrial_complex": 6, "steel_complex": 6, "aluminium_complex": 6, "arms_factory": 6,
    "anti_air_building": 3,
}
PER_LAND = ["supply_node", "bunker", "special_project_facility_spawn", "trench_line"]
PER_COAST = ["naval_supply_hub", "naval_headquarters", "coastal_bunker", "naval_base_spawn"]
SEA_TYPES = {"naval_base_spawn"}          # rows whose last field is a sea zone


def load(mod):
    d = {}
    for ln in open(os.path.join(mod, "map/definition.csv"), encoding="latin1"):
        p = ln.strip().split(";")
        if len(p) >= 7 and p[0].isdigit():
            d[int(p[0])] = ((int(p[1]) << 16) | (int(p[2]) << 8) | int(p[3]), p[4], p[5] == "true")
    colors = sorted((c, i) for i, (c, _, _) in d.items())
    cs = np.array([c for c, _ in colors]); ci = np.array([i for _, i in colors], np.int32)
    a = np.asarray(Image.open(os.path.join(mod, "map/provinces.bmp")).convert("RGB"))
    P = (a[..., 0].astype(np.uint32) << 16) | (a[..., 1].astype(np.uint32) << 8) | a[..., 2]
    pos = np.searchsorted(cs, P); pos[pos >= len(cs)] = 0
    PID = ci[pos]
    typ = {i: t for i, (_, t, _) in d.items()}
    coast = {i: c for i, (_, _, c) in d.items()}
    st = {}
    for f in glob.glob(os.path.join(mod, "history/states/*.txt")):
        t = open(f, encoding="latin1").read()
        m = re.search(r"\bid\s*=\s*(\d+)", t)
        pr = re.search(r"provinces\s*=\s*\{([^}]*)\}", t)
        if m and pr:
            for x in pr.group(1).split():
                st[int(x)] = int(m.group(1))
    return PID, typ, coast, st


def pix(PID, f):
    H, W = PID.shape
    x = int(round(float(f[2]))); y = H - 1 - int(round(float(f[4])))
    if not (0 <= x < W and 0 <= y < H):
        return None
    return int(PID[y, x]), x, y


class Tool:
    def __init__(self, mod):
        self.mod = mod
        self.PID, self.typ, self.coast, self.st = load(mod)
        self.H, self.W = self.PID.shape
        self.bf = os.path.join(mod, "map/buildings.txt")
        raw = open(self.bf, "rb").read().decode("latin1")
        self.lines = raw.split("\n")
        crlf = sum(1 for l in self.lines if l.endswith("\r"))
        self.eol = "\r\n" if crlf > len(self.lines) // 2 else "\n"
        self.lines = [l.rstrip("\r") for l in self.lines]   # normalised; eol restored on write
        self.nrows = 0
        self.log = collections.defaultdict(list)
        self.sea = {i for i, t in self.typ.items() if t == "sea"}
        n = int(max(self.typ)) + 2
        self.is_land = np.zeros(n, bool); self.is_sea = np.zeros(n, bool)
        for i, t in self.typ.items():
            self.is_land[i] = t == "land"; self.is_sea[i] = t == "sea"
        self._pixels = None; self._coastpx = None

    # ---- geometry helpers -------------------------------------------------
    def pixels(self):
        if self._pixels is None:
            flat = self.PID.ravel(); order = np.argsort(flat, kind="stable")
            ids, start = np.unique(flat[order], return_index=True)
            self._pixels = (order, dict(zip(ids.tolist(), start.tolist())), dict(zip(ids.tolist(), np.append(start[1:], len(flat)).tolist())))
        return self._pixels

    def land_pixels(self, p):
        order, s, e = self.pixels()
        idx = order[s[p]:e[p]]
        return idx // self.W, idx % self.W

    def coast_pixels(self):
        """province -> list of (y, x, seaid) for land pixels with a 4-neighbour sea pixel."""
        if self._coastpx is None:
            P = self.PID; out = collections.defaultdict(list)
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                Q = np.roll(P, (-dy, -dx), axis=(0, 1))
                m = self.is_land[P] & self.is_sea[Q]
                if dy == 1: m[-1, :] = False
                if dy == -1: m[0, :] = False
                ys, xs = np.nonzero(m)
                for y, x, q, p in zip(ys.tolist(), xs.tolist(), Q[ys, xs].tolist(), P[ys, xs].tolist()):
                    out[p].append((y, x, q))
            self._coastpx = out
        return self._coastpx

    def best_sea(self, p):
        c = collections.Counter(q for _, _, q in self.coast_pixels().get(p, []))
        return c.most_common(1)[0][0] if c else None

    @staticmethod
    def rot(key):
        return (zlib.crc32(key.encode()) % 6283) / 1000.0 - 3.141

    def make_row(self, s, t, y, x, last, ref_y):
        z = self.H - 1 - y
        self.nrows += 1
        return ";".join([str(s), t, "%.2f" % x, "%.2f" % ref_y, "%.2f" % z, "%.2f" % self.rot("%s%s%d%d%d" % (s, t, y, x, self.nrows)), str(last)])

    # ---- parse ------------------------------------------------------------
    def rows(self):
        for i, l in enumerate(self.lines):
            f = l.split(";")
            if len(f) >= 7 and f[0].isdigit():
                yield i, f

    # ---- the passes -------------------------------------------------------
    def run(self, only):
        want = lambda c: not only or c in only
        lines = self.lines; drop = set(); rep = {}
        have_state = collections.defaultdict(collections.Counter)
        have_prov = collections.defaultdict(set)
        fh_prov = collections.Counter()
        seen = set(); state_y = collections.defaultdict(list)
        for i, f in list(self.rows()):
            key = ";".join(f)
            if key in seen:
                if want("dup"): drop.add(i); self.log["dup"].append(key)
                continue
            seen.add(key)
            t = f[1]; s = int(f[0])
            if t == "floating_harbor":
                if f[6].strip().isdigit(): fh_prov[int(f[6])] += 1
                continue
            r = pix(self.PID, f)
            if r is None or not self.is_land[r[0]]:
                self.log["not_over_land"].append(key); continue      # engine ignores these; report only
            p = r[0]
            if self.st.get(p) != s:
                new = self.st.get(p)
                if new is not None and want("rekey"):
                    f2 = list(f); f2[0] = str(new); rep[i] = ";".join(f2); self.log["rekey"].append((key, new)); s = new
            if t in SEA_TYPES:
                z = int(f[6]) if f[6].strip().lstrip("-").isdigit() else 0
                ok = z > 0 and self.typ.get(z) == "sea"
                if not ok and want("invalid_port"):
                    if self.coast.get(p):
                        nz = self.best_sea(p)
                        if nz:
                            f2 = (rep.get(i) or key).split(";"); f2[6] = str(nz); rep[i] = ";".join(f2)
                            self.log["invalid_port"].append((key, "sea zone -> %d" % nz)); ok = True
                    if not ok:
                        drop.add(i); self.log["invalid_port"].append((key, "removed: province %d not coastal" % p))
                        continue
            have_state[s][t] += 1; have_prov[p].add(t); state_y[s].append(float(f[3]))
        # add missing rows
        add = collections.defaultdict(list)
        def ymed(s): v = state_y.get(s); return sorted(v)[len(v) // 2] if v else 9.5
        used = set()
        def spread(p, k):
            ys, xs = self.land_pixels(p)
            cy, cx = ys.mean(), xs.mean()
            o = np.argsort((ys - cy) ** 2 + (xs - cx) ** 2)
            j = min(k * 7, len(o) - 1)
            return int(ys[o[j]]), int(xs[o[j]])
        all_states = sorted(set(self.st.values()))
        by_state = collections.defaultdict(list)
        for p, s in self.st.items():
            if self.is_land[p]: by_state[s].append(p)
        if want("add_state"):
            for s in all_states:
                provs = sorted(by_state.get(s, []), key=lambda p: -len(self.land_pixels(p)[0]))
                if not provs: continue
                for t, n in PER_STATE.items():
                    if have_state[s][t]: continue
                    for k in range(n):
                        p = provs[k % len(provs)]
                        y, x = spread(p, 1 + k // len(provs))
                        add[s].append(self.make_row(s, t, y, x, 0, ymed(s)))
                        self.log["add_state"].append((s, t))
        if want("add_coast"):
            for p, lst in sorted(self.coast_pixels().items()):
                s = self.st.get(p)
                if s is None or not self.coast.get(p): continue
                sz = self.best_sea(p)
                if sz is None: continue
                cp = sorted(lst, key=lambda a: (a[0], a[1]))
                for k, t in enumerate(PER_COAST):
                    if t in have_prov[p]: continue
                    y, x, _ = cp[(k * max(1, len(cp) // 5)) % len(cp)]
                    add[s].append(self.make_row(s, t, y, x, sz if t in SEA_TYPES else 0, ymed(s)))
                    self.log["add_coast"].append((s, p, t))
                if not fh_prov[p] and "naval_base_spawn" not in have_prov[p]:
                    y, x, q = cp[0]
                    sy = y + (1 if self.PID[min(y + 1, self.H - 1), x] == q else 0)
                    add[s].append(self.make_row(s, "floating_harbor", sy, x, p, 14.8))
                    self.log["add_coast"].append((s, p, "floating_harbor"))
        if want("add_land"):
            for p in sorted(self.st):
                if not self.is_land[p]: continue
                s = self.st[p]
                for k, t in enumerate(PER_LAND):
                    if t in have_prov[p]: continue
                    y, x = spread(p, k)
                    add[s].append(self.make_row(s, t, y, x, 0, ymed(s)))
                    self.log["add_land"].append((s, p, t))
        # coastal provinces with no port row at all after passes (report)
        self.out_lines = self.apply(rep, drop, add)
        return self.log

    def apply(self, rep, drop, add):
        lines = self.lines; last = {}
        for i, f in self.rows():
            last[int(rep.get(i, ";".join(f)).split(";")[0])] = i
        out = []
        ins = collections.defaultdict(list)
        tail = []
        for s, rows in add.items():
            if s in last: ins[last[s]].extend(rows)
            else: tail.extend(rows)
        for i, l in enumerate(lines):
            if i in drop: continue
            out.append(rep.get(i, l))
            if i in ins: out.extend(ins[i])
        out.extend(tail)
        return out

    def write(self):
        open(self.bf, "wb").write(self.eol.join(self.out_lines).encode("latin1"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["audit", "fix"])
    ap.add_argument("--mod", default=".")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only", default="")
    ap.add_argument("--report", default="")
    a = ap.parse_args()
    only = {x for x in a.only.split(",") if x}
    t = Tool(os.path.abspath(a.mod))
    log = t.run(only)
    lines = []
    for k in ("not_over_land", "rekey", "invalid_port", "dup", "add_state", "add_coast", "add_land"):
        v = log.get(k, [])
        lines.append("%-14s %d" % (k, len(v)))
        for e in v[:40]: lines.append("    %s" % (e,))
        if len(v) > 40: lines.append("    ... %d more" % (len(v) - 40))
    rep = "\n".join(lines)
    print(rep)
    if a.report: open(a.report, "w", encoding="utf-8").write(rep)
    if a.cmd == "fix" and a.apply:
        t.write(); print("written:", t.bf)
    elif a.cmd == "fix":
        print("dry run: nothing written (use --apply)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
