#!/usr/bin/env python3
"""
update_continents_by_region.py

Bulk-update HoI4 map/definition.csv continent IDs by mapping:
    continent_id -> [ strategic_region_id, ... ]

Behavior:
 - Reads strategic region files in --strategy-dir (expects files like "1-region.txt")
 - Extracts numbers inside the provinces = { ... } block only (ignores weather block)
 - Builds continent -> province sets from the strategic region mapping
 - Optionally merges any direct province_assignments (continent -> [provinceIDs]) if present
 - Will NOT change rows where continent == 0 or land/sea == "sea"
 - Creates timestamped backup before writing
 - Dry-run and verbose modes available

Usage:
  python update_continents_by_region.py --definitions map/definition.csv \
      --strategy-dir map/strategicregions --config config.json --dry-run --verbose

Config file (JSON) example shown below in the docs.

Dry run (preview only; no files changed):
python update_continents.py --definitions definition.csv --strategy-dir strategicregions --config config.json --dry-run --verbose

Apply the changes (writes definition.csv; creates a timestamped backup):
python update_continents.py --definitions definition.csv --strategy-dir strategicregions --config config.json --verbose
"""

import argparse
import csv
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple

# -------------------------
# Default in-script CONFIG
# -------------------------
# You can edit this block or supply an external JSON --config file.
# New preferred mapping: "continent_strategy_assignments": { "<continent_id>": [ <strategic_region_ids> ] }
default_config = {
    # Optional direct province assignments (fallback / extra)
    "province_assignments": {
        # e.g. "1": [1,2,3]
    },

    # Primary mode: continent -> list of strategic region ids
    "continent_strategy_assignments": {
        # e.g. "1": [1, 2, 3],  "6": [10,11]
    },

    "protect_zero": True,
    "protect_sea": True
}

# -------------------------
# Helpers
# -------------------------
def parse_args():
    p = argparse.ArgumentParser(description="Bulk update continent IDs using strategic region IDs.")
    p.add_argument("--definitions", "-d", required=True, help="Path to map/definition.csv")
    p.add_argument("--strategy-dir", "-s", required=True, help="Path to map/strategicregions/ directory")
    p.add_argument("--config", "-c", required=False, help="JSON config file (optional). If omitted, the defaults in the script are used.")
    p.add_argument("--dry-run", action="store_true", help="Don't write changes; preview only")
    p.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    return p.parse_args()

def load_json_config(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)

def read_definition_csv(path: Path) -> Tuple[List[str], List]:
    """
    Read file lines and also parse CSV-like lines by semicolon.
    Returns (raw_lines, parsed_rows) where parsed_rows entries are either:
      - list of fields (CSV line split) or
      - raw string for non-CSV lines (blank/comments)
    """
    raw = path.read_text(encoding="utf-8").splitlines(keepends=True)
    parsed = []
    for line in raw:
        if line.strip() == "":
            parsed.append(line)   # keep blank line raw
            continue
        if line.count(";") < 2:
            # non-CSV-ish line -> keep raw
            parsed.append(line)
            continue
        # parse CSV tokens
        tokens = next(csv.reader([line], delimiter=';'))
        parsed.append(tokens)
    return raw, parsed

def backup_file(path: Path) -> Path:
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bak = path.with_name(path.name + f".bak.{stamp}")
    shutil.copy2(path, bak)
    return bak

def parse_provinces_from_region_file(file_path: Path) -> Set[int]:
    """
    Extract integers inside provinces = { ... } block.
    Uses a targeted regex and will not try to parse weather or other blocks.
    """
    txt = file_path.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r'provinces\s*=\s*\{([^}]*)\}', txt, re.DOTALL)
    if not m:
        return set()
    content = m.group(1)
    nums = re.findall(r'\d+', content)
    return set(int(n) for n in nums)

def build_strategic_region_map(strategy_dir: Path, verbose=False) -> Dict[int, Set[int]]:
    """
    Return mapping: strategic_region_id -> set(province ids).
    We detect region id from filename prefix (\d+) or internal 'id = N' in the file.
    """
    out = {}
    if not strategy_dir.exists() or not strategy_dir.is_dir():
        if verbose:
            print(f"Strategy dir {strategy_dir} missing or not a directory.")
        return out
    for f in strategy_dir.iterdir():
        if not f.is_file():
            continue
        # only consider .txt files typically
        if not f.name.lower().endswith(".txt"):
            continue
        # try filename leading number
        m = re.match(r'(\d+)', f.name)
        region_id = None
        if m:
            region_id = int(m.group(1))
        else:
            # try to find "id = N" inside file
            txt = f.read_text(encoding="utf-8", errors="ignore")
            mm = re.search(r'\bid\s*=\s*(\d+)', txt)
            if mm:
                region_id = int(mm.group(1))
        if region_id is None:
            if verbose:
                print(f"Could not determine region id for file {f.name}; skipping.")
            continue
        provs = parse_provinces_from_region_file(f)
        out[region_id] = provs
        if verbose:
            print(f"Loaded strategic region {region_id} from {f.name}: {len(provs)} provinces")
    return out

def apply_updates(rows, prov_to_target: Dict[int, int], protect_zero=True, protect_sea=True, verbose=False):
    """
    rows: list of parsed rows (some entries are list-of-fields, others raw strings)
    prov_to_target: mapping province_id -> target_continent_id
    Returns (new_rows, changes_list)
    """
    changes = []
    new_rows = []
    for entry in rows:
        if isinstance(entry, list):
            fields = entry.copy()
            # require first field be digit
            if not fields or not fields[0].strip().isdigit():
                new_rows.append(entry)
                continue
            prov_id = int(fields[0].strip())
            # get current continent - assume last field
            try:
                current_continent = int(fields[-1].strip())
            except Exception:
                new_rows.append(entry)
                continue
            # check protections
            if protect_zero and current_continent == 0:
                new_rows.append(entry)
                continue
            land_or_sea = fields[4].strip().lower() if len(fields) > 4 else ""
            if protect_sea and land_or_sea == "sea":
                new_rows.append(entry)
                continue
            # apply if mapping present
            if prov_id in prov_to_target:
                target = int(prov_to_target[prov_id])
                if current_continent != target:
                    old = current_continent
                    fields[-1] = str(target)
                    changes.append((prov_id, old, target))
                    if verbose:
                        print(f"Change province {prov_id}: {old} -> {target}")
            new_rows.append(fields)
        else:
            # raw string
            new_rows.append(entry)
    return new_rows, changes

# -------------------------
# Main
# -------------------------
def main():
    args = parse_args()
    defs_path = Path(args.definitions)
    strategy_dir = Path(args.strategy_dir)

    if not defs_path.exists():
        print(f"Definitions file {defs_path} not found.", file=sys.stderr)
        sys.exit(1)
    if not strategy_dir.exists():
        print(f"Strategic regions directory {strategy_dir} not found.", file=sys.stderr)
        sys.exit(1)

    # load config
    config = default_config.copy()
    if args.config:
        try:
            external = load_json_config(args.config)
            config.update(external)
        except Exception as e:
            print(f"Failed to load config {args.config}: {e}", file=sys.stderr)
            sys.exit(1)

    # normalize direct province assignments (optional)
    province_assignments = {}
    for k, v in config.get("province_assignments", {}).items():
        cont = int(k)
        if isinstance(v, str):
            nums = [int(x) for x in re.findall(r'\d+', v)]
        else:
            nums = [int(x) for x in v]
        province_assignments[cont] = set(nums)

    # normalize continent -> strategic region list
    continent_strategy = {}
    for k, v in config.get("continent_strategy_assignments", {}).items():
        cont = int(k)
        if isinstance(v, str):
            region_ids = [int(x) for x in re.findall(r'\d+', v)]
        else:
            region_ids = [int(x) for x in v]
        continent_strategy[cont] = set(region_ids)

    protect_zero = bool(config.get("protect_zero", True))
    protect_sea = bool(config.get("protect_sea", True))

    # Build strategic region map from files
    sr_map = build_strategic_region_map(strategy_dir, verbose=args.verbose)

    # Compose mapping continent -> province set
    assign_map: Dict[int, Set[int]] = {}
    # Add provinces from continent_strategy mapping
    for cont, sr_ids in continent_strategy.items():
        provs = set()
        for sr in sr_ids:
            found = sr_map.get(sr)
            if found:
                provs.update(found)
            else:
                if args.verbose:
                    print(f"Warning: strategic region {sr} referenced for continent {cont} but not found in {strategy_dir}.")
        if provs:
            assign_map.setdefault(cont, set()).update(provs)

    # Merge direct province_assignments (if any)
    for cont, provs in province_assignments.items():
        assign_map.setdefault(cont, set()).update(provs)

    if args.verbose:
        total = sum(len(s) for s in assign_map.values())
        print(f"Prepared assignments for {len(assign_map)} continents totalling {total} provinces.")

    # Build reverse map province -> target continent (first-match wins arbitrarily)
    prov_to_target = {}
    for cont, provs in assign_map.items():
        for p in provs:
            if p in prov_to_target:
                # already assigned by earlier cont key; keep existing (documented behavior)
                continue
            prov_to_target[p] = cont

    # read definitions CSV
    raw_lines, parsed_rows = read_definition_csv(defs_path)

    # apply updates
    new_rows, changes = apply_updates(parsed_rows, prov_to_target,
                                      protect_zero=protect_zero,
                                      protect_sea=protect_sea,
                                      verbose=args.verbose)

    if not changes:
        print("No changes detected.")
        return

    print(f"{len(changes)} provinces would be changed.")
    if args.dry_run or args.verbose:
        for pid, old, new in changes:
            print(f"  province {pid}: {old} -> {new}")

    if args.dry_run:
        print("Dry-run: no file written. Remove --dry-run to apply changes.")
        return

    # backup and write
    bak = backup_file(defs_path)
    if args.verbose:
        print(f"Backed up {defs_path} -> {bak}")

    # write result: keep non-CSV raw lines intact, join CSV lists by ';'
    with defs_path.open("w", encoding="utf-8", newline='') as fh:
        for entry in new_rows:
            if isinstance(entry, str):
                fh.write(entry if entry.endswith("\n") else entry + "\n")
            elif isinstance(entry, list):
                fh.write(";".join(entry).rstrip("\n") + "\n")
            else:
                fh.write(str(entry) + "\n")

    print(f"Wrote updated definitions to {defs_path}. Backup saved as {bak}.")

if __name__ == "__main__":
    main()
