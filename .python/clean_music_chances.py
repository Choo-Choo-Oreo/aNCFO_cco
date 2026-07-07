import os
import re
import glob

def fix_and_clean_music_files():
    music_dir = os.path.join("..", "music")
    
    # Fallback to local directory if needed
    if not os.path.exists(music_dir):
        music_dir = "music"
        
    if not os.path.exists(music_dir):
        print("[-] Could not find the 'music' folder.")
        return

    txt_files = glob.glob(os.path.join(music_dir, "*.txt"))
    if not txt_files:
        print("[-] No .txt files found.")
        return

    modified_count = 0

    for file_path in txt_files:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if "chance" not in content:
            continue

        output = []
        pos = 0
        length = len(content)
        file_changed = False

        while pos < length:
            # Capture the indentation spacing right before 'chance'
            match = re.search(r'([ \t]*)chance\s*=\s*\{', content[pos:])
            if not match:
                output.append(content[pos:])
                break

            # Calculate absolute string indices to prevent slicing errors
            chance_start_idx = pos + match.start()
            brace_start_idx = pos + match.end() # Index immediately AFTER the '{'
            
            indent = match.group(1) if match.group(1) else "\t\t"

            # Append everything perfectly up to the start of this block
            output.append(content[pos:chance_start_idx])

            brace_count = 1
            scan_idx = brace_start_idx
            in_comment = False
            in_string = False

            # Bulletproof character scanner
            while scan_idx < length and brace_count > 0:
                char = content[scan_idx]

                if in_comment:
                    if char == '\n':
                        in_comment = False
                elif in_string:
                    if char == '"' and content[scan_idx-1] != '\\':
                        in_string = False
                else:
                    if char == '#':
                        in_comment = True
                    elif char == '"':
                        in_string = True
                    elif char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                
                scan_idx += 1

            # Extract the raw inner text of the entire swallowed block
            inner_text = content[brace_start_idx:scan_idx-1]
            
            # Strip out comments temporarily to check for a flat 'factor = 0'
            clean_text = "\n".join([line.split('#')[0] for line in inner_text.splitlines()])
            
            # Smart Check: preserve factor = 0 for event-only speeches
            if re.search(r'\bfactor\s*=\s*0(?!\.\d)', clean_text):
                factor_val = "0"
            else:
                factor_val = "1"

            # Rebuild the pristine, modifier-free block
            replacement = f"{indent}chance = {{\n{indent}\tfactor = {factor_val}\n{indent}}}"
            output.append(replacement)

            pos = scan_idx
            file_changed = True

        if file_changed:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("".join(output))
            print(f"[+] Formatted perfectly: {os.path.basename(file_path)}")
            modified_count += 1

    print(f"\n[+] Script execution complete. Safely processed {modified_count} files.")

if __name__ == "__main__":
    print("=== Running Bulletproof Soundtrack Optimizer ===")
    fix_and_clean_music_files()
