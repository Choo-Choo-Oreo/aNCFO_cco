import sys
import os

# Check if a file name was provided as an argument
if len(sys.argv) < 2:
    print("Usage: python pdx_file_decompression.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Derive output file name by appending '_compressed' before the extension
base, ext = os.path.splitext(input_file)
output_file = f"{base}_restored{ext}"

try:
    with open(input_file, "r", encoding="utf-8") as f:
        compressed = f.read()

    indent_level = 0
    indent_str = "    "  # 4 spaces
    result_lines = []
    i = 0
    length = len(compressed)
    token = ""
    current_line = ""

    while i < length:
        c = compressed[i]

        if c in ['=', '<', '>']:
            # Finish current token, add operator with space
            token = token.strip()
            if token:
                current_line += token + f" {c} "
            token = ""
            i += 1

        elif c == '{':
            token = token.strip()
            if token:
                current_line += token
                token = ""
            if current_line.strip():
                # Append ' {' to the current line, no new line for brace
                result_lines.append(indent_str * indent_level + current_line.strip() + " {")
            else:
                # No current text, just a brace on its own line
                result_lines.append(indent_str * indent_level + "{")
            current_line = ""
            indent_level += 1
            i += 1

        elif c == '}':
            token = token.strip()
            if token:
                current_line += token
                token = ""
            if current_line.strip():
                result_lines.append(indent_str * indent_level + current_line.strip())
            current_line = ""
            indent_level -= 1
            result_lines.append(indent_str * indent_level + "}")
            i += 1

        elif c == ' ':
            if current_line.strip().endswith(('=', '<', '>')) and token.strip():
                current_line += token.strip()
                token = ""
                result_lines.append(indent_str * indent_level + current_line.strip())
                current_line = ""
            else:
                if token.strip():
                    current_line += token.strip() + " "
                    token = ""
            i += 1

        else:
            token += c
            i += 1

    # Flush any remaining token
    if token.strip():
        current_line += token.strip()
    if current_line.strip():
        result_lines.append(indent_str * indent_level + current_line.strip())

    # Write to output
    with open(output_file, "w", encoding="utf-8") as f:
        f.write('\n'.join(result_lines))

    print(f"Restored pretty text written to: {output_file}")

except Exception as e:
    print("Error:", e)

input("\nDone. Press Enter to exit...")
