import csv
import shutil
from datetime import datetime
from pathlib import Path

# -------------------------------------------------------------
# CONFIGURATION SECTION — EDIT ONLY THESE VALUES
# -------------------------------------------------------------

DEFINITION_FILE = "definition.csv"

# The new terrain type to apply (e.g., "forest", "mountain", "plains", "urban", "desert")
NEW_TERRAIN = "desert"

# List of province IDs you want to change to the NEW_TERRAIN
TARGET_PROVINCES = [
	10, 2801, 3305, 4809, 5160, 13987, 14015, 14057, 14070, 14463, 18370
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
