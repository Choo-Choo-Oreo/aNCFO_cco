import os
import re
import csv

# Friendly dataset labels keyed by the header's first data column (the column
# right after Country_Tag). Each generator effect logs its own header, so this
# is what tells the three datasets apart when they dump at the same timestamp:
#   ECO_generate_csv_data_per_country        -> Country_Population_K
#   LCfN_generate_csv_naval_capacity_data    -> Calculated_Naval_Cap
#   OCfA_generate_csv_battalion_capacity_data-> Total_Divisions
# Unknown headers fall back to a sanitised version of that column name, so a new
# generator added later still gets its own separate files instead of colliding.
DATASET_LABELS = {
    "Country_Population_K": "economy",
    "Calculated_Naval_Cap": "naval",
    "Total_Divisions": "army",
}


def dataset_label(header):
    """Return a short, filesystem-safe name identifying which generator produced
    this header. Uses the first data column; falls back to a sanitised form."""
    if len(header) >= 2:
        key = header[1]
        if key in DATASET_LABELS:
            return DATASET_LABELS[key]
        return re.sub(r"[^A-Za-z0-9]+", "_", key).strip("_").lower() or "unknown"
    return "unknown"


def generate_country_reports(log_file_path, output_dir):
    # regex supports alphanumeric tags (e.g., D01) and game timestamps
    log_pattern = re.compile(r'\[.*?\]\[(?P<date>\d{4}\.\d{2}\.\d{2}\.\d{2})\]\[.*?\]:\s*(?P<csv_data>[A-Z0-9]{3},.*)')
    raw_csv_pattern = re.compile(r'^([A-Z0-9]{3}(?:,-?\d+(?:\.\d+)?%?)+)')

    # Keyed by (dataset_label, timestamp) so ECO/LCfN/OCfA dumps that share an
    # in-game timestamp no longer overwrite each other (the original code keyed
    # on timestamp alone and kept only whichever dataset was seen first).
    reports_data = {}
    current_timestamp = "Unknown"
    current_header = []
    current_label = "unknown"

    if not os.path.exists(log_file_path):
        print(f"Error: Could not find the log file at {log_file_path}")
        return

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def bucket_for(timestamp):
        key = (current_label, timestamp)
        if key not in reports_data:
            reports_data[key] = {
                'header': current_header.copy(),
                'rows': [],
                'seen': set(),
            }
        return reports_data[key]

    def add_row(timestamp, data_row):
        # Deduplicate identical rows within a (dataset, timestamp) bucket. The
        # LCfN/OCfA generators are (as of 2026-07-15) invoked from an unguarded
        # on_monthly that fires once per country, so each monthly dump repeats
        # every country's row ~N times. The first column is the unique country
        # tag, so an identical full row is the same logical record; a report
        # wants one row per country per timestamp regardless of that wiring.
        bucket = bucket_for(timestamp)
        signature = tuple(data_row)
        if signature in bucket['seen']:
            return
        bucket['seen'].add(signature)
        bucket['rows'].append(data_row)

    with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip()

            if "Country_Tag" in line:
                header_match = re.search(r'Country_Tag.*', line)
                if header_match:
                    current_header = header_match.group(0).split(',')
                    current_label = dataset_label(current_header)
                continue

            match = log_pattern.search(line)
            if match:
                current_timestamp = match.group('date')

                csv_string = match.group('csv_data')
                data_row = csv_string.split(',')

                if current_header and len(data_row) == len(current_header):
                    add_row(current_timestamp, data_row)
                continue

            raw_match = raw_csv_pattern.search(line)
            if raw_match:
                data_row = raw_match.group(1).split(',')
                if current_header and len(data_row) == len(current_header):
                    add_row(current_timestamp, data_row)

    if not reports_data:
        print("No valid country data matching the header structure was found in the log.")
        return

    for (label, timestamp), data in reports_data.items():
        extracted_data = data['rows']
        header = data['header']

        if not extracted_data:
            continue

        safe_timestamp = timestamp.replace('.', '-')
        output_filename = f"generate_country_csv_report_{label}_{safe_timestamp}.csv"
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if header:
                writer.writerow(header)
            writer.writerows(extracted_data)

        print(f"Success: Generated {output_filename} in {output_dir}")


if __name__ == "__main__":
    home = os.path.expanduser("~")

    # game.log is written by the game into the Documents logs folder; that's the
    # real input location and does not move with this script.
    LOG_FILE_PATH = os.path.join(home, "Documents", "Paradox Interactive", "Hearts of Iron IV", "logs", "game.log")
    # Write the generated CSVs next to this script (tools/Generated CSV/) rather
    # than into Documents, so they land inside the mod's working tree.
    OUTPUT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

    generate_country_reports(LOG_FILE_PATH, OUTPUT_DIRECTORY)
