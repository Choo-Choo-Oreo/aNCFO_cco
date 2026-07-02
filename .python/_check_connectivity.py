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

Each state also gets a distance_from_capital_px / _pct_map_width, the straight
line pixel distance from the state's pixel centroid to the capital state's
centroid (capital read from history/countries/<TAG>). This is STRAIGHT LINE
distance only -- it does not account for terrain, sea routes, or actual travel
difficulty, so it measures physical proximity, not reachability.

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
import sys
from pathlib import Path

from _map_common import (
    ADJACENCIES_FILE,
    COUNTRY_TAGS_DIR,
    DEFINITION_FILE,
    MOD_ROOT,
    PROVINCES_BMP,
    STATES_DIR,
    UnionFind,
    apply_adjacency_exceptions,
    compute_province_centroids,
    extract_pixel_adjacency,
    parse_definition,
    parse_states,
    read_capital,
    tag_is_known,
    verify_mod_root,
)


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

    # --- Straight-line distance from the capital (physical proximity only) ---
    print(f"Computing province centroids from {PROVINCES_BMP.name} ...")
    centroids, map_width = compute_province_centroids(PROVINCES_BMP, code2id)

    def state_centroid(sid):
        """Pixel-count weighted mean of a state's province centroids, or None if
        none of its provinces have pixels."""
        st = by_id.get(sid)
        if st is None:
            return None
        sx = sy = 0.0
        total = 0
        for pid in st["provinces"]:
            c = centroids.get(pid)
            if c is not None:
                cx, cy, n = c
                sx += cx * n
                sy += cy * n
                total += n
        return (sx / total, sy / total) if total else None

    def wrapped_distance(a, b):
        """Straight-line pixel distance, taking the shorter of the direct span
        and the span going the other way around the horizontally-wrapping map."""
        if a is None or b is None:
            return None
        dx = abs(a[0] - b[0])
        dx = min(dx, map_width - dx)  # same E-W wrap as extract_pixel_adjacency
        dy = abs(a[1] - b[1])
        return (dx * dx + dy * dy) ** 0.5

    capital_state_id = read_capital(tag)
    capital_centroid = (
        state_centroid(capital_state_id) if capital_state_id is not None else None
    )
    if capital_state_id is None:
        print(
            f"WARNING: no capital found for {tag} in history/countries; "
            "distances will be null."
        )
    elif capital_centroid is None:
        print(
            f"WARNING: capital state {capital_state_id} has no pixels on the "
            "bitmap; distances will be null."
        )

    selected_ids = set(selected)
    # Strict owned-only connectivity: a bridging edge only ever forms when BOTH
    # endpoint provinces belong to states this tag owns ("owned" or "both").
    # Core-only states ("core") are never merged into any cluster, regardless of
    # adjacency -- each always reports as its own isolated singleton.
    owned_ids = {sid for sid, rel in selected.items() if rel in ("owned", "both")}

    # Build the state graph. Every selected state is a node so isolated states
    # (all core-only states, plus any owned exclave) form their own component.
    uf = UnionFind()
    for sid in selected_ids:
        uf.find(sid)

    # Connect owned states to each other through owned-only pixel / adjacencies.csv
    # connectivity. This is the only place clusters get merged, so a claimed-but-
    # not-owned state can never act as a stepping stone or attach to a cluster.
    for pair in land_adj:
        a, b = tuple(pair)
        sa = prov2state.get(a)
        sb = prov2state.get(b)
        if sa is None or sb is None or sa == sb:
            continue
        if sa in owned_ids and sb in owned_ids:
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
        dist_px = wrapped_distance(state_centroid(sid), capital_centroid)
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
                "distance_from_capital_px": (
                    round(dist_px, 1) if dist_px is not None else None
                ),
                "distance_from_capital_pct_map_width": (
                    round(dist_px / map_width * 100, 2) if dist_px is not None else None
                ),
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
                "distance_from_capital_px",
                "distance_from_capital_pct_map_width",
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
            "capital_state_id": capital_state_id,
            "map_width_px": map_width,
            "distance_note": "straight-line pixel distance only; ignores terrain, "
            "sea routes, and travel difficulty (proximity, not reachability)",
            "states": rows,
        }
        json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    # -------- Console summary --------
    print("\n" + "=" * 60)
    print(f"Connectivity report for {tag}  (own-territory-only)")
    print("=" * 60)
    print(f"States analyzed : {len(rows)} (owned + core)")
    cap_desc = capital_state_id if capital_state_id is not None else "unknown"
    print(f"Capital state   : {cap_desc}  (distances are straight-line, not routes)")
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
                pct = r["distance_from_capital_pct_map_width"]
                dist_tag = f" [dist {pct:.1f}% map]" if pct is not None else " [dist n/a]"
                # Under strict owned-only connectivity every core-only state is
                # always its own singleton and thus always flagged -- expected,
                # not an edge case. Mark it so a claim reads differently from a
                # physically detached OWNED holding (a real accidental exclave).
                claim_note = (
                    "  <- claim only (not owned): always reported separately "
                    "under owned-only connectivity; reflects a claim without "
                    "physical control, e.g. a mutual claim / frozen conflict, "
                    "not an accidental exclave"
                    if r["relation"] == "core"
                    else ""
                )
                print(
                    f"    - state {r['state_id']:>5}  {r['state_name']:<28} "
                    f"[{r['relation']}]{impassable_tag}{dist_tag}{claim_note}"
                )

    print(f"\nWrote {csv_path}" + (f" and connectivity_{tag}.json" if args.json else ""))


if __name__ == "__main__":
    main()
