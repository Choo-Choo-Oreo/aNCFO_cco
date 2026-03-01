import os

def generate_dynamic_map():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_folder_name = os.path.basename(current_dir)
    
    output_filename = "_found_tree.txt"
    script_filename = os.path.basename(__file__)
    
    file_count = 0
    dir_count = 0
    
    with open(output_filename, "w", encoding="utf-8") as output_file:
        output_file.write(f"Structure for: {parent_folder_name}\n\n")
        
        for root, dirs, files in os.walk(current_dir):
            relative_path = os.path.relpath(root, current_dir)
            
            if relative_path == ".":
                level = 0
                display_name = parent_folder_name
            else:
                level = relative_path.count(os.sep) + 1
                display_name = os.path.basename(root)
            
            indent = ' ' * 4 * level
            output_file.write(f"{indent}[{display_name}/]\n")
            
            sub_indent = ' ' * 4 * (level + 1)
            
            for file in files:
                # Ignore the script itself and the output text file
                if file == script_filename or file == output_filename:
                    continue
                
                output_file.write(f"{sub_indent}{file}\n")
                file_count += 1
            
            dir_count += len(dirs)

        output_file.write("\n" + "="*30 + "\n")
        output_file.write(f"Total Folders: {dir_count}\n")
        output_file.write(f"Total Files:   {file_count}\n")
        output_file.write("="*30 + "\n")

if __name__ == "__main__":
    generate_dynamic_map()