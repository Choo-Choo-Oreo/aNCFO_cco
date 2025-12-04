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
    6, 66, 70, 93, 113, 129, 147, 155, 158, 162, 216, 237, 287, 302, 325, 359, 386, 396, 472, 543, 574, 625, 661, 682, 770, 805, 817, 859, 909, 1026, 1060, 1151, 1174, 1203, 1362, 1380, 1404, 1414, 1440, 1460, 1498, 1507, 1545, 1547, 1676, 1748, 1792, 1828, 1841, 1933, 2011, 2058, 2082, 2113, 2173, 2271, 2277, 2422, 2457, 2829, 2911, 2928, 2969, 3008, 3043, 3100, 3168, 3193, 3194, 3277, 3342, 3804, 3841, 3852, 4055, 4102, 4164, 4431, 4528, 4814, 4837, 4925, 5050, 5353, 5360, 5750, 5789, 6237, 6262, 6263, 6265, 6266, 6267, 6268, 6269, 6272, 6276, 6281, 6282, 6284, 6287, 6288, 6289, 6290, 6292, 6294, 6296, 6297, 6299, 6302, 6303, 6309, 6310, 6312, 6314, 6316, 6321, 6326, 6331, 6332, 6334, 7083, 7088, 7246, 7293, 7407, 7466, 7505, 7754, 10775, 15311, 16922, 17518
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
