import re

# File paths (adjust if needed)
dominant_file = "generic.FAI_defines.lua"
subordinate_file = "aNCFO_defines.lua"
output_file = "aNCFO_defines_cleaned.lua"

# Regex to find the "NDefines.X.Y" part of a line
key_pattern = re.compile(r'(NDefines\.[a-zA-Z0-9._]+)')

# 1. Get all keys from the dominant (AI) file
dominant_keys = set()

# Added encoding='utf-8' here
with open(dominant_file, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        match = key_pattern.search(line)
        if match:
            dominant_keys.add(match.group(1))

# 2. Filter the aNCFO file
cleaned_lines = []

# Added encoding='utf-8' here as well
with open(subordinate_file, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        match = key_pattern.search(line)
        # If the key is in our dominant list, we skip it
        if match and match.group(1) in dominant_keys:
            continue 
        cleaned_lines.append(line)

# 3. Write the cleaned version
with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(cleaned_lines)

print(f"Duplicates removed. Cleaned file saved as {output_file}")