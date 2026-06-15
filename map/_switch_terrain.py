import csv
import shutil
from datetime import datetime
from pathlib import Path

# -------------------------------------------------------------
# CONFIGURATION SECTION — EDIT ONLY THESE VALUES
# -------------------------------------------------------------

DEFINITION_FILE = "definition.csv"

# The new terrain type to apply (e.g., "forest", "mountain", "plains", "urban", "desert")
NEW_TERRAIN = "jungle"

# List of province IDs you want to change to the NEW_TERRAIN
TARGET_PROVINCES = [
	193, 317, 1594, 1735, 1888, 1930, 2518, 3659, 3918, 3979, 4310, 4361, 4878, 4895, 5130, 5229, 5385, 5713, 6235, 12320, 12438, 12446, 12459, 12470, 12475, 12476, 12481, 12486, 12502, 12528, 12529, 12574, 12590, 12608, 12609, 12626, 12652, 12653, 12684, 12700, 318, 761, 857, 1264, 1598, 3457, 4379, 4670, 4719, 5345, 5856, 12270, 12280, 12297, 12306, 12313, 12336, 12349, 12350, 12358, 12364, 12378, 12397, 12419, 12426, 12460, 12463, 12464, 12477, 12487, 12497, 12498, 12503, 12519, 12543, 12544, 173, 294, 408, 503, 2275, 2694, 4504, 4600, 4642, 5442, 5484, 5496, 5752, 5920, 11992, 12025, 12075, 12107, 12108, 12147, 12148, 12158, 12192, 12201, 12202, 12234, 12253, 12298, 12307, 12314, 12321, 12365, 12379, 12380, 12414
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

def switch_terrain():
	definition_path = Path(DEFINITION_FILE)

	if not definition_path.exists():
		print(f"ERROR: Cannot find {DEFINITION_FILE}")
		return

	# Create a backup before modifying the file
	backup_file(definition_path)

	updated_rows = []
	changed_count = 0
	target_set = set(TARGET_PROVINCES)

	with definition_path.open("r", newline="", encoding="utf-8") as f:
		reader = csv.reader(f, delimiter=';')
		rows = list(reader)

	# Expected File Structure:
	# 0: ID
	# 1: R
	# 2: G
	# 3: B
	# 4: land/sea
	# 5: is_coastal
	# 6: terrain
	# 7: continent_id

	for row in rows:
		if not row or not row[0].isdigit():
			updated_rows.append(row)
			continue

		province_id = int(row[0])

		if province_id in target_set:
			# Overwrite the terrain column (index 6)
			row[6] = NEW_TERRAIN
			changed_count += 1
			
		updated_rows.append(row)

	# Write the modified data back to the CSV
	with definition_path.open("w", newline="", encoding="utf-8") as f:
		writer = csv.writer(f, delimiter=';')
		writer.writerows(updated_rows)

	print(f"Done. Changed terrain to '{NEW_TERRAIN}' for {changed_count} provinces.")

if __name__ == "__main__":
	switch_terrain()
