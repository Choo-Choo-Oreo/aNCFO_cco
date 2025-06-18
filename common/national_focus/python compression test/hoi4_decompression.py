input_file = "HHE.national_branches_compressed.txt"
output_file = "HHE.national_branches_restored.txt"

# python hoi4_decompression.py

try:
    with open(input_file, "r", encoding="utf-8") as f:
        compressed = f.read()

    indent_level = 0
    indent_str = "    "  # 4 spaces per indent
    result_lines = []
    buffer = ""
    i = 0
    length = len(compressed)

    while i < length:
        c = compressed[i]

        if c == '{':
            # Write buffer trimmed as a line, if any
            if buffer.strip():
                result_lines.append(indent_str * indent_level + buffer.strip())
            buffer = ""
            # Write '{' on its own line, indent then increase indent
            result_lines.append(indent_str * indent_level + '{')
            indent_level += 1
            i += 1

        elif c == '}':
            # Flush buffer if any
            if buffer.strip():
                result_lines.append(indent_str * indent_level + buffer.strip())
            buffer = ""
            indent_level -= 1
            # Write '}' on its own line
            result_lines.append(indent_str * indent_level + '}')
            i += 1

        elif c == '=':
            # Append equal sign with spaces around it (for readability)
            buffer += ' = '
            i += 1
        elif c == ' ':
            # Append a single space to buffer (condense multiple spaces)
            if buffer and buffer[-1] != ' ':
                buffer += ' '
            i += 1
        else:
            buffer += c
            i += 1

    # Flush remaining buffer
    if buffer.strip():
        result_lines.append(indent_str * indent_level + buffer.strip())

    # Join lines with newlines
    pretty_text = '\n'.join(result_lines)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(pretty_text)

    print(f"Restored pretty text written to: {output_file}")

except Exception as e:
    print("Error:", e)

input("\nDone. Press Enter to exit...")
