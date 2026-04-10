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
    737, 959, 1012, 1084, 1299, 1430, 1590, 1714, 1844, 1942, 2091, 2181, 2330, 2371, 2375, 2564, 2905, 3473, 3597, 4187, 4206, 4391, 4430, 4510, 4689, 4835, 5308, 5665, 5706, 5756, 5835, 6244, 11051, 11082, 11096, 11122, 11131, 11146, 11177, 11189, 11194, 11232, 11233, 11253, 11297, 11298, 11305, 11313, 11358, 11359, 11366, 11376, 11400, 11416, 11422, 11440, 11441, 11489, 11504, 11505, 11554, 11555, 11591, 11592, 11628, 11639, 11667, 11686, 11695, 11725, 11726, 11764, 11791, 11803, 11814, 11850, 11869, 11883, 11944, 11998, 15124, 18296, 231, 888, 1102, 1196, 1260, 1405, 1730, 2498, 2862, 3147, 4292, 5370, 5640, 8444, 11039, 11071, 11095, 11103, 11136, 11160, 11218, 11260, 11267, 11277, 11278, 11320, 11329, 11383, 11398, 11415, 11429, 11466, 11480, 11488, 11503, 11561, 11600, 11601, 11638, 16445, 16467, 17395, 19133, 19171, 19503, 19529, 19573, 19587, 19790
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
