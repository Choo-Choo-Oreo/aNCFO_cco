import os
import re

class PeekableIterator:
    """An iterator that allows looking ahead one token without consuming it."""
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self._peek = []
        
    def __next__(self):
        if self._peek:
            return self._peek.pop(0)
        return next(self.iterator)
        
    def peek(self):
        if not self._peek:
            try:
                self._peek.append(next(self.iterator))
            except StopIteration:
                return None
        return self._peek[0]

def tokenize(text):
    """Removes comments and extracts Clausewitz syntax tokens."""
    text = re.sub(re.compile(r"#.*?\n"), "\n", text)
    
    token_specification = [
        ('STRING',  r'"[^"\\]*(?:\\.[^"\\]*)*"'), 
        ('ASSIGN',  r'='),
        ('LBRACE',  r'\{'),
        ('RBRACE',  r'\}'),
        ('WORD',    r'[^\s={}\n#]+'),             
    ]
    tok_regex = '|'.join(f'(?P<{name}>{reg})' for name, reg in token_specification)
    for mo in re.finditer(tok_regex, text):
        kind = mo.lastgroup
        value = mo.group()
        yield kind, value

def parse_elements(tokens):
    """Parses tokens recursively into a structured AST tree of nodes."""
    elements = []
    while True:
        tok = tokens.peek()
        if tok is None:
            break
        kind, val = tok
        if kind == 'RBRACE':
            next(tokens) 
            break
        next(tokens)     
        
        next_tok = tokens.peek()
        if next_tok and next_tok[0] == 'ASSIGN':
            next(tokens) 
            val_tok = tokens.peek()
            if val_tok and val_tok[0] == 'LBRACE':
                next(tokens) 
                sub_elements = parse_elements(tokens)
                elements.append(('pair', val, sub_elements))
            else:
                v_kind, v_val = next(tokens)
                elements.append(('pair', val, v_val))
        else:
            elements.append(('value', val))
    return elements

def format_generic_element(el, indent, spaces=True):
    """Recursively formats elements not caught by specialized rules."""
    if el[0] == 'value':
        return el[1]
    elif el[0] == 'pair':
        key, val = el[1], el[2]
        eq = " = " if spaces else "="
        if isinstance(val, list):
            ind = "\t" * indent
            sub_ind = "\t" * (indent + 1)
            sub_lines = []
            for sub_el in val:
                sub_lines.append(f"{sub_ind}{format_generic_element(sub_el, indent + 1, spaces=spaces)}\n")
            return f"{key}{eq}{{\n" + "".join(sub_lines) + ind + "}"
        else:
            return f"{key}{eq}{val}"

def format_resources(elements, indent):
    """Formats natural resource distribution matching template sequence."""
    res_order = ['oil', 'coal', 'aluminium', 'rubber', 'tungsten', 'steel', 'chromium']
    pairs = {el[1]: el for el in elements if el[0] == 'pair'}
    ind = "\t" * indent
    lines = []
    for r in res_order:
        if r in pairs:
            lines.append(f"{ind}{r}={pairs[r][2]}\n")
    for r, el in pairs.items():
        if r not in res_order:
            lines.append(f"{ind}{r}={el[2]}\n")
    return "{\n" + "".join(lines) + "\t" * (indent - 1) + "}"

def format_provinces(elements, indent):
    """Formats linear province lists on a single clean array line."""
    vals = [el[1] for el in elements if el[0] == 'value']
    if all(v.isdigit() for v in vals):
        vals.sort(key=int)
    return "{\n" + "\t" * indent + " ".join(vals) + "\n" + "\t" * (indent - 1) + "}"

def format_buildings(elements, indent):
    """Dynamic parser that groups buildings matching the template criteria."""
    ind = "\t" * indent
    lines = []
    
    infra_pairs = [el for el in elements if el[0] == 'pair' and el[1] == 'infrastructure']
    for el in infra_pairs:
        lines.append(f"{ind}infrastructure = {el[2]}\n")
    
    prov_pairs = [el for el in elements if el[0] == 'pair' and el[1].isdigit()]
    prov_pairs.sort(key=lambda x: int(x[1]))
    for el in prov_pairs:
        sub_ind = "\t" * (indent + 1)
        sub_lines = []
        if isinstance(el[2], list):
            for sub_el in el[2]:
                sub_lines.append(f"{sub_ind}{format_generic_element(sub_el, indent + 1, spaces=True)}\n")
            sub_str = "{\n" + "".join(sub_lines) + ind + "}"
        else:
            sub_str = el[2]
        lines.append(f"{ind}{el[1]} = {sub_str}\n")
        
    state_bld_pairs = [el for el in elements if el[0] == 'pair' and el[1] != 'infrastructure' and not el[1].isdigit()]
    for el in state_bld_pairs:
        lines.append(f"{ind}{format_generic_element(el, indent, spaces=True)}\n")
        
    return "{\n" + "".join(lines) + "\t" * (indent - 1) + "}"

def format_history_element(el, indent):
    """Specialized historical assignments formatting handler."""
    key, val = el[1], el[2]
    if key == 'victory_points':
        if isinstance(val, list):
            vals_str = " ".join(v[1] for v in val if v[0] == 'value')
            return f"victory_points = {{ {vals_str} }}"
        return f"victory_points = {val}"
    elif key == 'buildings':
        if isinstance(val, list):
            return f"buildings = {format_buildings(val, indent + 1)}"
        return f"buildings = {val}"
    else:
        return format_generic_element(el, indent, spaces=True)

def format_history(elements, indent):
    """Formats core state metrics timeline hierarchy."""
    hist_order = ['owner', 'add_core_of', 'add_claim_by', 'victory_points', 'buildings', 'add_extra_state_shared_building_slots']
    pairs_by_key = {}
    other_elements = []
    for el in elements:
        if el[0] == 'pair':
            pairs_by_key.setdefault(el[1], []).append(el)
        else:
            other_elements.append(el)
    
    ind = "\t" * indent
    lines = []
    
    for k in hist_order:
        if k in pairs_by_key:
            for el in pairs_by_key[k]:
                lines.append(f"{ind}{format_history_element(el, indent)}\n")
            del pairs_by_key[k]
    
    for k, els in pairs_by_key.items():
        for el in els:
            lines.append(f"{ind}{format_history_element(el, indent)}\n")
            
    for el in other_elements:
        lines.append(f"{ind}{format_generic_element(el, indent, spaces=True)}\n")
        
    return "{\n" + "".join(lines) + "\t" * (indent - 1) + "}"

def format_state_element(el, indent=1):
    """Applies strict formatting rules directly mapped out by standard template."""
    key, val = el[1], el[2]
    ind = "\t" * indent
    if key == 'id':
        return f"{ind}id={val}\n"
    elif key == 'name':
        return f"{ind}name={val}\n"
    elif key == 'resources':
        if isinstance(val, list):
            return f"{ind}resources={format_resources(val, indent + 1)}\n"
        return f"{ind}resources={val}\n"
    elif key == 'history':
        if isinstance(val, list):
            return f"{ind}history={format_history(val, indent + 1)}\n"
        return f"{ind}history={val}\n"
    elif key == 'provinces':
        if isinstance(val, list):
            return f"{ind}provinces={format_provinces(val, indent + 1)}\n"
        return f"{ind}provinces={val}\n"
    elif key == 'manpower':
        return f"{ind}manpower={val}\n"
    elif key == 'buildings_max_level_factor':
        return f"{ind}buildings_max_level_factor={val}\n"
    elif key == 'state_category':
        return f"{ind}state_category={val}\n"
    elif key == 'impassable':
        return f"{ind}impassable={val}\n"
    elif key == 'local_supplies':
        return f"{ind}local_supplies={val}\n"
    else:
        # FIX: Corrected fallback prevents duplicating unmapped keywords like force_link_ownership_to
        if isinstance(val, list):
            sub_lines = []
            for sub_el in val:
                sub_lines.append(f"\t" * (indent + 1) + format_generic_element(sub_el, indent + 1, spaces=True) + "\n")
            return f"{ind}{key} = {{\n" + "".join(sub_lines) + ind + "}\n"
        else:
            return f"{ind}{key} = {val}\n"

def format_state_block(state_el):
    """Assembles all finalized fields inside the root state container block."""
    elements = state_el[2]
    ordered_keys = [
        'id', 'name', 'resources', 'history', 'provinces', 
        'manpower', 'buildings_max_level_factor', 'state_category', 
        'impassable', 'local_supplies'
    ]
    
    pairs_by_key = {}
    for el in elements:
        if el[0] == 'pair':
            pairs_by_key.setdefault(el[1], []).append(el)
    
    lines = []
    for k in ordered_keys:
        if k in pairs_by_key:
            for el in pairs_by_key[k]:
                lines.append(format_state_element(el, 1))
            del pairs_by_key[k]
            
    for k, els in pairs_by_key.items():
        for el in els:
            lines.append(format_state_element(el, 1))
            
    return "state={\n" + "".join(lines) + "}\n"

def format_hoi4_state_file(text):
    """Main execution block formatting pipeline handler."""
    tokens = PeekableIterator(tokenize(text))
    elements = parse_elements(tokens)
    state_blocks = [el for el in elements if el[0] == 'pair' and el[1] == 'state']
    if not state_blocks:
        return "# Error: No standard root 'state' block discovered inside file.\n"
    return format_state_block(state_blocks[0])

def fix_filename_casing(directory_path):
    """
    Scans the directory for files that cause HOI4 State ID conflicts due to 
    case-mismatches with the base game, forcing them to base game standard.
    """
    # Exact map of conflicted filenames derived from your error log vs vanilla
    expected_casing = {
        "301-paraguay.txt": "301-paraguay.txt",
        "624-central islands.txt": "624-Central islands.txt",
        "83-crisana.txt": "83-crisana.txt",
        "844-jubaland.txt": "844-jubaland.txt",
        "862-ouest du quebec.txt": "862-ouest du quebec.txt"
    }
    
    renamed_count = 0
    for current_file in os.listdir(directory_path):
        lower_name = current_file.lower()
        if lower_name in expected_casing:
            correct_name = expected_casing[lower_name]
            if current_file != correct_name:
                old_path = os.path.join(directory_path, current_file)
                temp_path = os.path.join(directory_path, "TEMP_" + current_file)
                new_path = os.path.join(directory_path, correct_name)
                
                # Safely rename via temp file to avoid Windows case-insensitive filesystem collisions
                os.rename(old_path, temp_path)
                os.rename(temp_path, new_path)
                print(f"Fixed File Casing Conflict: '{current_file}' -> '{correct_name}'")
                renamed_count += 1
    if renamed_count > 0:
        print(f"Successfully synchronized {renamed_count} files with vanilla HOI4 case rules.\n")

def process_files_in_directory(directory_path="."):
    """Dynamically parses and cleans up all state files in the target directory."""
    if not os.path.isdir(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        return

    # Automatically resolve case conflicts before scanning
    fix_filename_casing(directory_path)

    all_files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]
    exclude_files = ["State Template.txt", "Wiki_StateModding.txt"]
    target_files = [f for f in all_files if f not in exclude_files]
    
    total_files = len(target_files)
    print(f"Found {total_files} files to process in '{directory_path}'...")
    
    success_count = 0
    error_count = 0

    for index, filename in enumerate(target_files, start=1):
        file_path = os.path.join(directory_path, filename)
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                content = f.read()
                
            if "state" not in content.lower():
                continue

            formatted_content = format_hoi4_state_file(content)
            
            if formatted_content.startswith("# Error"):
                print(f"[{index}/{total_files}] Skipped '{filename}': No root state block found.")
                error_count += 1
                continue
                
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
            
            success_count += 1
            
            if success_count % 100 == 0:
                print(f"Progress: Cleaned & Standardized {success_count}/{total_files} files...")

        except Exception as e:
            print(f"Error processing '{filename}' at item {index}: {e}")
            error_count += 1

    print(f"\n==========================================")
    print(f"Processing Complete!")
    print(f"Successfully formatted: {success_count} files.")
    print(f"Skipped or Errors:     {error_count} files.")
    print(f"==========================================")

if __name__ == "__main__":
    process_files_in_directory(".")
