"""
update_continents.py

Bulk-update HoI4 map/definition.csv continent IDs using Strategic Regions.

USAGE COMMAND:
py _update_continents.py -d definition.csv -s strategicregions -c config.json --verbose
"""

import argparse
import json
import re
import shutil
import sys
import time
from pathlib import Path
from typing import Dict, List, Set, Tuple

# -------------------------
# Default CONFIG
# -------------------------
default_config = {
    "province_assignments": {},
    "continent_strategy_assignments": {},
    "protect_zero": True,
    "protect_sea": True
}

# -------------------------
# Compiled Regex for Speed
# -------------------------
# Finds the "provinces = { ... }" block
RE_PROVINCES_BLOCK = re.compile(r'provinces\s*=\s*\{([^}]*)\}', re.DOTALL)
# Finds all numbers in a string
RE_NUMBERS = re.compile(r'\d+')
# Finds "id = 123" in region files
RE_REGION_ID = re.compile(r'\bid\s*=\s*(\d+)')

# -------------------------
# Helpers
# -------------------------
def parse_args():
    p = argparse.ArgumentParser(description="Bulk update continent IDs (Optimized).")
    p.add_argument("--definitions", "-d", required=True, help="Path to map/definition.csv")
    p.add_argument("--strategy-dir", "-s", required=True, help="Path to map/strategicregions/")
    p.add_argument("--config", "-c", required=False, help="JSON config file.")
    p.add_argument("--dry-run", action="store_true", help="Preview only")
    p.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    return p.parse_args()

def load_json_config(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)

def read_definition_csv_fast(path: Path) -> Tuple[List[str], List]:
    """
    Fast reader. Instead of csv.reader per line, simply split by ';'.
    Returns (raw_lines, parsed_rows)
    """
    raw_lines = []
    parsed_rows = []
    
    with path.open("r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    for line in raw_lines:
        stripped = line.strip()
        # Keep empty lines or comments as raw strings
        if not stripped or stripped.startswith('#') or ';' not in line:
            parsed_rows.append(line) 
            continue
        
        # Fast split
        tokens = line.strip().split(';')
        parsed_rows.append(tokens)

    return raw_lines, parsed_rows

def parse_provinces_from_region_file(txt: str) -> Set[int]:
    m = RE_PROVINCES_BLOCK.search(txt)
    if not m:
        return set()
    return set(int(n) for n in RE_NUMBERS.findall(m.group(1)))

def build_strategic_region_map(strategy_dir: Path, verbose=False) -> Dict[int, Set[int]]:
    out = {}
    if not strategy_dir.exists():
        return out
    
    files = list(strategy_dir.glob("*.txt"))
    if verbose:
        print(f"Scanning {len(files)} strategic region files...")

    for f in files:
        txt = f.read_text(encoding="utf-8", errors="ignore")
        
        # 1. Try filename for ID
        region_id = None
        m_name = RE_NUMBERS.match(f.name)
        if m_name:
            region_id = int(m_name.group(0))
        
        # 2. Fallback: Look inside file
        if region_id is None:
            m_id = RE_REGION_ID.search(txt)
            if m_id:
                region_id = int(m_id.group(1))

        if region_id is None:
            continue

        out[region_id] = parse_provinces_from_region_file(txt)
        
    return out

def apply_updates(rows, prov_to_target: Dict[int, int], protect_zero=True, protect_sea=True):
    changes = []
    new_rows = []
    
    for entry in rows:
        # If it's a string, it's a comment/blank line; preserve it
        if isinstance(entry, str):
            new_rows.append(entry)
            continue

        # entry is a list of columns
        # Index 0: ID, Index 4: Type (land/sea), Index -1 (or 7): Continent
        # Safety check for short rows
        if len(entry) < 8: 
            new_rows.append(entry)
            continue
            
        try:
            prov_id = int(entry[0])
            current_continent = int(entry[-1]) if entry[-1].isdigit() else 0
        except ValueError:
            new_rows.append(entry)
            continue

        # Checks
        if protect_zero and current_continent == 0:
            new_rows.append(entry)
            continue
            
        if protect_sea:
            # Check column 4 (land/sea)
            prov_type = entry[4].lower() if len(entry) > 4 else ""
            if prov_type == 'sea':
                new_rows.append(entry)
                continue

        # Apply Update
        if prov_id in prov_to_target:
            target = prov_to_target[prov_id]
            if current_continent != target:
                old = current_continent
                entry[-1] = str(target)
                changes.append((prov_id, old, target))

        new_rows.append(entry)

    return new_rows, changes

# -------------------------
# Main
# -------------------------
def main():
    start_time = time.time()
    args = parse_args()
    defs_path = Path(args.definitions)
    strategy_dir = Path(args.strategy_dir)

    if not defs_path.exists():
        sys.exit(f"Error: {defs_path} not found.")

    # Load Config
    config = default_config.copy()
    if args.config:
        try:
            config.update(load_json_config(args.config))
        except Exception as e:
            sys.exit(f"Config Error: {e}")

    # 1. Build Map: Continent -> Strategic Region List
    continent_strategy = {}
    for k, v in config.get("continent_strategy_assignments", {}).items():
        # Handle string inputs "1 2 3" or lists [1, 2, 3]
        ids = [int(x) for x in re.findall(r'\d+', str(v))]
        continent_strategy[int(k)] = set(ids)

    # 2. Scan Strategic Regions files
    sr_map = build_strategic_region_map(strategy_dir, verbose=args.verbose)

    # 3. Build Lookup: Province ID -> Target Continent
    prov_to_target = {}
    
    # Process Strategy Regions
    for cont_id, region_ids in continent_strategy.items():
        for rid in region_ids:
            if rid in sr_map:
                for pid in sr_map[rid]:
                    prov_to_target[pid] = cont_id

    # Process Direct Province Assignments (Overrides)
    for k, v in config.get("province_assignments", {}).items():
        cont_id = int(k)
        pids = [int(x) for x in re.findall(r'\d+', str(v))]
        for pid in pids:
            prov_to_target[pid] = cont_id

    if args.verbose:
        print(f"Mapped {len(prov_to_target)} provinces to new continents.")

    # 4. Read & Process Definition.csv
    raw_lines, parsed_rows = read_definition_csv_fast(defs_path)
    new_rows, changes = apply_updates(parsed_rows, prov_to_target, 
                                      protect_zero=config.get("protect_zero", True),
                                      protect_sea=config.get("protect_sea", True))

    print(f"Processed {len(parsed_rows)} rows. Found {len(changes)} updates.")

    if not changes:
        print("No changes needed.")
        return

    if args.dry_run:
        print("Dry run complete. No files changed.")
        return

    # 5. Write Output
    backup_path = defs_path.with_name(f"{defs_path.name}.bak.{int(time.time())}")
    shutil.copy2(defs_path, backup_path)
    if args.verbose: 
        print(f"Backup saved: {backup_path.name}")

    with defs_path.open("w", encoding="utf-8", newline='') as f:
        for row in new_rows:
            if isinstance(row, list):
                f.write(";".join(row) + "\n")
            else:
                f.write(row) # Preserve original line endings/content

    print(f"Success! Updated definition.csv in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
