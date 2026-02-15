import csv
import shutil
from datetime import datetime
from pathlib import Path

# -------------------------------------------------------------
# CONFIGURATION SECTION — EDIT ONLY THESE VALUES
# -------------------------------------------------------------

DEFINITION_FILE = "definition.csv"

# List of province IDs you want to invert
INVERT_PROVINCES = [
    3695, 5124, 9153, 9188, 9232, 9276, 9302, 11586, 15171, 15255, 15317, 15439, 15440, 15502, 15508, 15665, 15838, 15934, 16027, 16254, 16285, 16677, 16721, 16751, 16752, 16768, 16809, 17067, 17069, 17189, 17358, 17517, 17749, 17780, 17797, 18094, 18294, 18350, 18444, 18581, 18675, 18716, 18749, 18930, 18950, 19130, 19140, 19176, 19188, 19276, 19304, 19434, 19519, 19545, 19557, 19558, 19568, 19621, 19629, 19705, 19786, 19822
]

# If true, the script will NOT change any province where land/sea column == "sea"
PROTECT_SEA = True


def backup_file(path: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    backup_path = path.with_name(f"{path.name}.bak.{timestamp}")
    shutil.copy2(path, backup_path)
    print(f"Backup created: {backup_path}")
    return backup_path


def invert_coastal_flag():
    definition_path = Path(DEFINITION_FILE)

    if not definition_path.exists():
        print(f"ERROR: Cannot find {DEFINITION_FILE}")
        return

    # Backup first
    backup_file(definition_path)

    updated_rows = []
    changed_count = 0

    with definition_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        rows = list(reader)

    # HOI4 format:
    # province;R;G;B;land/sea;is_coastal;terrain;continent_id

    for row in rows:
        if not row or not row[0].isdigit():
            updated_rows.append(row)
            continue

        province_id = int(row[0])

        if province_id not in INVERT_PROVINCES:
            updated_rows.append(row)
            continue

        # row[4] is land/sea
        # row[5] is coastal flag (true/false)

        # Skip sea provinces if enabled
        if PROTECT_SEA and row[4].strip().lower() != "land":
            updated_rows.append(row)
            continue

        coastal_val = row[5].strip().lower()

        if coastal_val == "true":
            row[5] = "false"
        else:
            row[5] = "true"

        changed_count += 1
        updated_rows.append(row)

    # Write updated file
    with definition_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(updated_rows)

    print(f"Done. Inverted coastal flag for {changed_count} provinces.")


if __name__ == "__main__":
    invert_coastal_flag()
