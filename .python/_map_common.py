"""
Shared map-graph helpers for the aNCFO_cco connectivity tools.

Reads the mod's province / state data and derives a land-adjacency graph:
  * parse_definition        -- definition.csv -> colour->id map and land set
  * extract_pixel_adjacency -- provinces.bmp  -> land-land pixel borders
  * apply_adjacency_exceptions -- adjacencies.csv edits (straits / impassable)
  * parse_states            -- history/states -> province grouping and ownership
  * UnionFind               -- connected-components primitive

adjacencies.csv holds ONLY exceptions (sea straits, canal / tunnel passages, and
impassable borders); it never contains standard land borders, which is why land
adjacency has to be read off the bitmap pixels.

These modules live in the mod's root-level .python/ folder. All input paths are
resolved from this file's own location (mod root = the parent of .python/), so
the tools work no matter what directory they are invoked from.

Requires: Pillow, numpy.
"""

import csv
import re
from pathlib import Path

import numpy as np
from PIL import Image

# -------------------------------------------------------------
# PATHS (resolved from this file's location, never from the cwd)
# -------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
MOD_ROOT = SCRIPT_DIR.parent

DEFINITION_FILE = MOD_ROOT / "map" / "definition.csv"
PROVINCES_BMP = MOD_ROOT / "map" / "provinces.bmp"
ADJACENCIES_FILE = MOD_ROOT / "map" / "adjacencies.csv"
STATES_DIR = MOD_ROOT / "history" / "states"
COUNTRY_TAGS_DIR = MOD_ROOT / "common" / "country_tags"
COUNTRIES_DIR = MOD_ROOT / "history" / "countries"


def verify_mod_root(root: Path):
    """Confirm the resolved mod root actually looks like the mod, so a moved or
    renamed script fails loudly instead of silently finding nothing. Returns a
    list of human-readable problems (empty when everything checks out)."""
    problems = []
    if not (root / "descriptor.mod").is_file():
        problems.append(f"descriptor.mod not found at mod root ({root})")
    if not (root / "map").is_dir():
        problems.append(f"map/ folder not found at mod root ({root})")
    if not (root / "history" / "states").is_dir():
        problems.append(f"history/states/ folder not found at mod root ({root})")
    return problems


# -------------------------------------------------------------
# PARSING: definition.csv
# -------------------------------------------------------------


def parse_definition(path: Path):
    """Return (code2id, land_ids).

    code = R<<16 | G<<8 | B  ->  province id
    land_ids = set of province ids whose type is 'land'
    """
    code2id = {}
    land_ids = set()

    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            # Same row-shape guard as map/_switch_land_sea.py: data rows start
            # with a numeric province id.
            if not row or not row[0].isdigit():
                continue
            pid = int(row[0])
            r, g, b = int(row[1]), int(row[2]), int(row[3])
            ptype = row[4].strip().lower()
            code = (r << 16) | (g << 8) | b
            code2id[code] = pid
            if ptype == "land":
                land_ids.add(pid)

    return code2id, land_ids


# -------------------------------------------------------------
# PIXEL ADJACENCY: provinces.bmp
# -------------------------------------------------------------


def _pairs_from_shift(a, b):
    """Given two aligned code arrays, return the (min,max) id-agnostic code
    pairs where they differ, as an (N,2) int64 array."""
    a = a.ravel()
    b = b.ravel()
    mask = a != b
    a = a[mask]
    b = b[mask]
    lo = np.minimum(a, b)
    hi = np.maximum(a, b)
    return np.stack([lo, hi], axis=1)


def extract_pixel_adjacency(bmp_path: Path, code2id: dict, land_ids: set, conn: int):
    """Return a set of frozensets {id_a, id_b} of land provinces whose pixels
    touch on the bitmap. Horizontal edges wrap (map loops E-W)."""
    img = Image.open(bmp_path).convert("RGB")
    arr = np.asarray(img, dtype=np.uint32)  # H x W x 3
    code = (arr[:, :, 0] << 16) | (arr[:, :, 1] << 8) | arr[:, :, 2]

    chunks = []
    # Horizontal neighbours.
    chunks.append(_pairs_from_shift(code[:, :-1], code[:, 1:]))
    # Horizontal wrap: last column against first column.
    chunks.append(_pairs_from_shift(code[:, -1], code[:, 0]))
    # Vertical neighbours.
    chunks.append(_pairs_from_shift(code[:-1, :], code[1:, :]))

    if conn == 8:
        # Down-right and down-left diagonals.
        chunks.append(_pairs_from_shift(code[:-1, :-1], code[1:, 1:]))
        chunks.append(_pairs_from_shift(code[:-1, 1:], code[1:, :-1]))
        # Diagonal wrap columns.
        chunks.append(_pairs_from_shift(code[:-1, -1], code[1:, 0]))
        chunks.append(_pairs_from_shift(code[:-1, 0], code[1:, -1]))

    all_pairs = np.concatenate(chunks, axis=0)
    # Deduplicate code pairs before translating (far fewer unique border pairs).
    unique_pairs = np.unique(all_pairs, axis=0)

    land_adj = set()
    missing_codes = set()
    for lo, hi in unique_pairs:
        ida = code2id.get(int(lo))
        idb = code2id.get(int(hi))
        if ida is None:
            missing_codes.add(int(lo))
            continue
        if idb is None:
            missing_codes.add(int(hi))
            continue
        if ida in land_ids and idb in land_ids and ida != idb:
            land_adj.add(frozenset((ida, idb)))

    if missing_codes:
        print(
            f"WARNING: {len(missing_codes)} bitmap colour(s) had no "
            f"definition.csv entry; those borders were skipped."
        )

    return land_adj


def compute_province_centroids(bmp_path: Path, code2id: dict):
    """Return (centroids, width).

    centroids: province id -> (cx, cy, pixel_count), where cx / cy are the mean
    column (x) and row (y) of that province's pixels in the bitmap. width is the
    bitmap width in pixels, needed for horizontal-wrap distance and for
    normalising distances against the map size.

    The mean is a naive average of pixel coordinates, so a province straddling
    the horizontal wrap seam gets an x that ignores the wrap -- the wrap
    correction is applied when measuring distance between two centroids, exactly
    as extract_pixel_adjacency wraps its horizontal neighbours.
    """
    img = Image.open(bmp_path).convert("RGB")
    arr = np.asarray(img, dtype=np.uint32)  # H x W x 3
    height, width = arr.shape[0], arr.shape[1]
    code = (arr[:, :, 0] << 16) | (arr[:, :, 1] << 8) | arr[:, :, 2]
    flat = code.ravel()
    # Compact per-pixel labels so the bincounts stay province-sized.
    uniq, inv = np.unique(flat, return_inverse=True)
    del arr, code, flat  # free the big bitmap arrays before allocating coords

    counts = np.bincount(inv).astype(np.float64)
    xs = np.tile(np.arange(width, dtype=np.float64), height)  # column per pixel
    ys = np.repeat(np.arange(height, dtype=np.float64), width)  # row per pixel
    sum_x = np.bincount(inv, weights=xs)
    sum_y = np.bincount(inv, weights=ys)
    del xs, ys, inv

    centroids = {}
    for i in range(uniq.size):
        pid = code2id.get(int(uniq[i]))
        if pid is None:
            continue
        n = counts[i]
        centroids[pid] = (sum_x[i] / n, sum_y[i] / n, int(n))

    return centroids, width


# -------------------------------------------------------------
# EXCEPTIONS: adjacencies.csv
# -------------------------------------------------------------


def apply_adjacency_exceptions(land_adj: set, path: Path, land_ids: set):
    """Mutate land_adj in place per adjacencies.csv. Returns (added, removed)."""
    added = 0
    removed = 0

    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            if not row:
                continue
            # Skip any non-data row: the "From;To;..." header (first column not
            # numeric) is dropped here, and the "-1;-1;..." terminator is dropped
            # by the frm/to < 0 guard below.
            if not row[0].strip().lstrip("-").isdigit():
                continue
            frm = int(row[0])
            to = int(row[1])
            if frm < 0 or to < 0:
                continue  # -1;-1;... terminator
            atype = row[2].strip().lower() if len(row) > 2 else ""

            # Only land-land pairs affect landmass connectivity.
            if frm not in land_ids or to not in land_ids:
                continue

            pair = frozenset((frm, to))
            if atype == "impassable":
                if pair in land_adj:
                    land_adj.discard(pair)
                    removed += 1
            else:
                # sea straits, tunnels, canal passages, or blank (defaults sea)
                if pair not in land_adj:
                    land_adj.add(pair)
                    added += 1

    return added, removed


# -------------------------------------------------------------
# STATES: history/states/*.txt
# -------------------------------------------------------------

_ID_RE = re.compile(r"\bid\s*=\s*(\d+)")
_OWNER_RE = re.compile(r"\bowner\s*=\s*([A-Z0-9]{3})")
_CORE_RE = re.compile(r"\badd_core_of\s*=\s*([A-Z0-9]{3})")
# Top-level state-block flag from history/states (State_modding wiki). This is a
# state-level wasteland/buffer flag and is UNRELATED to the adjacencies.csv
# 'impassable' adjacency type handled in apply_adjacency_exceptions().
_STATE_IMPASSABLE_RE = re.compile(r"\bimpassable\s*=\s*yes\b")


def _extract_provinces_block(text: str):
    """Return the list of province ids inside provinces={ ... }."""
    m = re.search(r"provinces\s*=\s*\{", text)
    if not m:
        return []
    start = m.end()
    depth = 1
    i = start
    while i < len(text) and depth > 0:
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        i += 1
    body = text[start : i - 1]
    return [int(tok) for tok in body.split() if tok.isdigit()]


def parse_states(states_dir: Path):
    """Return list of dicts:
    {id, name, provinces(set), owner, cores(set), impassable(bool)}."""
    states = []
    for path in sorted(states_dir.glob("*.txt")):
        text = path.read_text(encoding="utf-8-sig", errors="replace")

        id_m = _ID_RE.search(text)
        if not id_m:
            continue
        sid = int(id_m.group(1))

        name_m = re.search(r'name\s*=\s*"([^"]*)"', text)
        name = name_m.group(1) if name_m else f"STATE_{sid}"

        provinces = set(_extract_provinces_block(text))

        owner_m = _OWNER_RE.search(text)
        owner = owner_m.group(1) if owner_m else None
        cores = set(_CORE_RE.findall(text))

        # Optional top-level state flag; absent means passable.
        impassable = _STATE_IMPASSABLE_RE.search(text) is not None

        states.append(
            {
                "id": sid,
                "name": name,
                "provinces": provinces,
                "owner": owner,
                "cores": cores,
                "impassable": impassable,
                "file": path.name,
            }
        )
    return states


# -------------------------------------------------------------
# CONNECTED COMPONENTS (union-find)
# -------------------------------------------------------------


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        # Path compression.
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb


# -------------------------------------------------------------
# COUNTRY TAG VALIDATION (optional, non-fatal)
# -------------------------------------------------------------


def tag_is_known(tag: str, tags_dir: Path):
    """Best-effort check that the tag appears in common/country_tags. Returns
    True/False, or None if the directory can't be read."""
    if not tags_dir.is_dir():
        return None
    pattern = re.compile(rf"^\s*{re.escape(tag)}\s*=", re.MULTILINE)
    for path in tags_dir.glob("*.txt"):
        try:
            if pattern.search(path.read_text(encoding="utf-8-sig", errors="replace")):
                return True
        except OSError:
            continue
    return False


_CAPITAL_RE = re.compile(r"\bcapital\s*=\s*(\d+)")


def read_capital(tag: str, countries_dir: Path = COUNTRIES_DIR):
    """Return the capital STATE id from history/countries/<TAG> - *.txt, or None
    if the file or the capital field is missing. Country files are named
    "TAG - Name.txt" and are UTF-8 with a BOM, so utf-8-sig is used."""
    if not countries_dir.is_dir():
        return None
    matches = sorted(countries_dir.glob(f"{tag} - *.txt")) or sorted(
        countries_dir.glob(f"{tag}*.txt")
    )
    for path in matches:
        try:
            m = _CAPITAL_RE.search(
                path.read_text(encoding="utf-8-sig", errors="replace")
            )
        except OSError:
            continue
        if m:
            return int(m.group(1))
    return None
