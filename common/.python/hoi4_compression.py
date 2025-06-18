import re
import sys
import os

# Check if a file name was provided as an argument
if len(sys.argv) < 2:
    print("Usage: python hoi4_compression.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Derive output file name by appending '_compressed' before the extension
base, ext = os.path.splitext(input_file)
output_file = f"{base}_compressed{ext}"

# python hoi4_compression.py input_file

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

    # Remove spaces around =, {, }, <, >
    compressed = re.sub(r"\s*([=\{\}<>])\s*", r"\1", compressed)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(compressed)

    print(f"Compressed output written to: {output_file}")

except Exception as e:
    print(f"Error during compression: {e}")

input("\nDone. Press Enter to exit...")
