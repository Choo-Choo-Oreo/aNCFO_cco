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
    38, 373, 468, 578, 915, 937, 1153, 1157, 1183, 1313, 1636, 2175, 2217, 2384, 2397, 2645, 2828, 2960, 3016, 3471, 3981, 4047, 4308, 5191, 5458, 5541, 5569, 10057, 12209, 13497, 13725, 13757, 13821, 13822, 13831, 13879, 13888, 14024, 14039, 14106, 14274, 14353, 14683, 14738, 14770, 14944, 14975, 15144, 16141, 16145, 16548, 16936, 17188, 17519, 17630, 17644, 17960, 18206, 18227, 18425, 18870, 18895, 19018, 19049, 19109, 19714, 19726, 19727, 19729, 19740, 19753
    # add more IDs here...
]

# If true, the script will NOT change any province where land/sea column == "sea"
PROTECT_SEA = True

# -------------------------------------------------------------
# END OF CONFIG
# -------------------------------------------------------------


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

    # HOI4 format assumption:
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
