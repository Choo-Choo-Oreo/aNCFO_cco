import os
import csv
from PIL import Image

# Directory setup relative to the script's location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HIGHRES_DIR = os.path.join(SCRIPT_DIR, "highres")
# The leaders directory is one level up from .tools.art
LEADERS_DIR = os.path.dirname(SCRIPT_DIR)

# Resolution definitions
RES_MAP = {
    'A': (156, 210),
    'B': (312, 420)
}

def process_portraits():
    csv_file = os.path.join(SCRIPT_DIR, "portraits.csv")
    
    if not os.path.exists(csv_file):
        print(f"CSV file not found at: {csv_file}")
        return

    with open(csv_file, mode='r', encoding='utf-8') as f:
        # Read the CSV with semicolon delimiter
        reader = csv.DictReader(f, delimiter=';')
        
        for row in reader:
            # Extract and strip whitespace
            highres_file = row['highres_file'].strip()
            background_file = row['background_file'].strip()
            output_name = row['output_name'].strip()
            output_tag = row['output_tag'].strip()
            output_res = row['output_res'].strip()
            
            if output_res not in RES_MAP:
                print(f"Skipping {output_name}: Invalid resolution identifier '{output_res}'.")
                continue
            
            target_size = RES_MAP[output_res]
            
            bg_path = os.path.join(SCRIPT_DIR, background_file)
            fg_path = os.path.join(HIGHRES_DIR, highres_file)
            
            try:
                # Load images and ensure they have an alpha channel for compositing
                bg = Image.open(bg_path).convert("RGBA")
                fg = Image.open(fg_path).convert("RGBA")
                
                # Resize both images to the target dimensions before compositing
                bg = bg.resize(target_size, Image.Resampling.LANCZOS)
                fg = fg.resize(target_size, Image.Resampling.LANCZOS)
                
                # Composite the highres image over the background
                composite = Image.alpha_composite(bg, fg)
                
                # Create the target tag directory if it does not exist
                out_dir = os.path.join(LEADERS_DIR, output_tag)
                os.makedirs(out_dir, exist_ok=True)
                
                # Save the final image as DDS
                out_path = os.path.join(out_dir, f"{output_name}.dds")
                composite.save(out_path, format="DDS")
                
                print(f"Successfully generated: {out_path}")
                
            except Exception as e:
                print(f"Error processing {output_name}: {e}")

if __name__ == "__main__":
    process_portraits()
