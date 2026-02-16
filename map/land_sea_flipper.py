import csv
import shutil
from datetime import datetime
from pathlib import Path

# -------------------------------------------------------------
# CONFIGURATION SECTION
# -------------------------------------------------------------

DEFINITION_FILE = "definition.csv"

# SET THIS TO TRUE OR FALSE
# True  = Convert the IDs below to LAND (plains, continent 1)
# False = Convert the IDs below to SEA (ocean, continent 0)
SWITCH_TO_LAND = True 

# List of province IDs you want to change
TARGET_PROVINCES = [
    50, 489, 613, 658, 939, 1147, 1584, 1793, 3084, 3144, 3255, 3307, 3715, 4025, 4128, 4135, 4618, 4726, 4963, 5108, 5610, 5843, 12794, 12805, 12808, 12814, 12828, 12850, 12860, 12888, 12893, 12924, 12948, 12966, 12994, 13004, 13010, 13011, 13046, 13118, 13159, 13170, 13274, 13308, 13357, 13415, 13481, 13490, 13549, 13820, 13878, 13914, 15184, 15613, 15705, 15754, 15822, 15957, 15994, 16047, 16052, 16479, 17205, 17310, 17973, 18335, 18438, 18912, 19110, 19413, 19605
]

# -------------------------------------------------------------
# SCRIPT LOGIC
# -------------------------------------------------------------

def backup_file(path: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    backup_path = path.with_name(f"{path.name}.bak.{timestamp}")
    shutil.copy2(path, backup_path)
    print(f"Backup created: {backup_path}")
    return backup_path

def process_provinces():
    definition_path = Path(DEFINITION_FILE)

    if not definition_path.exists():
        print(f"ERROR: Cannot find {DEFINITION_FILE}")
        return

    # Create a backup before touching anything
    backup_file(definition_path)

    updated_rows = []
    changed_count = 0
    
    # Pre-process targets into a set for faster lookup
    target_set = set(TARGET_PROVINCES)

    with definition_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        rows = list(reader)

    # Expected File Structure based on your example:
    # 0: ID
    # 1: R
    # 2: G
    # 3: B
    # 4: land/sea
    # 5: is_coastal
    # 6: terrain
    # 7: continent_id

    for row in rows:
        # Check if row is valid data (starts with a number)
        if not row or not row[0].isdigit():
            updated_rows.append(row)
            continue

        province_id = int(row[0])

        if province_id in target_set:
            if SWITCH_TO_LAND:
                # SEA -> LAND transformation
                row[4] = "land"     # Type
                row[5] = "false"    # Coastal (Always false as requested)
                row[6] = "plains"   # Terrain
                row[7] = "1"        # Continent (Land default)
            else:
                # LAND -> SEA transformation
                row[4] = "sea"      # Type
                row[5] = "false"    # Coastal (Always false as requested)
                row[6] = "ocean"    # Terrain
                row[7] = "0"        # Continent (Sea default)
            
            changed_count += 1
        
        updated_rows.append(row)

    # Write the file back
    with definition_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(updated_rows)

    print(f"Done. Modified {changed_count} provinces.")
    if SWITCH_TO_LAND:
        print("Mode: SEA -> LAND (Continent 1, Plains)")
    else:
        print("Mode: LAND -> SEA (Continent 0, Ocean)")

if __name__ == "__main__":
    process_provinces()
