#!/usr/bin/env python3
"""
SEH.export_state_graph.py

Join four per-state facts into one JSON file, with no other data:
  * which states each state borders (state -> state land adjacency),
  * the state's owner,
  * the state's SEH species / ethnos / heritage (resolved to localised names).

The pieces are scattered across the mod and are not joined anywhere else:
  * land adjacency is derived from map/provinces.bmp pixel borders via the shared
    _map_common.py library (adjacencies.csv holds only strait / impassable
    exceptions, never standard land borders),
  * owner comes from history/states,
  * the SEH majority per state lives in three scripted-effect files
    (common/scripted_effects/SEH.<category>_scripted_effects.txt), each a block
    of `<stateID> = { set_variable = { SEH_<category> = <ID> } }` lines,
  * the numeric SEH IDs resolve to names through the var_SEH_<category>.<ID>
    keys in localisation/english (same source as SEH.acceptance_reference.md).

Output SEH.state_graph.json is written to the current working directory: an
envelope with provenance plus a `states` array, one record per state:
  { state_id, state_name, owner, species, ethnos, heritage, neighbors[] }
owner is null when unset; each SEH field is null when the state has no entry in
that category's file. A SEH ID with no localised name falls back to the numeric
ID as a string and is reported as a WARNING.

This script lives in the mod's root-level tools/ folder. All input files are
resolved from the script's own location (mod root = the parent of tools/), so it
can be invoked from any working directory.

Usage (from anywhere):

    python /path/to/mod/tools/SEH.export_state_graph.py [--conn 4|8]

Requires: Pillow, numpy.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from _map_common import (
    ADJACENCIES_FILE,
    DEFINITION_FILE,
    MOD_ROOT,
    PROVINCES_BMP,
    STATES_DIR,
    apply_adjacency_exceptions,
    extract_pixel_adjacency,
    parse_definition,
    parse_states,
    verify_mod_root,
)

# -------------------------------------------------------------
# PATHS / CONSTANTS
# -------------------------------------------------------------

CATEGORIES = ["species", "ethnos", "heritage"]

SEH_EFFECT_DIR = MOD_ROOT / "common" / "scripted_effects"
EFFECT_FILES = {
    cat: SEH_EFFECT_DIR / f"SEH.{cat}_scripted_effects.txt" for cat in CATEGORIES
}
LOC_DIR = MOD_ROOT / "localisation" / "english"

OUTPUT_FILE = "SEH.state_graph.json"

# `<stateID> = { set_variable = { SEH_<cat> = <ID> } }`  -- same shape the
# acceptance-reference tool matches. Captures (state_id, value).
STATE_SET_RE = {
    cat: re.compile(
        r"(\d+)\s*=\s*\{\s*set_variable\s*=\s*\{\s*SEH_" + cat + r"\s*=\s*(\d+)"
    )
    for cat in CATEGORIES
}
LOC_LINE_RE = re.compile(r'^\s*([\w.\-]+):\d*\s+"(.*)"')


# -------------------------------------------------------------
# SEH per-state majority
# -------------------------------------------------------------


def parse_state_seh(cat):
    """{state_id: seh_id} for one category, from its scripted-effects file."""
    result = {}
    try:
        text = EFFECT_FILES[cat].read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return result
    for state_id, value in STATE_SET_RE[cat].findall(text):
        result[int(state_id)] = int(value)
    return result


# -------------------------------------------------------------
# SEH ID -> localised name
# -------------------------------------------------------------


def _resolve_refs(loc):
    """Expand $ref$ substitutions in place (a few shallow passes are enough)."""
    ref_re = re.compile(r"\$([\w.\-]+)\$")
    for key in list(loc.keys()):
        val = loc[key]
        if "$" not in val:
            continue
        for _ in range(5):
            new = ref_re.sub(lambda m: loc.get(m.group(1), m.group(0)), val)
            if new == val:
                break
            val = new
        loc[key] = val


def parse_id_names():
    """{category: {id: name}} from the var_SEH_<category>.<id> base loc keys.

    Every english .yml is scanned (not just the SEH file) so $ref$ names that
    point at keys defined elsewhere still resolve. First non-empty writer wins,
    matching SEH.generate_acceptance_reference.py.
    """
    loc = {}
    for path in sorted(LOC_DIR.glob("**/*.yml")):
        try:
            text = path.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
        for line in text.splitlines():
            stripped = line.lstrip()
            if not stripped or stripped.startswith("#"):
                continue
            m = LOC_LINE_RE.match(line)
            if not m:
                continue
            key, val = m.group(1), m.group(2)
            if key not in loc or (loc[key] == "" and val != ""):
                loc[key] = val
    _resolve_refs(loc)

    names = {c: {} for c in CATEGORIES}
    for cat in CATEGORIES:
        pat = re.compile(r"^var_SEH_" + cat + r"\.(\d+)$")
        for key, val in loc.items():
            m = pat.match(key)
            if m:
                names[cat][int(m.group(1))] = val
    return names


# -------------------------------------------------------------
# MAIN
# -------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(
        description="Export per-state land adjacency, owner, and SEH "
        "species/ethnos/heritage (localised) to SEH.state_graph.json."
    )
    ap.add_argument(
        "--conn",
        type=int,
        choices=(4, 8),
        default=4,
        help="Pixel connectivity: 4 = orthogonal (default), 8 = include diagonals",
    )
    args = ap.parse_args()

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
            "  This script must stay inside <mod_root>/tools/. Move it back or "
            "adjust MOD_ROOT."
        )
        sys.exit(1)

    for p in (DEFINITION_FILE, PROVINCES_BMP, ADJACENCIES_FILE):
        if not p.exists():
            print(f"ERROR: cannot find {p}")
            sys.exit(1)

    # --- Land adjacency (province level) ---
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

    # --- States and province -> state map ---
    print(f"Parsing states in {STATES_DIR} ...")
    states = parse_states(STATES_DIR)
    prov2state = {}
    for st in states:
        for pid in st["provinces"]:
            prov2state[pid] = st["id"]
    print(f"  {len(states)} states, {len(prov2state)} provinces assigned.")

    # --- State -> state adjacency (ownership-agnostic) ---
    # Same pair loop as _check_connectivity.py, minus its owned-only filter:
    # map both endpoints of every province border to their states; a differing,
    # both-resolved pair is a state border. Kept symmetric.
    state_adj = defaultdict(set)
    for pair in land_adj:
        a, b = tuple(pair)
        sa = prov2state.get(a)
        sb = prov2state.get(b)
        if sa is None or sb is None or sa == sb:
            continue
        state_adj[sa].add(sb)
        state_adj[sb].add(sa)

    # --- SEH majority per state, and ID -> name resolution ---
    seh_by_state = {cat: parse_state_seh(cat) for cat in CATEGORIES}
    id_names = parse_id_names()

    # --- Assemble one record per state ---
    unresolved = {c: set() for c in CATEGORIES}

    def seh_field(cat, sid):
        seh_id = seh_by_state[cat].get(sid)
        if seh_id is None:
            return None
        name = id_names[cat].get(seh_id)
        if name is None:
            unresolved[cat].add(seh_id)
            return str(seh_id)  # fall back to the raw ID, flagged below
        return name

    records = []
    for st in sorted(states, key=lambda s: s["id"]):
        sid = st["id"]
        records.append(
            {
                "state_id": sid,
                "state_name": st["name"],
                "owner": st["owner"],
                "species": seh_field("species", sid),
                "ethnos": seh_field("ethnos", sid),
                "heritage": seh_field("heritage", sid),
                "neighbors": sorted(state_adj.get(sid, ())),
            }
        )

    # --- Output ---
    payload = {
        "map": MOD_ROOT.name,
        "generated_by": Path(__file__).name,
        "pixel_connectivity": args.conn,
        "sea_crossings": "all_strait_crossings_bridge",
        "state_count": len(records),
        "states": records,
    }
    out_path = Path(OUTPUT_FILE)
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    # --- Console summary ---
    print("\n" + "=" * 60)
    print("State SEH + adjacency export")
    print("=" * 60)
    print(f"States written  : {len(records)}")
    edge_count = sum(len(v) for v in state_adj.values()) // 2
    print(f"State borders    : {edge_count} undirected edge(s)")
    for cat in CATEGORIES:
        assigned = sum(1 for r in records if r[cat] is not None)
        print(f"{cat.capitalize():<9} assigned: {assigned}/{len(records)}")

    for cat in CATEGORIES:
        if unresolved[cat]:
            ids = ", ".join(str(v) for v in sorted(unresolved[cat]))
            print(
                f"  WARNING undefined {cat} ID(s) with no localised name "
                f"(emitted as raw ID): {ids}"
            )

    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
