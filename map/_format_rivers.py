"""
_format_rivers.py

Correctly saves rivers.bmp for Hearts of Iron IV.

The game requires ALL of the following, which PIL alone does not guarantee:
  - BITMAPINFOHEADER (40-byte DIB header, not BITMAPV4/V5HEADER)
  - 8-bit indexed (palette mode), never 24-bit RGB
  - No compression (BI_RGB = 0)
  - Palette order preserved exactly (the game reads index IDs, not RGB colours)
  - colors_used / colors_important set to 0 in the DIB header, even though the
    colour table still holds 256 entries. This tells the game to skip reading
    the colour table entirely and go straight to the pixel data. GIMP instead
    writes 256 into that field, which produces the harmless but noisy
    "MAP_ERROR: Palette in rivers.bmp is probably not correct" on load.

Rivers must be exactly one pixel thick, orthogonally connected only (no
diagonal joins), and rivers.bmp must match the pixel dimensions of
provinces.bmp. Indexes 0-11 are the actual river colours read by the game
(0-6 small rivers, 7-11 large rivers); every other index is ignored in-game
and is free to use as a visual "comment" layer, conventionally land shading
to make it easier to trace province outlines while placing rivers.

Usage:
  Run directly from your map directory:
      python _format_rivers.py
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
INPUT_PATH  = os.path.join(SCRIPT_DIR, "rivers.bmp")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "rivers.bmp")

# Indexes 0-11 are read by the game (NDefines.NMilitary.RIVER_SMALL_START_INDEX
# through RIVER_LARGE_STOP_INDEX). Indexes 12-15 and 254-255 are the land
# shading / outline "comment" colours observed in this mod's existing
# rivers.bmp; everything else defaults to the (2, 0, 1) filler also observed
# there.
RIVER_PALETTE = {
     0: (  0, 255,   0),   # river source
     1: (255,   0,   0),   # flow-in source (joins paths into one river)
     2: (255, 252,   0),   # flow-out source (branches outward)
     3: (  0, 225, 255),   # narrowest river texture
     4: (  0, 200, 255),   # narrow river texture
     5: (  0, 150, 255),
     6: (  0, 100, 255),   # wide river texture
     7: (  0,   0, 255),
     8: (  0,   0, 225),
     9: (  0,   0, 200),
    10: (  0,   0, 150),
    11: (  0,   0, 100),   # widest river texture
    12: (  0,  85,   0),   # land shading (not read in-game)
    13: (  0, 125,   0),   # land shading (not read in-game)
    14: (  0, 158,   0),   # land shading (not read in-game)
    15: ( 24, 206,   0),   # land shading (not read in-game)
    16: (  0,   0,   0),   # land outline (not read in-game)
   254: (122, 122, 122),   # land outline (not read in-game)
   255: (255, 255, 255),   # land fill (not read in-game)
}
RIVER_FILLER = (2, 0, 1)   # unused comment-colour filler (indexes 17-253)


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


def _build_color_table_from_palette_dict(palette_dict, num_entries=256):
    ct = bytearray()
    for i in range(num_entries):
        r, g, b = palette_dict.get(i, RIVER_FILLER)
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
    colors_used=0,
    colors_important=0,
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
    print(f"  {width}x{height}  |  8 bpp  |  {ct_entries} palette entries  |  colors_used={colors_used}  |  {file_size:,} bytes")


# -------------------------------------------------------------------
# Main conversion function
# -------------------------------------------------------------------

def convert_rivers_bmp(input_path, output_path):
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
        # Already 8-bit indexed: keep the existing palette exactly as-is.
        # (Preserves index order, including the river colour codes at 0-11
        # and any land-shading "comment" colours already in use.)
        color_table = _parse_raw_color_table(file_bytes)

    elif mode in ("RGB", "RGBA", "L"):
        print(f"Warning: Input is {mode} mode, converting to 8-bit indexed...")
        color_table = _build_color_table_from_palette_dict(RIVER_PALETTE, num_entries=256)

        reverse = {}
        for i, (r, g, b) in enumerate(
            (RIVER_PALETTE.get(j, RIVER_FILLER) for j in range(256))
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
                    (RIVER_PALETTE.get(j, RIVER_FILLER) for j in range(256))
                ):
                    d = (r-pr)**2 + (g-pg)**2 + (b-pb)**2
                    if d < best_dist:
                        best_dist, best_idx = d, i
                pixel_bytes[px] = best_idx

        pixel_bytes = bytes(pixel_bytes)

    else:
        raise ValueError(f"Unsupported image mode: {mode}")

    pixel_rows = _build_pixel_rows(pixel_bytes, width, height)

    # colors_used/colors_important are forced to 0 regardless of the palette
    # entry count. This is the DIB header trick described in
    # documentation/wikis/Wiki_MapModding.txt that avoids
    # "MAP_ERROR: Palette in rivers.bmp is probably not correct".
    _write_bitmapinfoheader_bmp(
        output_path,
        width, height,
        color_table,
        pixel_rows,
        colors_used=0,
        colors_important=0,
    )


if __name__ == "__main__":
    convert_rivers_bmp(INPUT_PATH, OUTPUT_PATH)
