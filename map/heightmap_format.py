from PIL import Image
import struct

# Paths
input_path = "heightmap.bmp"
output_path = "heightmap.bmp"

# Load image and force 8-bit grayscale
img = Image.open(input_path).convert("L")

# Re-save with explicit 256-color palette BMP
img.save(
    output_path,
    format="BMP",
    bits=8
)

output_path
