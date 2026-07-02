"""
Determine province / state connectivity for a country tag.

Groups a country's owned and core states into clusters that are reachable by
land while staying on THIS country's own territory. States outside the largest
cluster are flagged as candidates to verify (possible colony / exclave), NOT as
confirmed detached territory.

Land adjacency is derived from map/provinces.bmp pixel borders (adjacencies.csv
holds only exceptions, never standard land borders). Ownership is used only to
restrict which provinces are eligible path nodes; it is never used as an
adjacency signal.

This script lives in the mod's root-level .python/ folder. All input files are
resolved relative to the script's own location (mod root = the parent of the
.python/ folder), so it can be invoked from any working directory. Output CSV /
JSON files are written to the current working directory.

Usage (from anywhere):

    python /path/to/mod/.python/_check_connectivity.py TAG [--json] [--conn 4|8]

or from the .python/ folder:

    python _check_connectivity.py TAG [--json] [--conn 4|8]

Requires: Pillow, numpy.
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

# -------------------------------------------------------------
# CONFIGURATION SECTION
# -------------------------------------------------------------

# The script lives in <mod_root>/.python/ so the mod root is one level up.
# Everything is resolved from the script's own location, never from the current
# working directory.
SCRIPT_DIR = Path(__file__).resolve().parent
MOD_ROOT = SCRIPT_DIR.parent

DEFINITION_FILE = MOD_ROOT / "map" / "definition.csv"
PROVINCES_BMP = MOD_ROOT / "map" / "provinces.bmp"
ADJACENCIES_FILE = MOD_ROOT / "map" / "adjacencies.csv"
STATES_DIR = MOD_ROOT / "history" / "states"
COUNTRY_TAGS_DIR = MOD_ROOT / "common" / "country_tags"


def verify_mod_root(root: Path):
    """Confirm the resolved mod root actually looks like the mod, so a moved or
    renamed script fails loudly instead of silently finding nothing. Returns a
    list of human-readable problems (empty when everything checks out)."""
    problems = []
    if not (root / "descriptor.mod").is_file():
        problems.append(f"descriptor.mod not found at mod root ({root})")
    if not (root / "map").is_dir():
        problems.append(f"map/ folder not found at mod root ({root})")
    if not (root / "history" / "states").is_dir():
        problems.append(f"history/states/ folder not found at mod root ({root})")
    return problems

# -------------------------------------------------------------
# PARSING: definition.csv
# -------------------------------------------------------------


def parse_definition(path: Path):
    """Return (code2id, land_ids).

    code = R<<16 | G<<8 | B  ->  province id
    land_ids = set of province ids whose type is 'land'
    """
    code2id = {}
    land_ids = set()

    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            # Same row-shape guard as map/_switch_land_sea.py: data rows start
            # with a numeric province id.
            if not row or not row[0].isdigit():
                continue
            pid = int(row[0])
            r, g, b = int(row[1]), int(row[2]), int(row[3])
            ptype = row[4].strip().lower()
            code = (r << 16) | (g << 8) | b
            code2id[code] = pid
            if ptype == "land":
                land_ids.add(pid)

    return code2id, land_ids


# -------------------------------------------------------------
# PIXEL ADJACENCY: provinces.bmp
# -------------------------------------------------------------


def _pairs_from_shift(a, b):
    """Given two aligned code arrays, return the (min,max) id-agnostic code
    pairs where they differ, as an (N,2) int64 array."""
    a = a.ravel()
    b = b.ravel()
    mask = a != b
    a = a[mask]
    b = b[mask]
    lo = np.minimum(a, b)
    hi = np.maximum(a, b)
    return np.stack([lo, hi], axis=1)


def extract_pixel_adjacency(bmp_path: Path, code2id: dict, land_ids: set, conn: int):
    """Return a set of frozensets {id_a, id_b} of land provinces whose pixels
    touch on the bitmap. Horizontal edges wrap (map loops E-W)."""
    img = Image.open(bmp_path).convert("RGB")
    arr = np.asarray(img, dtype=np.uint32)  # H x W x 3
    code = (arr[:, :, 0] << 16) | (arr[:, :, 1] << 8) | arr[:, :, 2]

    chunks = []
    # Horizontal neighbours.
    chunks.append(_pairs_from_shift(code[:, :-1], code[:, 1:]))
    # Horizontal wrap: last column against first column.
    chunks.append(_pairs_from_shift(code[:, -1], code[:, 0]))
    # Vertical neighbours.
    chunks.append(_pairs_from_shift(code[:-1, :], code[1:, :]))

    if conn == 8:
        # Down-right and down-left diagonals.
        chunks.append(_pairs_from_shift(code[:-1, :-1], code[1:, 1:]))
        chunks.append(_pairs_from_shift(code[:-1, 1:], code[1:, :-1]))
        # Diagonal wrap columns.
        chunks.append(_pairs_from_shift(code[:-1, -1], code[1:, 0]))
        chunks.append(_pairs_from_shift(code[:-1, 0], code[1:, -1]))

    all_pairs = np.concatenate(chunks, axis=0)
    # Deduplicate code pairs before translating (far fewer unique border pairs).
    unique_pairs = np.unique(all_pairs, axis=0)

    land_adj = set()
    missing_codes = set()
    for lo, hi in unique_pairs:
        ida = code2id.get(int(lo))
        idb = code2id.get(int(hi))
        if ida is None:
            missing_codes.add(int(lo))
            continue
        if idb is None:
            missing_codes.add(int(hi))
            continue
        if ida in land_ids and idb in land_ids and ida != idb:
            land_adj.add(frozenset((ida, idb)))

    if missing_codes:
        print(
            f"WARNING: {len(missing_codes)} bitmap colour(s) had no "
            f"definition.csv entry; those borders were skipped."
        )

    return land_adj


# -------------------------------------------------------------
# EXCEPTIONS: adjacencies.csv
# -------------------------------------------------------------


def apply_adjacency_exceptions(land_adj: set, path: Path, land_ids: set):
    """Mutate land_adj in place per adjacencies.csv. Returns (added, removed)."""
    added = 0
    removed = 0

    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        header_seen = False
        for row in reader:
            if not row:
                continue
            if not header_seen:
                header_seen = True
                # First line is the column header (From;To;Type;...).
                if not row[0].strip().lstrip("-").isdigit():
                    continue
            # Terminator line and malformed rows.
            if not row[0].strip().lstrip("-").isdigit():
                continue
            frm = int(row[0])
            to = int(row[1])
            if frm < 0 or to < 0:
                continue  # -1;-1;... terminator
            atype = (row[2].strip().lower() if len(row) > 2 else "")

            # Only land-land pairs affect landmass connectivity.
            if frm not in land_ids or to not in land_ids:
                continue

            pair = frozenset((frm, to))
            if atype == "impassable":
                if pair in land_adj:
                    land_adj.discard(pair)
                    removed += 1
            else:
                # sea straits, tunnels, canal passages, or blank (defaults sea)
                if pair not in land_adj:
                    land_adj.add(pair)
                    added += 1

    return added, removed


# -------------------------------------------------------------
# STATES: history/states/*.txt
# -------------------------------------------------------------

_ID_RE = re.compile(r"\bid\s*=\s*(\d+)")
_OWNER_RE = re.compile(r"\bowner\s*=\s*([A-Z0-9]{3})")
_CORE_RE = re.compile(r"\badd_core_of\s*=\s*([A-Z0-9]{3})")
# Top-level state-block flag from history/states (State_modding wiki). This is a
# state-level wasteland/buffer flag and is UNRELATED to the adjacencies.csv
# 'impassable' adjacency type handled in apply_adjacency_exceptions().
_STATE_IMPASSABLE_RE = re.compile(r"\bimpassable\s*=\s*yes\b")


def _extract_provinces_block(text: str):
    """Return the list of province ids inside provinces={ ... }."""
    m = re.search(r"provinces\s*=\s*\{", text)
    if not m:
        return []
    start = m.end()
    depth = 1
    i = start
    while i < len(text) and depth > 0:
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        i += 1
    body = text[start : i - 1]
    return [int(tok) for tok in body.split() if tok.isdigit()]


def parse_states(states_dir: Path):
    """Return list of dicts:
    {id, name, provinces(set), owner, cores(set), impassable(bool)}."""
    states = []
    for path in sorted(states_dir.glob("*.txt")):
        text = path.read_text(encoding="utf-8-sig", errors="replace")

        id_m = _ID_RE.search(text)
        if not id_m:
            continue
        sid = int(id_m.group(1))

        name_m = re.search(r'name\s*=\s*"([^"]*)"', text)
        name = name_m.group(1) if name_m else f"STATE_{sid}"

        provinces = set(_extract_provinces_block(text))

        owner_m = _OWNER_RE.search(text)
        owner = owner_m.group(1) if owner_m else None
        cores = set(_CORE_RE.findall(text))

        # Optional top-level state flag; absent means passable.
        impassable = _STATE_IMPASSABLE_RE.search(text) is not None

        states.append(
            {
                "id": sid,
                "name": name,
                "provinces": provinces,
                "owner": owner,
                "cores": cores,
                "impassable": impassable,
                "file": path.name,
            }
        )
    return states


# -------------------------------------------------------------
# CONNECTED COMPONENTS (union-find)
# -------------------------------------------------------------


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        # Path compression.
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb


# -------------------------------------------------------------
# COUNTRY TAG VALIDATION (optional, non-fatal)
# -------------------------------------------------------------


def tag_is_known(tag: str, tags_dir: Path):
    """Best-effort check that the tag appears in common/country_tags. Returns
    True/False, or None if the directory can't be read."""
    if not tags_dir.is_dir():
        return None
    pattern = re.compile(rf"^\s*{re.escape(tag)}\s*=", re.MULTILINE)
    for path in tags_dir.glob("*.txt"):
        try:
            if pattern.search(path.read_text(encoding="utf-8-sig", errors="replace")):
                return True
        except OSError:
            continue
    return False


# -------------------------------------------------------------
# MAIN
# -------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(
        description="Group a country's owned/core states into land-connected "
        "clusters and flag possible detached territory to verify."
    )
    ap.add_argument("tag", help="Country tag, e.g. MJU")
    ap.add_argument("--json", action="store_true", help="Also write a JSON file")
    ap.add_argument(
        "--conn",
        type=int,
        choices=(4, 8),
        default=4,
        help="Pixel connectivity: 4 = orthogonal (default), 8 = include diagonals",
    )
    args = ap.parse_args()
    tag = args.tag.strip().upper()

    # Confirm the script can reliably locate the mod root from its own location
    # before doing any work.
    root_problems = verify_mod_root(MOD_ROOT)
    if root_problems:
        print("ERROR: could not confirm the mod root from the script location.")
        print(f"  Script:   {Path(__file__).resolve()}")
        print(f"  Expected mod root: {MOD_ROOT}")
        for prob in root_problems:
            print(f"  - {prob}")
        print(
            "  This script must stay inside <mod_root>/.python/. Move it back or "
            "adjust MOD_ROOT."
        )
        sys.exit(1)

    for p in (DEFINITION_FILE, PROVINCES_BMP, ADJACENCIES_FILE):
        if not p.exists():
            print(f"ERROR: cannot find {p}")
            sys.exit(1)

    # Optional tag validation.
    known = tag_is_known(tag, COUNTRY_TAGS_DIR)
    if known is False:
        print(f"WARNING: {tag} was not found in common/country_tags (continuing).")

    print(f"Parsing {DEFINITION_FILE.name} ...")
    code2id, land_ids = parse_definition(DEFINITION_FILE)
    print(f"  {len(code2id)} provinces defined, {len(land_ids)} land provinces.")

    print(f"Extracting pixel adjacency from {PROVINCES_BMP.name} (conn={args.conn}) ...")
    land_adj = extract_pixel_adjacency(PROVINCES_BMP, code2id, land_ids, args.conn)
    print(f"  {len(land_adj)} land-land pixel borders.")

    added, removed = apply_adjacency_exceptions(land_adj, ADJACENCIES_FILE, land_ids)
    print(
        f"Applied {ADJACENCIES_FILE.name}: +{added} crossing(s), -{removed} impassable; "
        f"{len(land_adj)} edges total."
    )

    print(f"Parsing states in {STATES_DIR} ...")
    states = parse_states(STATES_DIR)
    prov2state = {}
    for st in states:
        for pid in st["provinces"]:
            prov2state[pid] = st["id"]
    print(f"  {len(states)} states, {len(prov2state)} provinces assigned.")

    # Select this country's states (owned union core), labeled.
    selected = {}  # state id -> relation
    by_id = {st["id"]: st for st in states}
    for st in states:
        is_owned = st["owner"] == tag
        is_core = tag in st["cores"]
        if not (is_owned or is_core):
            continue
        if is_owned and is_core:
            rel = "both"
        elif is_owned:
            rel = "owned"
        else:
            rel = "core"
        selected[st["id"]] = rel

    if not selected:
        print(f"\n{tag} owns or cores no states. Nothing to analyze.")
        sys.exit(0)

    selected_ids = set(selected)

    # Build state graph over own territory only: an edge exists only when both
    # provinces of a land-adjacency belong to this country's selected states.
    uf = UnionFind()
    for sid in selected_ids:
        uf.find(sid)  # ensure isolated states are their own component
    for pair in land_adj:
        a, b = tuple(pair)
        sa = prov2state.get(a)
        sb = prov2state.get(b)
        if sa is None or sb is None:
            continue
        if sa in selected_ids and sb in selected_ids and sa != sb:
            uf.union(sa, sb)

    # Group states by component root.
    clusters = {}  # root -> [state ids]
    for sid in selected_ids:
        clusters.setdefault(uf.find(sid), []).append(sid)

    # Cluster size = total province count of member states; assign stable ids.
    def cluster_provs(members):
        return sum(len(by_id[s]["provinces"]) for s in members)

    ordered = sorted(
        clusters.values(),
        key=lambda m: (-cluster_provs(m), min(m)),
    )
    cluster_id_of = {}
    for cid, members in enumerate(ordered, start=1):
        for s in members:
            cluster_id_of[s] = cid

    largest_members = ordered[0]
    largest_size = cluster_provs(largest_members)
    largest_ids = set(largest_members)
    tie = len(ordered) > 1 and cluster_provs(ordered[1]) == largest_size

    # Build rows.
    rows = []
    for sid in sorted(selected_ids):
        st = by_id[sid]
        in_largest = sid in largest_ids
        rows.append(
            {
                "state_id": sid,
                "state_name": st["name"],
                "relation": selected[sid],
                "cluster_id": cluster_id_of[sid],
                "state_province_count": len(st["provinces"]),
                "in_largest_cluster": in_largest,
                "flag_verify": not in_largest,
                "state_impassable": st["impassable"],
            }
        )
    rows.sort(key=lambda r: (r["cluster_id"], r["state_id"]))

    # -------- Output files --------
    csv_path = Path(f"connectivity_{tag}.csv")
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "state_id",
                "state_name",
                "relation",
                "cluster_id",
                "state_province_count",
                "in_largest_cluster",
                "flag_verify",
                "state_impassable",
            ],
        )
        w.writeheader()
        w.writerows(rows)

    if args.json:
        json_path = Path(f"connectivity_{tag}.json")
        payload = {
            "tag": tag,
            "connectivity": "own_territory_only",
            "state_set": "owned_union_core",
            "sea_crossings": "all_strait_crossings_bridge",
            "pixel_connectivity": args.conn,
            "cluster_count": len(ordered),
            "largest_cluster_id": 1,
            "largest_cluster_province_count": largest_size,
            "states": rows,
        }
        json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    # -------- Console summary --------
    print("\n" + "=" * 60)
    print(f"Connectivity report for {tag}  (own-territory-only)")
    print("=" * 60)
    print(f"States analyzed : {len(rows)} (owned + core)")
    print(f"Clusters found  : {len(ordered)}")
    print(
        f"Largest cluster : #1 ({len(largest_members)} states, "
        f"{largest_size} provinces) -- treated as the mainland"
    )
    if tie:
        print(
            "  NOTE: another cluster has the same province count; #1 was chosen "
            "as the lowest-id tie-break. The mainland is ambiguous -- verify."
        )

    flagged = [r for r in rows if r["flag_verify"]]
    if len(ordered) == 1:
        print("\nAll states form ONE contiguous cluster. No detached territory.")
    else:
        print(
            f"\nVerify these {len(flagged)} state(s) -- NOT in the largest cluster, "
            "so possibly a colony/exclave. This is a candidate to check, not a "
            "confirmed detached territory:"
        )
        # Group flagged states by cluster for readability.
        for cid in sorted({r["cluster_id"] for r in flagged}):
            members = [r for r in rows if r["cluster_id"] == cid]
            csize = cluster_provs([m["state_id"] for m in members])
            print(f"\n  Cluster #{cid} ({len(members)} state(s), {csize} provinces):")
            for r in members:
                impassable_tag = " [impassable]" if r["state_impassable"] else ""
                print(
                    f"    - state {r['state_id']:>5}  {r['state_name']:<28} "
                    f"[{r['relation']}]{impassable_tag}"
                )

    print(f"\nWrote {csv_path}" + (f" and connectivity_{tag}.json" if args.json else ""))


if __name__ == "__main__":
    main()
