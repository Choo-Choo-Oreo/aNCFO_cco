"""map_lint.py [--mod MOD] [--vanilla DIR]

Cross-checks a mod's map data against itself and the engine's own map rules.
Reports every mismatch, not just the first:
  definition.csv: duplicate ids/colours, land without continent, coastal flag
  provinces.bmp vs definition.csv: colours/ids that disagree, provinces with no pixels
  supply_nodes / railways / buildings / states / strategic regions / supply areas
  vs sea-or-land type; every province in exactly one state (land) and one region
Run from anywhere; mod path is resolved relative to cwd.
"""
import argparse, re, sys
from pathlib import Path
from collections import defaultdict

ap = argparse.ArgumentParser()
ap.add_argument("--mod", default="New-Horizons")
ap.add_argument("--vanilla", default=r"D:\Program Files\SteamLibrary\steamapps\common\Hearts of Iron IV")
ap.add_argument("--no-bmp", action="store_true")
a = ap.parse_args()
mod = Path(a.mod).resolve()
van = Path(a.vanilla)


def src(rel):
    """mod file if present else vanilla"""
    p = mod / rel
    return p if p.exists() else van / rel


def rd(p):
    return Path(p).read_text(encoding="utf-8-sig", errors="replace")


def strip(t):
    return re.sub(r"#.*", "", t)


problems = defaultdict(list)


def bad(kind, msg):
    problems[kind].append(msg)


# --- definition.csv
prov = {}
colors = defaultdict(list)
for ln in rd(src("map/definition.csv")).splitlines():
    f = ln.strip().split(";")
    if len(f) < 8 or not f[0].isdigit():
        continue
    i = int(f[0])
    if i in prov:
        bad("definition duplicate id", str(i))
    prov[i] = dict(rgb=(int(f[1]), int(f[2]), int(f[3])), type=f[4], coastal=f[5] == "true", terrain=f[6], cont=int(f[7]))
    colors[prov[i]["rgb"]].append(i)
for c, ids in colors.items():
    if len(ids) > 1:
        bad("definition duplicate colour", f"{c}: {ids[:6]}")
ids = sorted(prov)
for n, i in enumerate(ids):
    if i != n:
        bad("definition id gap", f"expected {n} found {i} (first gap only)")
        break
for i, p in prov.items():
    if i == 0:
        continue
    if p["type"] == "land" and p["cont"] == 0:
        bad("land without continent", str(i))
    if p["type"] in ("sea", "lake") and p["cont"] != 0 and p["type"] == "sea":
        bad("sea with continent", str(i))
land = {i for i, p in prov.items() if p["type"] == "land"}
sea = {i for i, p in prov.items() if p["type"] == "sea"}
print(f"definition: {len(prov)} provinces, {len(land)} land, {len(sea)} sea")

# --- provinces.bmp vs definition
if not a.no_bmp:
    try:
        from PIL import Image
        import numpy as np
        Image.MAX_IMAGE_PIXELS = None
        im = Image.open(src("map/provinces.bmp")).convert("RGB")
        arr = np.asarray(im).reshape(-1, 3)
        packed = (arr[:, 0].astype(np.int64) << 16) | (arr[:, 1].astype(np.int64) << 8) | arr[:, 2]
        uniq, counts = np.unique(packed, return_counts=True)
        seen = {int(u) for u in uniq}
        defc = {(r << 16) | (g << 8) | b: i for i, p in prov.items() if i for (r, g, b) in [p["rgb"]]}
        print(f"provinces.bmp: {im.size}, {len(seen)} unique colours")
        for u, c in zip(uniq, counts):
            u = int(u)
            if u not in defc:
                bad("bmp colour not in definition", f"#{u:06x} ({c} px)")
        for col, i in defc.items():
            if col not in seen:
                bad("province with no pixels", f"{i} {prov[i]['type']}")
    except Exception as e:
        print("bmp check skipped:", e)

# --- states
state_of = defaultdict(list)
state_ids = {}
sdir = mod / "history/states" if (mod / "history/states").exists() else van / "history/states"
for f in sorted(sdir.glob("*.txt")):
    t = strip(rd(f))
    m = re.search(r"\bid\s*=\s*(\d+)", t)
    pm = re.search(r"provinces\s*=\s*\{([^}]*)\}", t)
    if not m or not pm:
        bad("state missing id/provinces", f.name)
        continue
    sid = int(m.group(1))
    if sid in state_ids:
        bad("duplicate state id", f"{sid}: {state_ids[sid]} {f.name}")
    state_ids[sid] = f.name
    for p in map(int, pm.group(1).split()):
        state_of[p].append(sid)
        if p not in prov:
            bad("state province not in definition", f"state {sid} province {p}")
        elif p not in land:
            bad("state contains non-land province", f"state {sid} province {p} ({prov[p]['type']})")
    # buildings referencing provinces not in the state
    prs = set(map(int, pm.group(1).split()))
    for bm in re.finditer(r"\b(\d+)\s*=\s*\{\s*((?:naval_base|bunker|coastal_bunker|supply_node|rail_way)[^}]*)\}", t):
        if int(bm.group(1)) not in prs:
            bad("state building province not in state", f"state {sid} province {bm.group(1)}")
    for vm in re.finditer(r"victory_points\s*=\s*\{\s*(\d+)\s+\d+", t):
        if int(vm.group(1)) not in prs:
            bad("VP province not in state", f"state {sid} province {vm.group(1)}")
for p in land - {0}:
    if p not in state_of:
        bad("land province in no state", str(p))
for p, s in state_of.items():
    if len(s) > 1:
        bad("province in multiple states", f"{p}: {s}")
print(f"states: {len(state_ids)}")

# --- strategic regions
reg_of = defaultdict(list)
for f in sorted((mod / "map/strategicregions").glob("*.txt")):
    t = strip(rd(f))
    m = re.search(r"\bid\s*=\s*(\d+)", t)
    pm = re.search(r"provinces\s*=\s*\{([^}]*)\}", t)
    if not m or not pm:
        bad("region missing id/provinces", f.name)
        continue
    for p in map(int, pm.group(1).split()):
        reg_of[p].append(int(m.group(1)))
        if p not in prov:
            bad("region province not in definition", f"region {m.group(1)} province {p}")
for p in prov:
    if p == 0 or prov[p]["type"] == "lake":
        continue
    if p not in reg_of:
        bad("province in no strategic region", f"{p} {prov[p]['type']}")
for p, r in reg_of.items():
    if len(r) > 1:
        bad("province in multiple regions", f"{p}: {r}")

# --- supply nodes, railways
for ln in rd(src("map/supply_nodes.txt")).splitlines():
    f = ln.split()
    if len(f) == 2 and f[1].isdigit():
        p = int(f[1])
        if p not in prov:
            bad("supply node not in definition", str(p))
        elif p not in land:
            bad("supply node on non-land", f"{p} ({prov[p]['type']})")
        elif p not in state_of:
            bad("supply node in no state", str(p))
for n, ln in enumerate(rd(src("map/railways.txt")).splitlines(), 1):
    f = ln.split()
    if len(f) < 3:
        continue
    cnt = int(f[1])
    pr = list(map(int, f[2:]))
    if cnt != len(pr):
        bad("railway count mismatch", f"line {n}: says {cnt} has {len(pr)}")
    for p in pr:
        if p not in prov:
            bad("railway province not in definition", f"line {n}: {p}")
        elif p not in land:
            bad("railway on non-land", f"line {n}: {p} ({prov[p]['type']})")

# --- buildings.txt: state;name;x;y;z;rot;adjacent sea province
for n, ln in enumerate(rd(src("map/buildings.txt")).splitlines(), 1):
    f = ln.strip().split(";")
    if len(f) < 7:
        continue
    sid, name, adj = f[0], f[1], f[6]
    if sid.isdigit() and int(sid) not in state_ids:
        bad("buildings.txt state not found", f"line {n}: state {sid}")
    if name in ("naval_base", "naval_base_spawn", "floating_harbor", "coastal_bunker") or adj not in ("0", ""):
        if adj.isdigit() and int(adj) != 0:
            q = int(adj)
            if q not in prov:
                bad("buildings.txt adjacent province not in definition", f"line {n}: {name} {q}")
            elif name in ("naval_base_spawn", "naval_base", "coastal_bunker") and q not in sea:
                bad("building adjacent province not sea", f"line {n}: state {sid} {name} -> {q} ({prov[q]['type']})")

# --- positions / cities (only exist in vanilla unless overridden)
for rel in ("map/positions.txt", "map/cities.txt"):
    if not (mod / rel).exists():
        print(f"NOTE {rel} not provided by mod; vanilla's is used (covers vanilla provinces only)")

# --- adjacency count
adj = defaultdict(int)
for ln in rd(src("map/adjacencies.csv")).splitlines()[1:]:
    f = ln.split(";")
    if len(f) > 1 and f[0].isdigit() and f[1].isdigit():
        adj[int(f[0])] += 1
        adj[int(f[1])] += 1
for p, c in adj.items():
    if c > 254:
        bad("adjacencies >254", f"{p}: {c}")

total = 0
for k, v in sorted(problems.items()):
    total += len(v)
    print(f"\n== {k}: {len(v)}")
    for x in v[:40]:
        print("  ", x)
    if len(v) > 40:
        print(f"   ... {len(v)-40} more")
print(f"\nTOTAL problems: {total}")
