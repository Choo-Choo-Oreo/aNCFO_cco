"""
format_terrain.py

Correctly saves terrain.bmp for Hearts of Iron IV.

The game requires ALL of the following, which PIL alone does not guarantee:
  - BITMAPINFOHEADER (40-byte DIB header, not BITMAPV4/V5HEADER)
  - 8-bit indexed (palette mode), never 24-bit RGB
  - No compression (BI_RGB = 0)
  - Palette order preserved exactly (the game reads index IDs, not RGB colours)

Usage:
  Run directly from your map directory:
      python _format_terrain.py
"""

import os
import sys
import io
import stat
import time
import struct
from PIL import Image

# --- Configuration ---
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH  = os.path.join(SCRIPT_DIR, "terrain.bmp")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "terrain.bmp")

TERRAIN_PALETTE = {
     0: ( 86, 124,  27),   # plains
     1: (  0,  86,   6),   # forest (dense)
     2: (112,  74,  31),   # hills
     3: (206, 169,  99),   # desert
     4: (  6, 200,  11),   # forest (sparse)
     5: (255,   0,  24),   # plains / farmland
     6: (134,  84,  30),   # mountain
     7: (252, 255,   0),   # desert
     8: ( 73,  59,  15),   # desert
     9: ( 75, 147, 174),   # marsh
    10: (174,   0, 255),   # mountain
    11: ( 92,  83,  76),   # mountain
    12: (255,   0, 240),   # desert
    13: (240, 255,   0),   # urban
    14: ( 55,  90, 220),   # lakes (unused graphically)
    15: (  8,  31, 130),   # ocean
    16: (255, 255, 255),   # mountain / permanent snow
    17: (132, 255,   0),   # hills
    18: (255, 126,   0),   # mountain (unused in base game)
    19: (114, 137, 105),   # plains / permanent snow
    20: ( 58, 131,  82),   # mountain
    21: (255,   0, 127),   # jungle
    22: (  0,  82,  82),   # jungle (unused in base game)
    27: (243, 199, 147),   # mountain
    31: ( 27,  27,  27),   # mountain (unused in base game)
}


# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------

def _parse_raw_color_table(file_bytes):
    """Parses color table directly from memory array."""
    dib_size     = struct.unpack_from("<I", file_bytes, 14)[0]
    bpp          = struct.unpack_from("<H", file_bytes, 28)[0]
    pixel_offset = struct.unpack_from("<I", file_bytes, 10)[0]

    if bpp != 8:
        raise ValueError(
            f"Cannot read raw color table: input BMP is {bpp}-bit, not 8-bit."
        )

    ct_start = 14 + dib_size
    ct_size  = pixel_offset - ct_start
    return file_bytes[ct_start : ct_start + ct_size]


def _build_color_table_from_palette_dict(palette_dict, num_entries=255):
    ct = bytearray()
    for i in range(num_entries):
        r, g, b = palette_dict.get(i, (i, i, i))
        ct.extend([b, g, r, 0])
    return bytes(ct)


def _build_pixel_rows(pixel_bytes, width, height):
    row_stride = width
    row_padded = (row_stride + 3) & ~3
    padding    = row_padded - row_stride

    rows = bytearray()
    for y in range(height - 1, -1, -1):
        row = pixel_bytes[y * row_stride : y * row_stride + row_stride]
        rows.extend(row)
        rows.extend(b"\x00" * padding)
    return bytes(rows)


def _write_bitmapinfoheader_bmp(
    output_path,
    width, height,
    color_table,
    pixel_rows,
    colors_used=255,
    colors_important=255,
):
    BITMAPFILEHEADER_SIZE = 14
    BITMAPINFOHEADER_SIZE = 40
    pixel_offset = BITMAPFILEHEADER_SIZE + BITMAPINFOHEADER_SIZE + len(color_table)
    file_size    = pixel_offset + len(pixel_rows)

    file_header = struct.pack(
        "<2sIHHI",
        b"BM",
        file_size,
        0,
        0,
        pixel_offset,
    )

    row_padded = (width + 3) & ~3
    image_size = row_padded * height

    dib_header = struct.pack(
        "<IiiHHIIiiII",
        BITMAPINFOHEADER_SIZE,
        width,
        height,
        1,
        8,
        0,
        image_size,
        2834,
        2834,
        colors_used,
        colors_important,
    )

    if os.path.exists(output_path):
        try:
            os.chmod(output_path, stat.S_IWRITE)
        except Exception:
            pass

    # Problem Solving: Retry loop with delay to wait out OS file-locking filters
    max_retries = 5
    for attempt in range(max_retries):
        try:
            with open(output_path, "wb") as f:
                f.write(file_header)
                f.write(dib_header)
                f.write(color_table)
                f.write(pixel_rows)
            break  # Success
        except OSError as e:
            if attempt < max_retries - 1:
                print(f"Write blocked by Windows system filters (Attempt {attempt + 1}/{max_retries}). Retrying in 0.5s...")
                time.sleep(0.5)
            else:
                print("\n" + "!"*60)
                print(f"CRITICAL ERROR: Windows persistently blocked writing to: {output_path}")
                print(f"Error Details: {e}")
                print("-" * 60)
                print("EXTERNAL CONFLICT RESOLUTION REQUIRED:")
                print("The file is locked outside of Python. Please ensure:")
                print("1. Hearts of Iron IV and the Nudge tool are completely CLOSED.")
                print("2. Photoshop, GIMP, Paint.NET, or your image tool is completely CLOSED.")
                print("3. OneDrive syncing is paused (since it targets the Documents directory).")
                print("4. Windows Defender Ransomware Protection / Controlled Folder Access is turned off.")
                print("!"*60 + "\n")
                sys.exit(1)

    ct_entries = len(color_table) // 4
    print(f"Saved: {output_path}")
    print(f"  {width}x{height}  |  8 bpp  |  {ct_entries} palette entries  |  {file_size:,} bytes")


# -------------------------------------------------------------------
# Main conversion function
# -------------------------------------------------------------------

def convert_terrain_bmp(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: Missing input file target at {input_path}")
        return

    # Read entirely into memory immediately and drop the file stream
    with open(input_path, "rb") as f:
        file_bytes = f.read()

    # Feed the memory array to PIL
    with Image.open(io.BytesIO(file_bytes)) as img:
        width, height = img.size
        mode = img.mode
        pixel_bytes = img.tobytes()

    if mode == "P":
        color_table = _parse_raw_color_table(file_bytes)
        colors_used = len(color_table) // 4
        colors_important = colors_used

    elif mode in ("RGB", "RGBA", "L"):
        print(f"Warning: Input is {mode} mode, converting to 8-bit indexed...")
        color_table      = _build_color_table_from_palette_dict(TERRAIN_PALETTE, num_entries=255)
        colors_used      = 255
        colors_important = 255

        reverse = {}
        for i, (r, g, b) in enumerate(
            (TERRAIN_PALETTE.get(j, (j, j, j)) for j in range(255))
        ):
            reverse[(r, g, b)] = i

        with Image.open(io.BytesIO(file_bytes)) as img:
            rgb_img = img.convert("RGB")
            raw_rgb = rgb_img.tobytes()
            
        pixel_bytes = bytearray(width * height)

        for px in range(width * height):
            key = (raw_rgb[px*3], raw_rgb[px*3+1], raw_rgb[px*3+2])
            if key in reverse:
                pixel_bytes[px] = reverse[key]
            else:
                r, g, b = key
                best_idx, best_dist = 0, float("inf")
                for i, (pr, pg, pb) in enumerate(
                    (TERRAIN_PALETTE.get(j, (j, j, j)) for j in range(255))
                ):
                    d = (r-pr)**2 + (g-pg)**2 + (b-pb)**2
                    if d < best_dist:
                        best_dist, best_idx = d, i
                pixel_bytes[px] = best_idx

        pixel_bytes = bytes(pixel_bytes)

    else:
        raise ValueError(f"Unsupported image mode: {mode}")

    pixel_rows = _build_pixel_rows(pixel_bytes, width, height)

    _write_bitmapinfoheader_bmp(
        output_path,
        width, height,
        color_table,
        pixel_rows,
        colors_used=colors_used,
        colors_important=colors_important,
    )


if __name__ == "__main__":
    convert_terrain_bmp(INPUT_PATH, OUTPUT_PATH)
