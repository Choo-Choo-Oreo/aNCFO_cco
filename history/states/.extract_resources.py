import os
import re
import csv

def parse_state_file(filepath):
    # Default all tracked resources to 0
    resources = {
        'oil': 0,
        'aluminium': 0,
        'rubber': 0,
        'tungsten': 0,
        'steel': 0,
        'chromium': 0,
        'coal': 0
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if this is an actual state file
        if not re.search(r'\bstate\s*=\s*\{', content):
            return None
            
        # Step 1: Strip out any comments starting with '#' to avoid parsing old values
        content_clean = re.sub(r'#.*', '', content)
        
        # Step 2: Extract the entire resources block context
        # re.DOTALL allows the '.' to match newlines
        resource_block_match = re.search(r'resources\s*=\s*\{([^}]+)\}', content_clean, re.DOTALL)
        
        if resource_block_match:
            resource_block_content = resource_block_match.group(1)
            
            # Step 3: Find all resource pairs (e.g., oil=320 or aluminium = 50)
            # \w+ matches the resource name, \s* handles any spaces, \d+ matches the amount
            pairs = re.findall(r'(\w+)\s*=\s*(\d+)', resource_block_content)
            
            for res_name, res_val in pairs:
                # If the parsed resource is one of the ones we care about, record it
                if res_name in resources:
                    resources[res_name] = int(res_val)
                    
        return resources
    except Exception as e:
        print(f"Skipping {filepath} due to an error: {e}")
        return None

def main():
    # Define the exact columns requested
    headers = ['filename', 'oil', 'aluminium', 'rubber', 'tungsten', 'steel', 'chromium', 'coal']
    output_file = '.state_resources.csv'
    rows = []

    # Scan the current root folder
    for filename in os.listdir('.'):
        if filename.endswith('.txt'):
            filepath = os.path.join('.', filename)
            
            res_data = parse_state_file(filepath)
            if res_data is not None:
                # Prepare the row with the filename included
                row = {'filename': filename}
                row.update(res_data)
                rows.append(row)
                
    # Write the collected data to a CSV using a semicolon ';' delimiter
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter=';')
        writer.writeheader()
        writer.writerows(rows)

    print(f"Processing complete! Saved data for {len(rows)} states to '{output_file}'.")

if __name__ == '__main__':
    main()
