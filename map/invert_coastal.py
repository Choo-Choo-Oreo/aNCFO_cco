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
    6, 14, 73, 95, 97, 101, 115, 170, 180, 195, 222, 240, 296, 309, 316, 335, 381, 501, 507, 547, 554, 559, 562, 580, 585, 635, 640, 649, 685, 728, 780, 803, 806, 808, 821, 826, 878, 969, 1203, 1217, 1258, 1279, 1340, 1362, 1422, 1471, 1495, 1497, 1521, 1573, 1581, 1588, 1592, 1600, 1670, 1678, 1710, 1721, 1752, 1760, 1856, 1884, 1933, 1945, 1965, 2080, 2083, 2104, 2115, 2173, 2184, 2299, 2310, 2347, 2426, 2572, 2594, 2633, 2711, 2805, 2858, 2885, 2911, 2914, 3058, 3062, 3100, 3129, 3164, 3193, 3253, 3281, 3322, 3328, 3332, 3341, 3342, 3420, 3444, 3492, 3515, 3589, 3622, 3693, 3702, 3733, 3734, 3790, 3877, 3883, 3890, 3978, 4006, 4015, 4045, 4252, 4267, 4426, 4470, 4720, 4947, 5065, 5103, 5152, 5192, 5226, 5234, 5250, 5578, 5620, 5685, 5764, 5799, 5846, 6060, 6163, 6198, 6230, 6249, 6275, 6278, 6319, 6321, 6322, 6324, 6325, 6327, 6330, 6331, 6333, 6334, 6335, 6342, 6343, 6344, 6348, 6350, 6351, 6353, 6358, 6359, 6361, 6368, 6370, 6371, 6373, 6374, 6375, 6376, 6378, 6379, 6380, 6381, 6384, 6385, 6386, 6388, 6393, 6406, 6407, 6408, 6418, 6460, 6462, 6476, 6480, 6487, 6492, 6502, 6503, 6549, 6571, 6611, 6659, 6683, 6689, 6756, 6759, 6765, 6798, 6813, 6872, 8930, 8993, 9028, 9077, 9200, 9265, 9567, 9706, 9970, 10094, 10270, 10363, 10457, 10464, 10599, 10664, 10740, 12110, 14212, 14261, 14323, 14690, 15189, 15238, 15249, 15305, 15313, 15333, 15334, 15376, 15377, 15485, 15511, 15514, 15544, 15574, 15604, 15623, 15633, 15696, 15708, 15734, 15745, 15761, 15782, 15791, 15836, 15851, 15865, 15876, 15904, 15912, 15931, 15942, 15944, 15949, 15956, 15966, 15995, 16004, 16070, 16159, 16164, 16169, 16173, 16219, 16224, 16234, 16264, 16266, 16294, 16315, 16401, 16428, 16458, 16463, 16488, 16513, 16530, 16596, 16611, 16653, 16686, 16691, 16705, 16707, 16742, 16826, 16839, 16840, 16875, 16904, 16915, 16930, 16932, 16960, 16971, 16997, 17036, 17039, 17046, 17071, 17077, 17117, 17227, 17252, 17253, 17295, 17317, 17327, 17424, 17435, 17463, 17544, 17600, 17602, 17681, 17722, 17723, 17740, 17784, 17854, 17868, 17926, 17942, 17972, 17984, 17989, 18005, 18030, 18038, 18102, 18115, 18172, 18180, 18184, 18185, 18224, 18242, 18313, 18345, 18351, 18365, 18369, 18386, 18409, 18454, 18461, 18482, 18485, 18488, 18523, 18554, 18564, 18583, 18594, 18651, 18723, 18751, 18760, 18800, 18860, 18908, 18920, 18927, 18940, 18948, 19007, 19010, 19027, 19031, 19096, 19142, 19149, 19182, 19184, 19185, 19196, 19197, 19200, 19202, 19206, 19209, 19211, 19218, 19226, 19238, 19251, 19266, 19268, 19273, 19274, 19293, 19301, 19308, 19350, 19375, 19377, 19382, 19383, 19390, 19393, 19427, 19437, 19439, 19504, 19513, 19544, 19570, 19575, 19631, 19779
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
