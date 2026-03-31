import os

# 1. Define the directory path
countries_dir = os.path.join("history", "countries")

# 2. Hardcode the specific strings you want removed
invalid_ideas = [
    "species_idea_human",
    "species_idea_elf",
    "species_idea_dwarf",
    "species_supremacy_law",
    "culture_supremacy_law",
    "species_adjacent_law",
    "culture_adjacent_law"
]

print("Scanning files to remove invalid ideas...")

# Check if the directory exists
if not os.path.exists(countries_dir):
    print(f"Error: Could not find the directory '{countries_dir}'.")
    print("Make sure this python script is in the same folder that CONTAINS the 'history' folder.")
    exit()

files_modified = 0

# 3. Process the country files
for filename in os.listdir(countries_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(countries_dir, filename)
        
        # Read the file
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()
        
        new_lines = []
        modified = False
        
        # Check each line against our list of bad ideas
        for line in lines:
            # If the line contains any of the invalid ideas, we skip it (deleting the whole line)
            if any(bad_idea in line for bad_idea in invalid_ideas):
                modified = True
                continue 
            
            # Otherwise, keep the line
            new_lines.append(line)
        
        # If we caught and removed anything, overwrite the file with the clean lines
        if modified:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(new_lines)
            print(f"Cleaned: {filename}")
            files_modified += 1

print(f"\nDone! Cleaned up {files_modified} files by completely removing the specified lines.")