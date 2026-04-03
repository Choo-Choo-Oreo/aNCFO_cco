import os
import re
import csv

def generate_country_reports(log_file_path, output_dir):
    # regex supports alphanumeric tags (e.g., D01) and game timestamps
    log_pattern = re.compile(r'\[.*?\]\[(?P<date>\d{4}\.\d{2}\.\d{2}\.\d{2})\]\[.*?\]:\s*(?P<csv_data>[A-Z0-9]{3},.*)')
    raw_csv_pattern = re.compile(r'^([A-Z0-9]{3}(?:,-?\d+(?:\.\d+)?%?)+)')

    reports_data = {}
    current_timestamp = "Unknown"
    current_header = []

    if not os.path.exists(log_file_path):
        print(f"Error: Could not find the log file at {log_file_path}")
        return

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip()

            if "Country_Tag" in line:
                header_match = re.search(r'Country_Tag.*', line)
                if header_match:
                    current_header = header_match.group(0).split(',')
                continue

            match = log_pattern.search(line)
            if match:
                current_timestamp = match.group('date')
                
                if current_timestamp not in reports_data:
                    reports_data[current_timestamp] = {
                        'header': current_header.copy(),
                        'rows': []
                    }

                csv_string = match.group('csv_data')
                data_row = csv_string.split(',')

                if current_header and len(data_row) == len(current_header):
                    reports_data[current_timestamp]['rows'].append(data_row)
                continue

            raw_match = raw_csv_pattern.search(line)
            if raw_match:
                data_row = raw_match.group(1).split(',')
                if current_header and len(data_row) == len(current_header):
                    if current_timestamp not in reports_data:
                        reports_data[current_timestamp] = {
                            'header': current_header.copy(),
                            'rows': []
                        }
                    reports_data[current_timestamp]['rows'].append(data_row)

    if not reports_data:
        print("No valid country data matching the header structure was found in the log.")
        return

    for timestamp, data in reports_data.items():
        extracted_data = data['rows']
        header = data['header']
        
        if not extracted_data:
            continue
            
        safe_timestamp = timestamp.replace('.', '-')
        output_filename = f"generate_country_csv_report_{safe_timestamp}.csv"
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if header:
                writer.writerow(header)
            writer.writerows(extracted_data)

        print(f"Success: Generated {output_filename} in {output_dir}")

if __name__ == "__main__":
    home = os.path.expanduser("~")

    LOG_FILE_PATH = os.path.join(home, "Documents", "Paradox Interactive", "Hearts of Iron IV", "logs", "game.log")
    OUTPUT_DIRECTORY = os.path.join(home, "Documents", "Paradox Interactive", "Hearts of Iron IV", "mod", "aNCFO_cco", "documentation", "Generated CSV")

    generate_country_reports(LOG_FILE_PATH, OUTPUT_DIRECTORY)
