#!/usr/bin/env python3
"""crash_triage.py -- Automates the HOI4 crash-triage procedure from CLAUDE.md.

Given the HOI4 crashes directory and logs directory, this tool:
  1. Finds the most recently created hoi4_* crash subfolder.
  2. Parses meta.yml and extracts the LastRead (file/identifier + line).
  3. Displays the priority-ordered logs (per CLAUDE.md's usefulness list),
     preferring the crash folder's own frozen snapshot and falling back to
     the live logs directory.
  4. Matches LastRead against CLAUDE.md's "Common crash causes by phase" table
     and prints candidate causes as SUGGESTIONS (not conclusions).
  5. If LastRead points at the LAST line of its file, flags that the true
     failure is likely in the NEXT file read -- per CLAUDE.md's caveat -- and
     does NOT guess which file that is.

This mirrors the manual workflow in CLAUDE.md; it does not replace human
judgment on ambiguous cases -- it surfaces them the same way CLAUDE.md does.

Run  python crash_triage.py --help  for options.
"""
from __future__ import annotations

import argparse
import fnmatch
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------
# Default paths -- taken verbatim from CLAUDE.md. Override with CLI flags.
# --------------------------------------------------------------------------
DOCS = Path.home() / "Documents" / "Paradox Interactive" / "Hearts of Iron IV"
DEFAULT_CRASHES_DIR = DOCS / "crashes"
DEFAULT_LOGS_DIR = DOCS / "logs"
DEFAULT_MOD_DIR = Path(__file__).resolve().parent.parent  # the mod repo root
DEFAULT_BASE_GAME_DIR = Path(
    r"D:\Program Files\SteamLibrary\steamapps\common\Hearts of Iron IV"
)

# Priority-ordered log filenames, highest usefulness first (CLAUDE.md).
LOG_PRIORITY = [
    ("error.log", "nonfatal errors; almost all common/ entries should be fixed"),
    ("game.log", "actions taken by countries; useful when a crash follows an action"),
    ("setup.log", "setup loading completion per step; pinpoints a loading crash"),
    ("memory.log", "memory used during setup; narrows down a loading crash"),
    ("time.log", "time per loading step and tick interval; also loading crashes"),
    ("ai.log", "medium usefulness, situational"),
    ("system_debug.log", "medium usefulness, situational"),
    ("text.log", "medium usefulness, situational"),
]

# --------------------------------------------------------------------------
# "Common crash causes by phase" table, encoded from CLAUDE.md.
# Each entry: patterns that a LastRead token may match (file paths, globs, or
# identifiers like set_controller / client_ping), the phase, the candidate
# cause text, and whether reproducing it requires an in-game action.
# --------------------------------------------------------------------------
@dataclass
class CauseRule:
    patterns: list[str]
    phase: str
    cause: str
    requires_ingame_action: bool = False


CAUSE_TABLE: list[CauseRule] = [
    # --- Main menu loading ---
    CauseRule(
        ["common/countries/cosmetic.txt"],
        "Main menu loading",
        "Usually a full overwrite of common/national_focus/ or common/continuous_focus/.",
    ),
    CauseRule(
        ["map/rocketsites.txt"],
        "Main menu loading",
        "Usually a full overwrite of history/states/ or common/unit_leader/ "
        "(no generic fallback for states).",
    ),
    CauseRule(
        ["common/national_focus/*.txt", "common/national_focus/*"],
        "Main menu loading",
        "Often a shared_focus reference to a focus that does not exist.",
    ),
    CauseRule(
        ["gfx/models/supply/railroad.shader"],
        "Main menu loading",
        "Usually a malformed map bitmap: dimensions not divisible by 256, a "
        "bitmap over 40 MiB, mismatched dimensions between bitmaps, or a wrong "
        "DIB header.",
    ),
    CauseRule(
        ["history/general/*", "history/countries/*", "map/rocketsites.txt"],
        "Main menu loading",
        "A victory_points entry pointing at a province that does not exist.",
    ),
    CauseRule(
        ["savegame.hoi4", "map/cities.txt"],
        "Main menu loading",
        "Too many defined countries relative to available dynamic country slots "
        "(typically 40-80), often from a reckless overwrite of common/country_tags.",
    ),
    # --- During country selection (requires in-game action to reproduce) ---
    CauseRule(
        ["set_controller"],
        "During country selection",
        "A bookmark country missing a valid capital in its history/countries/TAG file.",
        requires_ingame_action=True,
    ),
    CauseRule(
        ["history/units/*"],
        "During country selection",
        "A naval OOB with airwings defined directly on a carrier (pre-1.12 syntax).",
        requires_ingame_action=True,
    ),
    CauseRule(
        ["history/units/*", "map/railways.txt"],
        "During country selection",
        "A division template with no matching common/ai_templates entry.",
        requires_ingame_action=True,
    ),
    CauseRule(
        ["map/supply_nodes.txt", "map/railways.txt"],
        "During country selection",
        "A supply building placed on a province not inside any state.",
        requires_ingame_action=True,
    ),
    CauseRule(
        ["tutorial/tutorial.txt"],
        "During country selection",
        "An erroneous tutorial file; replacing its contents with an empty "
        "tutorial block usually fixes it.",
        requires_ingame_action=True,
    ),
    # --- Middle of the game (requires in-game action to reproduce) ---
    CauseRule(
        ["client_ping", "hourly_tick"],
        "Middle of the game",
        "Almost always AI related (test by disabling AI via console). Common "
        "causes: a division template with no matching ai_templates entry, a "
        "state with no owner defined in its history file, or an incomplete "
        "map/buildings.txt affecting naval base / floating harbour placement.",
        requires_ingame_action=True,
    ),
]


# --------------------------------------------------------------------------
# Small output helpers
# --------------------------------------------------------------------------
def hr(char: str = "=", width: int = 74) -> str:
    return char * width


def section(title: str) -> None:
    print()
    print(hr())
    print(title)
    print(hr())


def die(msg: str, code: int = 2) -> "NoReturn":  # type: ignore[valid-type]
    print(f"\nERROR: {msg}", file=sys.stderr)
    sys.exit(code)


# --------------------------------------------------------------------------
# Step 1 -- locate the most recent crash folder
# --------------------------------------------------------------------------
CRASH_FOLDER_RE = re.compile(r"^hoi4_\d{8}_\d{6}$")


def find_latest_crash_folder(crashes_dir: Path) -> Path:
    if not crashes_dir.is_dir():
        die(f"Crashes directory does not exist: {crashes_dir}")
    candidates = [
        p for p in crashes_dir.iterdir()
        if p.is_dir() and CRASH_FOLDER_RE.match(p.name)
    ]
    if not candidates:
        die(
            f"No hoi4_XXXXXXXX_XXXXXX crash subfolders found in {crashes_dir}. "
            "Nothing to triage."
        )
    # Sort by folder mtime (creation time on Windows is unreliable across copies;
    # mtime of the timestamped folder is set when the crash is written).
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0]


# --------------------------------------------------------------------------
# Step 2 -- parse meta.yml
# --------------------------------------------------------------------------
@dataclass
class Meta:
    fields: dict[str, str] = field(default_factory=dict)
    lastread_raw: str | None = None
    lastread_target: str | None = None  # file path or identifier
    lastread_line: int | None = None


LASTREAD_RE = re.compile(r"^\s*LastRead\s*:\s*(?P<target>.+?)\s*\((?P<line>\d+)\)\s*$")


def parse_meta(crash_folder: Path) -> Meta:
    meta_path = crash_folder / "meta.yml"
    if not meta_path.is_file():
        die(
            f"Crash folder {crash_folder.name} has no meta.yml "
            f"(expected at {meta_path}). Cannot triage this folder -- per "
            "CLAUDE.md this is an ambiguous case that needs a human look."
        )
    meta = Meta()
    for line in meta_path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = LASTREAD_RE.match(line)
        if m:
            meta.lastread_raw = line.strip()
            meta.lastread_target = m.group("target").strip().strip('"')
            meta.lastread_line = int(m.group("line"))
            continue
        # generic "Key: value" capture for the summary block
        if ":" in line and not line.lstrip().startswith("#"):
            k, _, v = line.partition(":")
            k = k.strip()
            if k:
                meta.fields[k] = v.strip()
    if meta.lastread_raw is None:
        die(
            f"meta.yml in {crash_folder.name} has no parseable "
            "'LastRead: <target> (<line>)' entry. Inspect it manually."
        )
    return meta


# --------------------------------------------------------------------------
# Step 3 -- resolve the LastRead file and check the last-line caveat
# --------------------------------------------------------------------------
@dataclass
class LastReadResolution:
    is_file_path: bool
    resolved_path: Path | None
    searched: list[Path]
    total_lines: int | None
    is_last_line: bool | None  # None => could not determine


def looks_like_file_path(target: str) -> bool:
    # Identifiers from the table (set_controller, client_ping, hourly_tick) have
    # no path separator and no file extension. Real LastRead file paths do.
    return "/" in target or "\\" in target or "." in target


def resolve_lastread(meta: Meta, mod_dir: Path, base_game_dir: Path) -> LastReadResolution:
    target = meta.lastread_target or ""
    if not looks_like_file_path(target):
        return LastReadResolution(False, None, [], None, None)

    rel = target.replace("\\", "/")
    searched: list[Path] = []
    resolved: Path | None = None
    for root in (mod_dir, base_game_dir):
        cand = (root / rel)
        searched.append(cand)
        if cand.is_file():
            resolved = cand
            break

    if resolved is None:
        return LastReadResolution(True, None, searched, None, None)

    try:
        text = resolved.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return LastReadResolution(True, resolved, searched, None, None)

    # Count lines the way an editor numbers them (1-based, trailing newline
    # does not create an extra empty line).
    lines = text.splitlines()
    total = len(lines)
    is_last = (meta.lastread_line is not None and meta.lastread_line >= total)
    return LastReadResolution(True, resolved, searched, total, is_last)


# --------------------------------------------------------------------------
# Step 4 -- match LastRead against the cause table
# --------------------------------------------------------------------------
def match_causes(target: str) -> list[CauseRule]:
    norm = target.replace("\\", "/").strip().strip('"')
    matches: list[CauseRule] = []
    for rule in CAUSE_TABLE:
        for pat in rule.patterns:
            pat_norm = pat.replace("\\", "/")
            if "*" in pat_norm or "?" in pat_norm:
                if fnmatch.fnmatch(norm, pat_norm):
                    matches.append(rule)
                    break
            else:
                # exact identifier match, or file path match on the tail
                if norm == pat_norm or norm.endswith("/" + pat_norm) or norm == pat_norm.split("/")[-1]:
                    matches.append(rule)
                    break
    return matches


# --------------------------------------------------------------------------
# Step 4b -- heuristic upstream-reference scan of error.log
#
# Observed once (plane_designer_model.txt crash, 2026-07-08): a last-line
# LastRead meant the crash was a later resolution step choking on a bad
# cross-reference defined in an EARLIER file, not a problem in the next file
# read. When the last-line caveat fires and the cause table has no match,
# scan error.log for reference-error signatures and surface the earliest
# hits as CANDIDATES. This is a heuristic, not a diagnosis -- same standing
# as the table match.
# --------------------------------------------------------------------------
REFERENCE_ERROR_SIGNATURES = [
    "Unexpected token",
    "is not an equipment type",
    "could not find",
    "missing",
]

# Missing textures/icons are the most common BENIGN errors in a HOI4 log and
# are near-never crash causes; keep them out of the headline candidates.
COSMETIC_RE = re.compile(
    r"texture|icon( shine)?|sprite|\.dds|\.tga", re.IGNORECASE
)


def scan_upstream_reference_errors(
    crash_folder: Path, live_logs: Path, source_pref: str, limit: int = 10
) -> tuple[Path | None, str, list[tuple[int, str]], list[tuple[int, str]]]:
    """Return (error.log path, source label, data-ref hits, cosmetic hits)."""
    path, src = pick_log_source("error.log", crash_folder / "logs", live_logs,
                                source_pref)
    if path is None:
        return None, "", [], []
    data_hits: list[tuple[int, str]] = []
    cosmetic_hits: list[tuple[int, str]] = []
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return path, src, [], []
    for i, line in enumerate(lines, 1):
        low = line.lower()
        if not any(sig.lower() in low for sig in REFERENCE_ERROR_SIGNATURES):
            continue
        if COSMETIC_RE.search(line):
            cosmetic_hits.append((i, line.strip()))
        elif len(data_hits) < limit:
            data_hits.append((i, line.strip()))
    return path, src, data_hits, cosmetic_hits


def show_upstream_scan(crash_folder: Path, live_logs: Path,
                       source_pref: str) -> None:
    section("UPSTREAM REFERENCE SCAN (heuristic candidates, NOT a diagnosis)")
    print("Trigger: LastRead is the last line of its file AND the cause table "
          "has no\nmatch. Per an observed-once case (see CLAUDE.md), the true "
          "cause may be a bad\ncross-reference in an EARLIER file that a later "
          "resolution step choked on.\nEarliest error.log lines matching "
          "reference-error signatures\n"
          f"({', '.join(REFERENCE_ERROR_SIGNATURES)}):")
    path, src, data_hits, cosmetic_hits = scan_upstream_reference_errors(
        crash_folder, live_logs, source_pref)
    if path is None:
        print("\nNo error.log found to scan (crash snapshot or live).")
        return
    print(f"\nScanned: {path}  ({src})")
    if not data_hits and not cosmetic_hits:
        print("No signature matches found. This heuristic has nothing to "
              "offer here;\nfall back to manual log reading.")
        return
    if data_hits:
        print("\nData-reference errors (earliest first):")
        for lineno, text in data_hits:
            print(f"  error.log:{lineno}  {text}")
    else:
        print("\nNo data-reference errors matched -- only cosmetic asset "
              "misses (below).")
    if cosmetic_hits:
        print(f"\nDe-prioritized: {len(cosmetic_hits)} missing-texture/icon "
              "line(s) also matched the\nsignatures; these are near-never "
              "crash causes. First example:")
        lineno, text = cosmetic_hits[0]
        print(f"  error.log:{lineno}  {text}")
    print("\nThese are candidate ORIGINS to investigate, in file-load order. "
          "Verify\nagainst the actual files before acting -- a signature match "
          "is not proof.")


# --------------------------------------------------------------------------
# Step 5 -- display priority-ordered logs
# --------------------------------------------------------------------------
def pick_log_source(
    name: str, crash_logs: Path, live_logs: Path, source_pref: str
) -> tuple[Path | None, str]:
    """Return (path, source-label) for a log file per the source preference."""
    crash_candidate = crash_logs / name
    live_candidate = live_logs / name
    if source_pref == "crash":
        return (crash_candidate if crash_candidate.is_file() else None, "crash-snapshot")
    if source_pref == "live":
        return (live_candidate if live_candidate.is_file() else None, "live")
    # auto: prefer the frozen crash snapshot, fall back to the live logs dir
    if crash_candidate.is_file():
        return (crash_candidate, "crash-snapshot")
    if live_candidate.is_file():
        return (live_candidate, "live")
    return (None, "")


def tail(path: Path, n: int) -> list[str]:
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as e:
        return [f"<could not read: {e}>"]
    if n <= 0 or len(lines) <= n:
        return lines
    return lines[-n:]


def show_logs(
    crash_folder: Path, live_logs: Path, source_pref: str, lines: int
) -> None:
    crash_logs = crash_folder / "logs"
    section("PRIORITY-ORDERED LOGS (most useful first)")
    print(f"crash snapshot dir : {crash_logs}"
          f"{'  (missing)' if not crash_logs.is_dir() else ''}")
    print(f"live logs dir      : {live_logs}"
          f"{'  (missing)' if not live_logs.is_dir() else ''}")
    print(f"source preference  : {source_pref}   (per-log tail: {lines} lines)")

    for name, note in LOG_PRIORITY:
        path, src = pick_log_source(name, crash_logs, live_logs, source_pref)
        print()
        print(hr("-"))
        if path is None:
            print(f"[ {name} ] -- not found ({note})")
            continue
        print(f"[ {name} ]  ({src})  -- {note}")
        print(f"    {path}")
        content = tail(path, lines)
        if not content or all(not c.strip() for c in content):
            print("    (empty)")
            continue
        for c in content:
            print(f"    {c}")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Triage the most recent HOI4 crash, per CLAUDE.md's workflow.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument(
        "--crashes-dir", type=Path, default=DEFAULT_CRASHES_DIR,
        help="HOI4 crashes directory (contains hoi4_* subfolders).",
    )
    p.add_argument(
        "--logs-dir", type=Path, default=DEFAULT_LOGS_DIR,
        help="Live HOI4 logs directory.",
    )
    p.add_argument(
        "--mod-dir", type=Path, default=DEFAULT_MOD_DIR,
        help="Mod repo root, used to resolve LastRead file paths.",
    )
    p.add_argument(
        "--base-game-dir", type=Path, default=DEFAULT_BASE_GAME_DIR,
        help="Base game install, used as fallback to resolve LastRead paths.",
    )
    p.add_argument(
        "--crash-folder", type=Path, default=None,
        help="Triage this specific crash folder instead of the most recent.",
    )
    p.add_argument(
        "--logs-source", choices=("auto", "crash", "live"), default="auto",
        help="Where to read priority logs from. 'auto' prefers the crash "
             "folder's frozen snapshot, then the live dir.",
    )
    p.add_argument(
        "--lines", type=int, default=40,
        help="Tail length per log file (0 = whole file).",
    )
    p.add_argument(
        "--no-logs", action="store_true",
        help="Skip the log dump; show only the crash summary and suggestions.",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    # Step 1: locate crash folder
    if args.crash_folder is not None:
        crash_folder = args.crash_folder
        if not crash_folder.is_dir():
            die(f"--crash-folder does not exist: {crash_folder}")
    else:
        crash_folder = find_latest_crash_folder(args.crashes_dir)

    section(f"CRASH FOLDER: {crash_folder.name}")
    print(f"path : {crash_folder}")

    # Step 2: parse meta.yml
    meta = parse_meta(crash_folder)
    for key in ("AppVersion", "DateTime", "BuildType", "Mods", "LaunchArguments"):
        if key in meta.fields:
            print(f"{key:16}: {meta.fields[key]}")
    print(f"{'LastRead':16}: {meta.lastread_target}  (line {meta.lastread_line})")

    # exception.txt is a useful extra if present
    exc = crash_folder / "exception.txt"
    if exc.is_file():
        first = [l for l in exc.read_text(errors="replace").splitlines() if l.strip()]
        for l in first:
            if "Exception" in l or "at address" in l:
                print(f"{'Exception':16}: {l.strip()}")
                break

    # Step 3/4: resolve LastRead + match cause table
    resolution = resolve_lastread(meta, args.mod_dir, args.base_game_dir)
    matches = match_causes(meta.lastread_target or "")

    section("LastRead ANALYSIS")
    if not resolution.is_file_path:
        print(f"LastRead target '{meta.lastread_target}' is an IDENTIFIER, not a "
              "file path\n(matches a phase/event key in the cause table below, "
              "not a file on disk).")
    else:
        if resolution.resolved_path is not None:
            print(f"Resolved to: {resolution.resolved_path}")
            if resolution.total_lines is not None:
                print(f"File has {resolution.total_lines} lines; "
                      f"LastRead line = {meta.lastread_line}.")
                if resolution.is_last_line:
                    print()
                    print("*** CAVEAT (CLAUDE.md): LastRead is the LAST line of "
                          "its file. ***")
                    print("    The true failure is likely in the NEXT file read, "
                          "not this one.")
                    print("    This tool does NOT guess which file that is -- "
                          "inspect manually.")
                else:
                    print("LastRead is NOT the last line, so the failure is "
                          "plausibly within this file.")
        else:
            print(f"LastRead looks like a file path but was NOT found in the mod "
                  "or base game.\nSearched:")
            for s in resolution.searched:
                print(f"    - {s}")
            print("Cannot check the last-line caveat without the file. Inspect "
                  "manually.")

    section("CANDIDATE CAUSES (suggestions, NOT conclusions)")
    if not matches:
        print(f"No entry in CLAUDE.md's 'Common crash causes by phase' table "
              f"matches\n'{meta.lastread_target}'.")
        print("This does not mean the crash is unexplained -- it means the "
              "manual\ntable has no canned suggestion for this file/identifier. "
              "Fall back to\nthe priority logs and meta.yml above.")
    else:
        for i, rule in enumerate(matches, 1):
            flag = "  [requires in-game action to reproduce]" if rule.requires_ingame_action else ""
            print(f"\n  {i}. Phase: {rule.phase}{flag}")
            print(f"     Cause: {rule.cause}")
        if any(r.requires_ingame_action for r in matches):
            print("\n  NOTE: Items flagged above cannot be reproduced by editing "
                  "files alone.\n  Per CLAUDE.md, the user must perform the in-game "
                  "action (select the\n  country, fire the event, run under observe) "
                  "and report back.")

    # Step 4b: heuristic upstream scan -- only when the last-line caveat fired
    # and the table had nothing to say.
    if resolution.is_last_line and not matches:
        show_upstream_scan(crash_folder, args.logs_dir, args.logs_source)

    # Step 5: logs
    if not args.no_logs:
        show_logs(crash_folder, args.logs_dir, args.logs_source, args.lines)

    print()
    print(hr())
    print("Triage complete. All causes above are SUGGESTIONS -- verify against "
          "the logs\nand the actual files before acting.")
    print(hr())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
