"""Rename history/states/*.txt files to match their in-game localized name.

Each state file is named ID-Descriptor.txt. The descriptor is often stale
(left over from before the state ID was repurposed for this mod). This script
reads the file's `name = "KEY"` field (whatever key it is, e.g. STATE_100 or a
custom key like QUEEN_MAUD_LAND), resolves KEY by scanning every localisation
file under localisation/english/ (custom keys are not confined to
state_names_l_english.yml), and renames the file to ID-<resolved name>.txt via
`git mv` so the rename is tracked.
"""

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATES_DIR = REPO_ROOT / "history" / "states"
LOC_DIR = REPO_ROOT / "localisation" / "english"

FILENAME_RE = re.compile(r"^(\d+)\s*-\s*(.+)\.txt$")
NAME_FIELD_RE = re.compile(r'name\s*=\s*"([^"]+)"')
# Matches `KEY: "value"` or `KEY:0 "value"`, tolerating a trailing `# comment`
# after the closing quote (common in state_names_l_english.yml).
LOC_LINE_RE = re.compile(r'^\s*([A-Za-z0-9_]+):\d*\s*"((?:[^"\\]|\\.)*)"')
INVALID_CHARS_RE = re.compile(r'[\\/:*?"<>|]')


def load_loc_keys(loc_dir: Path) -> dict[str, str]:
    loc_keys: dict[str, str] = {}
    for loc_file in sorted(loc_dir.glob("*.yml")):
        with loc_file.open(encoding="utf-8-sig") as f:
            for line in f:
                match = LOC_LINE_RE.match(line)
                if match:
                    key, value = match.groups()
                    # First definition wins; later duplicate keys across
                    # files are assumed to be the same value and ignored.
                    loc_keys.setdefault(key, value)
    return loc_keys


def sanitize(name: str) -> str:
    return INVALID_CHARS_RE.sub("", name).strip()


def main() -> int:
    if not STATES_DIR.is_dir():
        print(f"States directory not found: {STATES_DIR}")
        return 1
    if not LOC_DIR.is_dir():
        print(f"Localisation directory not found: {LOC_DIR}")
        return 1

    loc_keys = load_loc_keys(LOC_DIR)

    renamed: list[tuple[str, str]] = []
    already_correct: list[str] = []
    unresolved: list[str] = []
    unrecognized: list[str] = []
    errors: list[tuple[str, str]] = []

    for path in sorted(STATES_DIR.glob("*.txt")):
        filename_match = FILENAME_RE.match(path.name)
        if not filename_match:
            unrecognized.append(path.name)
            continue
        state_id, _descriptor = filename_match.groups()

        try:
            content = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            content = path.read_text(encoding="latin-1")

        name_match = NAME_FIELD_RE.search(content)
        if not name_match:
            unresolved.append(f"{path.name} (no name field)")
            continue

        loc_key = name_match.group(1)
        display_name = loc_keys.get(loc_key)
        if display_name is None:
            unresolved.append(f"{path.name} (loc key '{loc_key}' not found)")
            continue

        sanitized = sanitize(display_name)
        if not sanitized:
            unresolved.append(f"{path.name} (loc key '{loc_key}' resolved to empty name)")
            continue

        new_name = f"{state_id}-{sanitized}.txt"
        if new_name == path.name:
            already_correct.append(path.name)
            continue

        try:
            subprocess.run(
                ["git", "mv", path.name, new_name],
                cwd=STATES_DIR,
                check=True,
                capture_output=True,
                text=True,
            )
            renamed.append((path.name, new_name))
        except subprocess.CalledProcessError as exc:
            errors.append((path.name, exc.stderr.strip() or str(exc)))

    print(f"Renamed:         {len(renamed)}")
    print(f"Already correct: {len(already_correct)}")
    print(f"Unresolved:      {len(unresolved)}")
    print(f"Unrecognized:    {len(unrecognized)}")
    print(f"Errors:          {len(errors)}")

    if unresolved:
        print("\nUnresolved files:")
        for entry in unresolved:
            print(f"  - {entry}")

    if unrecognized:
        print("\nUnrecognized filenames (didn't match ID-Descriptor.txt):")
        for entry in unrecognized:
            print(f"  - {entry}")

    if errors:
        print("\nErrors:")
        for name, message in errors:
            print(f"  - {name}: {message}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
