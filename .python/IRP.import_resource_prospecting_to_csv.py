# Improved Resource Prospecting - reconstruct the CSV from the generated decisions txt
import csv
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DECISIONS_DIR = os.path.join(SCRIPT_DIR, '..', 'common', 'decisions')

BLOCK_RE = re.compile(r'\n\t(\S+) = \{ # (\w+)\n(.*?)\n\t\}\n', re.DOTALL)
STATE_RE = re.compile(r'state = (\d+)')
FLAG_RE = re.compile(r'set_state_flag = state_(\d+)_(\w+)_developed_(\d+)')
AMOUNT_RE = re.compile(r'add_resource = \{ type = \w+ amount = (\d+) \}')
TECH_RE = re.compile(r'available = \{.*?has_tech = (\S+)', re.DOTALL)

def import_decisions():
    input_file = os.path.join(DECISIONS_DIR, 'IRP.resource_prospecting.txt')
    csv_file = os.path.join(SCRIPT_DIR, 'IRP.resource_prospecting.csv')

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    rows = []
    groups = {}
    for dec_id, _res_label, body in BLOCK_RE.findall(text):
        state_match = STATE_RE.search(body)
        flag_match = FLAG_RE.search(body)
        amount_match = AMOUNT_RE.search(body)
        tech_match = TECH_RE.search(body)

        state_id = state_match.group(1)
        res_type = flag_match.group(2)
        tier = int(flag_match.group(3))
        amount = amount_match.group(1)
        tech = tech_match.group(1)

        row = {
            'State_ID': state_id,
            'Resource_Type': res_type,
            'Resource_Amount': amount,
            'Required_Tech': tech,
            'Decision_ID': dec_id,
            'Required_Decision_ID': '',
        }
        rows.append(row)
        groups.setdefault((state_id, res_type), {})[tier] = row

    for group in groups.values():
        for tier, row in group.items():
            if tier > 1 and (tier - 1) in group:
                row['Required_Decision_ID'] = group[tier - 1]['Decision_ID']

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['State_ID', 'Resource_Type', 'Resource_Amount', 'Required_Tech', 'Decision_ID', 'Required_Decision_ID'])
        writer.writeheader()
        writer.writerows(rows)

    print(f"File {csv_file} generated successfully.")

if __name__ == "__main__":
    import_decisions()
