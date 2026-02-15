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
    1325, 1507, 1607, 3695, 3852, 5124, 6291, 6294, 6309, 9153, 9188, 9232, 9276, 9302, 10775, 11586, 15171, 15218, 15228, 15255, 15317, 15422, 15439, 15440, 15502, 15508, 15509, 15569, 15602, 15665, 15775, 15828, 15838, 15934, 15935, 16027, 16078, 16254, 16285, 16597, 16640, 16677, 16721, 16751, 16752, 16768, 16809, 17011, 17021, 17067, 17069, 17119, 17180, 17189, 17358, 17517, 17521, 17749, 17780, 17797, 17830, 18031, 18094, 18294, 18350, 18411, 18444, 18581, 18675, 18716, 18749, 18930, 18950, 19077, 19130, 19140, 19176, 19187, 19188, 19227, 19253, 19258, 19276, 19304, 19434, 19449, 19519, 19520, 19545, 19548, 19557, 19558, 19568, 19621, 19629, 19644, 19705, 19786, 19822
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
