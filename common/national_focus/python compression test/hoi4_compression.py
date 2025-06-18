import re

input_file = "HHE.national_branches.txt"
output_file = "HHE.national_branches_compressed.txt"

# python hoi4_compression.py

try:
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Remove comments (# to end of line)
    no_comments = [re.sub(r"#.*", "", line) for line in lines]

    # Join all lines into one string separated by spaces
    joined = " ".join(no_comments)

    # Replace tabs and newlines already removed by join, but ensure no weird whitespace remains
    # Collapse multiple whitespace into single space
    compressed = re.sub(r"\s+", " ", joined).strip()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(compressed)

    print(f"Compressed output written to: {output_file}")

except Exception as e:
    print(f"Error during compression: {e}")

input("\nDone. Press Enter to exit...")
