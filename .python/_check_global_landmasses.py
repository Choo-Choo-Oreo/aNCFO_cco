"""
Compute every discrete landmass on the mod's map, independent of ownership.

Builds the same land-adjacency graph as _check_connectivity.py (provinces.bmp
pixel borders, edited by adjacencies.csv straits / impassables) and takes the
connected components over EVERY land province, with no ownership restriction at
all. Each landmass is a maximal set of land provinces reachable from one another
by land.

Landmasses are numbered largest-to-smallest by province count (matching the
cluster-ordering convention in _check_connectivity.py, tie-broken by lowest
province id). For each landmass the output lists every province id, every state
present on it, and that state's current owner tag -- so the result can be cross
referenced directly against any tag's connectivity_TAG.json without recomputing.

Note: the node set is every land province in definition.csv, so a genuinely
isolated one-province island (no land neighbour) still appears as its own
landmass. A land province defined but absent from the bitmap would likewise
show up as a lone singleton, which is worth noticing as a data issue.

This script lives in the mod's root-level .python/ folder and resolves all input
files from its own location, so it runs from any working directory. Output is
written to the current working directory.

Usage (from anywhere):

    python /path/to/mod/.python/_check_global_landmasses.py [--conn 4|8]

or from the .python/ folder:

    python _check_global_landmasses.py [--conn 4|8]

Requires: Pillow, numpy.
"""

import argparse
import json
import sys
from pathlib import Path

from _map_common import (
    ADJACENCIES_FILE,
    DEFINITION_FILE,
    MOD_ROOT,
    PROVINCES_BMP,
    STATES_DIR,
    UnionFind,
    apply_adjacency_exceptions,
    extract_pixel_adjacency,
    parse_definition,
    parse_states,
    verify_mod_root,
)

OUTPUT_FILE = "landmasses.json"


def main():
    ap = argparse.ArgumentParser(
        description="Compute every discrete landmass on the map, independent of "
        "ownership, and write landmasses.json."
    )
    ap.add_argument(
        "--conn",
        type=int,
        choices=(4, 8),
        default=4,
        help="Pixel connectivity: 4 = orthogonal (default), 8 = include diagonals",
    )
    args = ap.parse_args()

    # Confirm the script can reliably locate the mod root before doing any work.
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
    owner_of = {st["id"]: st["owner"] for st in states}
    print(f"  {len(states)} states, {len(prov2state)} provinces assigned.")

    # Connected components over EVERY land province -- no ownership restriction.
    # Seeding with the full land set means isolated islands (no land neighbour)
    # still form their own landmass.
    uf = UnionFind()
    for pid in land_ids:
        uf.find(pid)
    for pair in land_adj:
        a, b = tuple(pair)
        uf.union(a, b)

    # Group provinces by component root.
    components = {}  # root -> [province ids]
    for pid in land_ids:
        components.setdefault(uf.find(pid), []).append(pid)

    # Largest to smallest by province count, tie-break lowest province id --
    # same ordering convention as _check_connectivity.py.
    ordered = sorted(components.values(), key=lambda c: (-len(c), min(c)))

    landmasses = []
    state_landmasses = {}  # state id -> set of landmass ids it has provinces on
    for lm_id, provinces in enumerate(ordered, start=1):
        provinces_sorted = sorted(provinces)
        # States present on this landmass, with their current owner tag.
        state_ids = sorted(
            {prov2state[p] for p in provinces_sorted if p in prov2state}
        )
        for sid in state_ids:
            state_landmasses.setdefault(sid, set()).add(lm_id)
        states_here = [
            {"state_id": sid, "owner": owner_of.get(sid)} for sid in state_ids
        ]
        landmasses.append(
            {
                "landmass_id": lm_id,
                "province_count": len(provinces_sorted),
                "state_count": len(states_here),
                "provinces": provinces_sorted,
                "states": states_here,
            }
        )

    # States whose provinces are split across more than one landmass. A coastal
    # state with a real offshore island looks identical here to a state that
    # accidentally includes a stray far-away province, so these are surfaced for
    # a manual check rather than treated as errors.
    multi_landmass_states = [
        {
            "state_id": sid,
            "owner": owner_of.get(sid),
            "landmass_ids": sorted(lids),
        }
        for sid, lids in sorted(state_landmasses.items())
        if len(lids) > 1
    ]

    payload = {
        "map": MOD_ROOT.name,
        "generated_by": Path(__file__).name,
        "pixel_connectivity": args.conn,
        "sea_crossings": "all_strait_crossings_bridge",
        "land_province_count": len(land_ids),
        "landmass_count": len(landmasses),
        "multi_landmass_state_count": len(multi_landmass_states),
        "multi_landmass_states": multi_landmass_states,
        "landmasses": landmasses,
    }
    out_path = Path(OUTPUT_FILE)
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    # -------- Console summary --------
    print("\n" + "=" * 60)
    print("Global landmasses (whole map, ownership-independent)")
    print("=" * 60)
    print(f"Land provinces : {len(land_ids)}")
    print(f"Landmasses     : {len(landmasses)}")
    print("Five largest (by province count):")
    for lm in landmasses[:5]:
        print(
            f"  #{lm['landmass_id']:<3} {lm['province_count']:>6} provinces, "
            f"{lm['state_count']:>4} states"
        )

    if multi_landmass_states:
        print(
            f"\nWARNING: {len(multi_landmass_states)} state(s) span more than one "
            "landmass -- worth a manual check."
        )
        print(
            "  A coastal state with a real offshore island is indistinguishable "
            "here from a"
        )
        print(
            "  state that accidentally includes a stray far-away province:"
        )
        for m in multi_landmass_states:
            owner = m["owner"] or "----"
            print(
                f"    - state {m['state_id']:>5} [{owner}] on landmasses "
                f"{m['landmass_ids']}"
            )

    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
