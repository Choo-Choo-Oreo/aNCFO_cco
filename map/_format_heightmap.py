from PIL import Image
import struct

# Overrides
input_path = "heightmap.bmp"
output_path = "heightmap.bmp"

# Load image and force 8-bit grayscale
img = Image.open(input_path).convert("L")

# Export as a 8-bit BMP
img.save (
    output_path,
    format = "BMP",
    bits = 8
)

output_path
