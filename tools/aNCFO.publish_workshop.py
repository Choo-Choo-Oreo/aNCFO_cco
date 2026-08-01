#!/usr/bin/env python3
"""
aNCFO.publish_workshop.py - Publish "A New Chapter - Fantasy Overhaul" to the
Steam Workshop via steamcmd.

Target item (the only one this mod has):
  https://steamcommunity.com/sharedfiles/filedetails/?id=3301072102

Usage:
  python tools/aNCFO.publish_workshop.py --full
  python tools/aNCFO.publish_workshop.py --full --version 0.3.1
  python tools/aNCFO.publish_workshop.py --base-ref v0.3.0
  python tools/aNCFO.publish_workshop.py --full --dry-run
  STEAM_USERNAME=MyUser python tools/aNCFO.publish_workshop.py --full

Username is read from --username or the STEAM_USERNAME env var.
--version rewrites version= in descriptor.mod for this upload only; omit it
to ship whatever version is currently committed in the repo.

--full is the safe default. --base-ref stages only files changed since a git
ref and relies on the Workshop merging that partial upload into the existing
item rather than replacing it wholesale; it refuses to run when the range
deletes files, because a deletion cannot be expressed that way.

Adapted from Millennium Dawn's publish_workshop.py.
"""

import argparse
import fnmatch
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

HOI4_APP_ID = "394360"

# tools/ sits directly under the mod root.
REPO_ROOT = Path(__file__).resolve().parent.parent

MOD_ID = "3301072102"
MOD_NAME = "A New Chapter - Fantasy Overhaul"

# Files that must always be included (even if unchanged in diff mode).
ALWAYS_KEEP = {"descriptor.mod", "thumbnail.png"}

# Dev/repo artifacts excluded only at the mod root. Names here can collide with
# legitimate game content deeper in the tree, so they are matched at depth 0
# only. Note country_metadata/, tests/, events/, tutorial/ etc. are real game
# folders and are NOT excluded; documentation/ is a vanilla folder name but in
# this repo it holds the wiki mirrors and lore doc, none of which the game loads.
ROOT_ONLY_EXCLUDES = {
    ".gitignore",
    ".gitattributes",
    "CODEOWNERS",
    "CONTRIBUTING.md",
    "CLAUDE.md",
    "LICENSE.md",
    "README.md",
    "documentation",
    "tools",
    "specs",
    "testing-docs",
    "thumbnail.psd",
}

# Dev artifacts excluded wherever they appear in the tree.
ANYWHERE_EXCLUDES = {
    ".git",
    ".github",
    ".claude",
    ".claire",
    ".cwtools",
    ".continue",
    ".opencode",
    ".pi-subagents",
    ".vs",
    ".vscode",
    ".idea",
    "vscode-userdata:",
    ".DS_Store",
    "desktop.ini",
    "AGENTS.md",
    "node_modules",
    "__pycache__",
    "*.pyc",
    "*.pyo",
    "*.pyd",
    "*.psd",
    "pythontools.log",
    "repomix-*.xml",
    ".full_diff.txt",
    ".tmp-archive",
    ".validation_cache",
    ".md-mcp-cache",
    ".mypy_cache",
    ".ruff_cache",
    ".pytest_cache",
}

DEFAULT_EXCLUDES = ROOT_ONLY_EXCLUDES | ANYWHERE_EXCLUDES

# Braille spinner frames break when stdout is redirected to a cp1252 file on
# Windows, so fall back to ASCII unless the stream can actually encode them.
_UNICODE_OK = (sys.stdout.encoding or "").lower().replace("-", "") in {
    "utf8",
    "utf16",
    "utf32",
    "cp65001",
}


def elapsed_str(start: float) -> str:
    s = int(time.time() - start)
    if s < 60:
        return f"{s}s"
    return f"{s // 60}m {s % 60:02d}s"


class Spinner:
    """Animated spinner that shows elapsed time on a single line."""

    FRAMES = "\u280b\u2819\u2839\u2838\u283c\u2834\u2826\u2827\u2807\u280f" if _UNICODE_OK else "|/-\\"

    def __init__(self, label: str):
        self._label = label
        self._start = time.time()
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._spin, daemon=True)

    def _spin(self) -> None:
        i = 0
        while not self._stop.is_set():
            frame = self.FRAMES[i % len(self.FRAMES)]
            sys.stdout.write(f"\r  {frame} {self._label} [{elapsed_str(self._start)}]   ")
            sys.stdout.flush()
            i += 1
            self._stop.wait(0.1)

    def __enter__(self) -> "Spinner":
        self._thread.start()
        return self

    def __exit__(self, exc_type: object, *_: object) -> None:
        self._stop.set()
        self._thread.join()
        dt = elapsed_str(self._start)
        status = "+" if exc_type is None else "x"
        label = self._label if exc_type is None else f"{self._label} failed"
        sys.stdout.write(f"\r  {status} {label} [{dt}]\n")
        sys.stdout.flush()


def find_steamcmd() -> Path:
    found = shutil.which("steamcmd")
    if found:
        return Path(found)
    for p in [
        Path("C:/Program Files/steamcmd/steamcmd.exe"),
        Path("C:/Program Files (x86)/steamcmd/steamcmd.exe"),
        Path("C:/steamcmd/steamcmd.exe"),
        Path.home() / "steamcmd" / "steamcmd.exe",
        Path.home() / "steamcmd" / "steamcmd.sh",
        Path("/usr/bin/steamcmd"),
        Path("/usr/local/bin/steamcmd"),
    ]:
        if p.exists():
            return p
    sys.exit(
        "ERROR: steamcmd not found. Install it from "
        "https://developer.valvesoftware.com/wiki/SteamCMD and add it to PATH, "
        "or unpack it to C:/steamcmd/."
    )


def git_diff_name_only(base_ref: str, diff_filter: str, find_renames: bool = True) -> set[str]:
    rename_flag = "--find-renames" if find_renames else "--no-renames"
    try:
        result = subprocess.run(
            [
                "git",
                "diff",
                "--name-only",
                f"--diff-filter={diff_filter}",
                rename_flag,
                f"{base_ref}...HEAD",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.strip() or exc.stdout.strip() or str(exc)
        sys.exit(f"ERROR: Failed to diff against '{base_ref}': {detail}")

    return {l for l in result.stdout.splitlines() if l}


def get_changed_files(base_ref: str) -> set[str]:
    files = git_diff_name_only(base_ref, "ACMR")
    if not files:
        sys.exit(f"No files changed since '{base_ref}'. Nothing to publish.")
    return files


def get_untracked_files() -> set[str]:
    """Working-tree files git doesn't know about.

    Diff mode derives its file list from git, so a new state/event file that
    was never committed is invisible to it and gets pruned away. This mod's
    working tree routinely carries such files, so warn rather than ship a
    silently incomplete update.
    """
    result = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return set()
    return {l for l in result.stdout.splitlines() if l}


def get_deleted_files(base_ref: str) -> set[str]:
    # --no-renames so a rename decomposes into add + delete; otherwise the old
    # path is reported as R (never D) and its stale file lingers in the Workshop.
    return git_diff_name_only(base_ref, "D", find_renames=False)


def get_publishable_changed_files(mod_dir: Path, changed: set[str]) -> set[str]:
    """Return changed files that survived the copy/exclude step."""
    return {
        path.relative_to(mod_dir).as_posix()
        for path in mod_dir.rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and path.relative_to(mod_dir).as_posix() in changed
    }


def dir_stats(root: Path) -> tuple[int, int]:
    """Return (file_count, total_bytes) for a directory tree."""
    count, total = 0, 0
    for path in root.rglob("*"):
        if path.is_file():
            count += 1
            total += path.stat().st_size
    return count, total


def format_size(n: int | float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def copy_repo(dest_parent: Path, excludes: set[str], dest_name: str = "mod") -> Path:
    dest = dest_parent / dest_name

    # Anything in excludes that is also in ROOT_ONLY_EXCLUDES is applied only at
    # the mod root. Everything else matches at every depth. Note: an exclusion
    # added via --exclude that happens to collide with a ROOT_ONLY_EXCLUDES name
    # is treated as root-only too.
    root_only = {e for e in excludes if e in ROOT_ONLY_EXCLUDES}
    anywhere = excludes - root_only

    def _ignore(dir_path: str, names: list[str]) -> set[str]:
        patterns = anywhere
        abs_dir = Path(dir_path).resolve()
        if abs_dir == REPO_ROOT:
            patterns = patterns | root_only
        return {n for n in names if n in patterns or any(fnmatch.fnmatch(n, p) for p in patterns)}

    with Spinner("Copying mod files"):
        shutil.copytree(REPO_ROOT, dest, ignore=_ignore)

    count, total = dir_stats(dest)
    print(f"    {count:,} files, {format_size(total)}")
    return dest


def escape_vdf(value: str | Path) -> str:
    """Escape a string for inclusion in a quoted VDF value."""
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\r", "\\r")
        .replace("\n", "\\n")
    )


def validate_mod_files(mod_dir: Path) -> None:
    """Check that required mod files exist and the thumbnail is Workshop-legal."""
    required = {
        "descriptor.mod": mod_dir / "descriptor.mod",
        "thumbnail.png": mod_dir / "thumbnail.png",
    }
    missing = [name for name, path in required.items() if not path.exists()]
    if missing:
        sys.exit(f"ERROR: Missing required mod files: {', '.join(missing)}")

    # Steam rejects preview images over 1 MiB with an unhelpful generic failure.
    preview_bytes = required["thumbnail.png"].stat().st_size
    if preview_bytes > 1024 * 1024:
        sys.exit(
            f"ERROR: thumbnail.png is {format_size(preview_bytes)}; Steam rejects "
            "preview images over 1.0 MB. Shrink it before publishing."
        )


def prune_unchanged(mod_dir: Path, changed: set[str], verbose: bool = False) -> None:
    removed, kept = 0, []
    for path in list(mod_dir.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        rel = path.relative_to(mod_dir).as_posix()
        if rel in changed or rel in ALWAYS_KEEP:
            kept.append((rel, path.stat().st_size))
        else:
            try:
                path.unlink()
                removed += 1
            except OSError as e:
                print(f"  WARNING: Failed to remove {rel}: {e}")

    # Clean empty directories.
    for path in sorted(mod_dir.rglob("*"), reverse=True):
        if path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass

    kept.sort(key=lambda x: x[1], reverse=True)
    total = sum(s for _, s in kept)
    if verbose:
        print(f"\n  {'File':<70}  {'Size':>10}")
        print(f"  {'-' * 70}  {'-' * 10}")
        for rel, size in kept:
            print(f"  {rel:<70}  {format_size(size):>10}")
        print(f"  {'-' * 70}  {'-' * 10}")
        print(f"  {'TOTAL':<70}  {format_size(total):>10}")
        print(f"\n  Removed {removed}, kept {len(kept)} files.")
    else:
        print(
            f"\n  Removed {removed}, kept {len(kept)} files "
            f"({format_size(total)}; pass --verbose for listing)."
        )


def write_vdf(mod_dir: Path, changenote: str) -> Path:
    vdf_path = mod_dir.parent / "workshop_upload.vdf"
    vdf_path.write_text(
        f'"workshopitem"\n'
        f"{{\n"
        f'    "appid"           "{HOI4_APP_ID}"\n'
        f'    "publishedfileid" "{escape_vdf(MOD_ID)}"\n'
        f'    "contentfolder"   "{escape_vdf(mod_dir)}"\n'
        f'    "previewfile"     "{escape_vdf(mod_dir / "thumbnail.png")}"\n'
        f'    "changenote"      "{escape_vdf(changenote)}"\n'
        f"}}\n",
        encoding="utf-8",
    )
    return vdf_path


def patch_descriptor(mod_dir: Path, version: str | None) -> None:
    """Rewrite name, remote_file_id, and (optionally) version in descriptor.mod.

    The shipped copy is made self-consistent with this Workshop item so the
    launcher binds the uploaded content to the right entry even if the repo's
    descriptor drifts. Read as utf-8-sig / written as utf-8: a stray BOM would
    otherwise hide the first line from the prefix match, and .txt-family files
    in this mod are BOM-less by convention.
    """
    descriptor = mod_dir / "descriptor.mod"
    if not descriptor.exists():
        print("  WARNING: descriptor.mod not found in content folder; skipping patch")
        return

    raw = descriptor.read_text(encoding="utf-8-sig")
    newline = "\r\n" if "\r\n" in raw else "\n"

    updates = {
        "name=": f'name="{MOD_NAME}"{newline}',
        "remote_file_id=": f'remote_file_id="{MOD_ID}"{newline}',
    }
    if version:
        updates["version="] = f'version="{version}"{newline}'

    lines = raw.splitlines(keepends=True)
    patched: set[str] = set()
    for i, line in enumerate(lines):
        for prefix, replacement in updates.items():
            if prefix in patched:
                continue
            if line.startswith(prefix):
                lines[i] = replacement
                patched.add(prefix)
                break

    # Any field missing from the descriptor is appended so the upload is
    # self-consistent rather than silently omitting it.
    if lines and not lines[-1].endswith(("\n", "\r")):
        lines[-1] += newline
    for prefix in updates.keys() - patched:
        print(f"  WARNING: descriptor.mod had no '{prefix.rstrip('=')}' line; appending")
        lines.append(updates[prefix])

    descriptor.write_text("".join(lines), encoding="utf-8", newline="")

    print(f"  Mod name:       {MOD_NAME}")
    print(f"  remote_file_id: {MOD_ID}")
    if version:
        print(f"  version:        {version}")
    else:
        print("  version:        (unchanged - using repo descriptor.mod value)")


def write_launcher_mod(mod_dir: Path) -> Path:
    """Write the sibling <folder>.mod the HOI4 launcher needs to see a local mod.

    Built from the staged descriptor.mod so replace_path lines match exactly --
    the launcher applies replace_path from THIS file, and a mismatch between the
    two is a known crash source. remote_file_id is dropped on purpose: a second
    local .mod claiming the same Workshop id as aNCFO_cco.mod would leave the
    launcher reconciling two entries for one subscribed item.
    """
    descriptor = mod_dir / "descriptor.mod"
    raw = descriptor.read_text(encoding="utf-8-sig")
    newline = "\r\n" if "\r\n" in raw else "\n"

    # The launcher lists mods by the name in THIS file, so a suffix keeps the
    # staged copy distinguishable from aNCFO_cco in the mod list. The payload's
    # own descriptor.mod is untouched and still carries the real name.
    kept = [
        f'name="{MOD_NAME} [staged]"' if l.startswith("name=") else l
        for l in raw.splitlines()
        if not l.startswith(("remote_file_id=", "path="))
    ]
    kept.append(f'path="{mod_dir.as_posix()}"')

    launcher = mod_dir.parent / f"{mod_dir.name}.mod"
    launcher.write_text(newline.join(kept) + newline, encoding="utf-8", newline="")
    return launcher


def steam_login(steamcmd: Path, username: str) -> None:
    """Log in to Steam interactively to cache credentials before uploading."""
    print(f"  Logging in to Steam as '{username}'...")
    print("  (Enter password / Steam Guard code if prompted)\n")
    ret = subprocess.call([str(steamcmd), "+login", username, "+quit"])
    if ret != 0:
        sys.exit(f"ERROR: Steam login failed (exit code {ret})")
    print("\n  Login successful - credentials cached.\n")


def publish(mod_dir: Path, username: str, changenote: str, verbose: bool = False) -> None:
    steamcmd = find_steamcmd()

    # Pre-login interactively so credentials are cached for the upload.
    steam_login(steamcmd, username)

    vdf_path = write_vdf(mod_dir, changenote)

    # Persistent log outside the temp content folder so it survives cleanup.
    log_path = Path(tempfile.gettempdir()) / f"aNCFO_publish_{int(time.time())}.log"

    count, total = dir_stats(mod_dir)

    # Phases are ordered: only move forward, never backwards, to avoid flapping.
    PHASES = [
        ("Connecting", ()),
        ("Logging in", ("logging in", "logged in")),
        ("Waiting for Steam Guard", ("waiting for confirmation",)),
        ("Preparing upload", ("preparing",)),
        ("Uploading content", ("uploading content",)),
        ("Uploading preview", ("uploading preview",)),
        ("Committing update", ("committing",)),
    ]

    # +set_spew_level N N raises steamcmd's console/log verbosity (0=silent, 4=debug).
    # +@ShutdownOnFailedCommand 0 prints failures instead of bailing silently.
    cmd = [
        str(steamcmd),
        "+@ShutdownOnFailedCommand",
        "0",
        "+@NoPromptForPassword",
        "1",
        "+set_spew_level",
        "4",
        "4",
        "+login",
        username,
        "+workshop_build_item",
        str(vdf_path),
        "+quit",
    ]

    preamble = [
        f"  Mod ID:       {MOD_ID}",
        f"  Content dir:  {mod_dir}",
        f"  Files:        {count:,}",
        f"  Total size:   {format_size(total)}",
        f"  VDF:          {vdf_path}",
        f"  steamcmd:     {steamcmd}",
        f"  Log file:     {log_path}",
        "",
        "  --- workshop_upload.vdf ---",
        *(f"    {l}" for l in vdf_path.read_text(encoding="utf-8").splitlines()),
        "  ---------------------------",
        "",
        f"  Command: {shlex.join(cmd)}",
        "",
    ]

    # Short summary always prints; full preamble (VDF contents + command line)
    # only at --verbose. The full version is written to the log file regardless,
    # so post-mortem debugging is unaffected.
    if verbose:
        for pline in preamble:
            print(pline)
    else:
        for pline in preamble[:7]:
            print(pline)
        print("  (pass --verbose to echo workshop_upload.vdf and the steamcmd command)\n")

    with log_path.open("w", encoding="utf-8") as log_f:
        for pline in preamble:
            log_f.write(pline + "\n")

    # steamcmd's first workshop upload frequently fails with transient CM /
    # session errors; a second attempt almost always succeeds. Auth failures
    # short-circuit since they don't fix themselves.
    MAX_ATTEMPTS = 3
    RETRY_BACKOFF_SECS = 15
    AUTH_ERROR_MARKERS = (
        "failed login",
        "invalid password",
        "two-factor code mismatch",
        "account logon denied",
        "rate limit exceeded",
    )

    overall_start = time.time()
    returncode = 1

    for attempt in range(1, MAX_ATTEMPTS + 1):
        if attempt > 1:
            print(f"\n  Retrying in {RETRY_BACKOFF_SECS}s (attempt {attempt}/{MAX_ATTEMPTS})...\n")
            time.sleep(RETRY_BACKOFF_SECS)

        start = time.time()
        phase_start = start
        phase_idx = 0
        phase_timings: list[tuple[str, float]] = []
        auth_failed = False

        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            errors="replace",
            bufsize=1,
        )

        with log_path.open("a", encoding="utf-8") as log_f:
            log_f.write(f"\n=== Attempt {attempt}/{MAX_ATTEMPTS} ===\n")
            log_f.flush()

            for line in proc.stdout:
                line = line.rstrip()
                if not line:
                    continue

                log_f.write(line + "\n")
                log_f.flush()

                low = line.lower()
                if any(m in low for m in AUTH_ERROR_MARKERS):
                    auth_failed = True

                # Detect monotonic phase transitions from steamcmd output.
                for i in range(phase_idx + 1, len(PHASES)):
                    name, keywords = PHASES[i]
                    if any(k in low for k in keywords):
                        dt = time.time() - phase_start
                        phase_timings.append((PHASES[phase_idx][0], dt))
                        print(f"  [{elapsed_str(start)}] + {PHASES[phase_idx][0]} done ({int(dt)}s)")
                        phase_idx = i
                        phase_start = time.time()
                        break

                # Per-line steamcmd echo is huge (hundreds of lines per upload);
                # the full stream is still captured in the log file. At default
                # verbosity only error/warning-looking lines are surfaced so the
                # user isn't blind if steamcmd is unhappy.
                if verbose:
                    print(f"  [{elapsed_str(start)}] {PHASES[phase_idx][0]}: {line}")
                elif any(
                    m in low
                    for m in ("error", "warning", "failed", "fail ", "denied", "timeout")
                ):
                    print(f"  [{elapsed_str(start)}] {PHASES[phase_idx][0]}: {line}")

        proc.wait()
        returncode = proc.returncode
        phase_timings.append((PHASES[phase_idx][0], time.time() - phase_start))

        print(f"\n  --- Phase timings (attempt {attempt}) ---")
        for name, dt in phase_timings:
            print(f"    {name:<28}  {int(dt)}s")
        print(f"    {'TOTAL':<28}  {elapsed_str(start)}\n")

        if returncode == 0:
            print(
                f"  Upload completed in {elapsed_str(overall_start)} "
                f"across {attempt} attempt(s)"
            )
            print(f"  Item: https://steamcommunity.com/sharedfiles/filedetails/?id={MOD_ID}")
            print(f"  Full steamcmd log preserved at: {log_path}")
            return

        if auth_failed:
            print(f"  Full steamcmd output: {log_path}")
            sys.exit(f"ERROR: steamcmd auth failure (exit code {returncode}) - not retrying")

        print(f"  Attempt {attempt} failed with exit code {returncode}.")

    print(f"  Full steamcmd output: {log_path}")
    sys.exit(f"ERROR: steamcmd exited with code {returncode} after {MAX_ATTEMPTS} attempts")


def check_repo_root() -> None:
    """Refuse to run if REPO_ROOT doesn't look like this mod, so a moved or
    copied script fails loudly instead of packaging the wrong directory."""
    descriptor = REPO_ROOT / "descriptor.mod"
    if not descriptor.exists() or not (REPO_ROOT / "map").is_dir():
        sys.exit(
            f"ERROR: {REPO_ROOT} does not look like the aNCFO mod root "
            "(expected descriptor.mod and map/). Keep this script in tools/."
        )
    if f'remote_file_id="{MOD_ID}"' not in descriptor.read_text(encoding="utf-8-sig"):
        print(
            f"  WARNING: repo descriptor.mod does not declare remote_file_id "
            f'"{MOD_ID}"; the shipped copy will be patched to it.'
        )


def main() -> None:
    total_start = time.time()

    parser = argparse.ArgumentParser(
        description='Publish "A New Chapter - Fantasy Overhaul" to the Steam Workshop.',
    )
    parser.add_argument(
        "--username",
        default=os.environ.get("STEAM_USERNAME"),
        help="Steam username (default: $STEAM_USERNAME)",
    )
    parser.add_argument(
        "--version",
        help='Override version= in descriptor.mod (e.g. "0.3.1"). '
        "Leave unset to ship the value already committed in the repo.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Extra exclude patterns (repeatable)",
    )
    parser.add_argument(
        "--no-default-excludes",
        action="store_true",
        help="Skip built-in exclude list",
    )
    parser.add_argument(
        "--changenote",
        default="Update",
        help="Change description for the Workshop (default: Update)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Stage and validate the upload folder, print what would ship, "
        "then stop without contacting Steam.",
    )
    parser.add_argument(
        "--stage-to",
        metavar="DIR",
        help="Implies --dry-run. Stage the exact upload payload into DIR "
        "instead of a temp folder and write the sibling DIR.mod launcher file, "
        "so the packaged result can be loaded and play-tested locally. "
        "Refuses to overwrite a directory it did not stage itself.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Echo the full file listing, VDF contents, steamcmd command, "
        "and per-line steamcmd output (default: summary only; the full stream "
        "is always written to the log file).",
    )

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--base-ref", help="Git ref to diff against (changed files only)")
    mode.add_argument("--full", action="store_true", help="Publish the entire mod")

    args = parser.parse_args()

    check_repo_root()

    stage_to = Path(args.stage_to).resolve() if args.stage_to else None
    if stage_to:
        args.dry_run = True
        if stage_to.resolve() == REPO_ROOT:
            sys.exit("ERROR: --stage-to cannot point at the mod root itself.")
        if stage_to.exists():
            # Only ever reclaim a directory this script produced; anything else
            # (an unrelated mod folder, a typo'd path) is left untouched.
            if not (stage_to / "descriptor.mod").exists():
                sys.exit(
                    f"ERROR: {stage_to} exists and is not a staged mod folder "
                    "(no descriptor.mod). Refusing to overwrite it."
                )
            print(f"  Replacing previous staged folder at {stage_to}")
            shutil.rmtree(stage_to)
        stage_to.parent.mkdir(parents=True, exist_ok=True)

    username = args.username
    if not username and not args.dry_run:
        sys.exit("ERROR: No username. Pass --username or set STEAM_USERNAME.")

    excludes = set() if args.no_default_excludes else set(DEFAULT_EXCLUDES)
    excludes.update(args.exclude)

    print(
        f"\n  Repo:   {REPO_ROOT}\n"
        f"  Target: {MOD_NAME} (mod {MOD_ID})\n"
        f"  Mode:   {'diff from ' + args.base_ref if args.base_ref else 'full'}"
        f"{' [DRY RUN]' if args.dry_run else ''}\n"
        f"{f'  Stage:  {stage_to}' + chr(10) if stage_to else ''}"
    )

    tmp = Path(tempfile.mkdtemp(prefix="aNCFO_publish_"))
    keep_tmp = False
    stage_parent = stage_to.parent if stage_to else tmp
    stage_name = stage_to.name if stage_to else "mod"
    try:
        if args.base_ref:
            deleted = get_deleted_files(args.base_ref)
            if deleted:
                sys.exit(
                    "ERROR: Diff publish cannot safely express deleted files. "
                    "Use --full when the range removes content."
                )

            changed = get_changed_files(args.base_ref)
            print(f"  {len(changed)} file(s) changed since {args.base_ref}")

            untracked = get_untracked_files()
            if untracked:
                print(
                    f"  WARNING: {len(untracked)} untracked file(s) in the working tree "
                    "will NOT be published in diff mode (git diff cannot see them). "
                    "Commit them or use --full."
                )
                for rel in sorted(untracked)[:10]:
                    print(f"    - {rel}")
                if len(untracked) > 10:
                    print(f"    ... and {len(untracked) - 10} more")

            mod_dir = copy_repo(stage_parent, excludes, stage_name)
            publishable_changed = get_publishable_changed_files(mod_dir, changed)
            skipped = sorted(changed - publishable_changed)
            if skipped:
                print(
                    f"  {len(skipped)} changed file(s) are excluded from publishing "
                    "and will be ignored"
                )
                if args.verbose:
                    for rel in skipped:
                        print(f"    - {rel}")
            if not publishable_changed - ALWAYS_KEEP:
                sys.exit(
                    "ERROR: No publishable mod files changed after excludes. "
                    "Use --full or adjust --exclude / --no-default-excludes."
                )
            prune_unchanged(mod_dir, publishable_changed, verbose=args.verbose)
        else:
            mod_dir = copy_repo(stage_parent, excludes, stage_name)

        # Rewrite descriptor.mod so the shipped copy matches this Workshop item.
        patch_descriptor(mod_dir, args.version)

        validate_mod_files(mod_dir)

        if args.dry_run:
            count, total = dir_stats(mod_dir)
            print(f"\n  Dry run: {count:,} files, {format_size(total)} staged at {mod_dir}")
            print("  Top-level entries that would ship:")
            for entry in sorted(p.name for p in mod_dir.iterdir()):
                print(f"    {entry}")
            print("\n  Nothing was uploaded. Re-run without --dry-run to publish.")
            if stage_to:
                launcher = write_launcher_mod(mod_dir)
                print(f"  Launcher file: {launcher}")
                print(
                    "  Enable it in the HOI4 launcher's mod list to play-test the "
                    "packaged result. Disable aNCFO_cco first so the two do not "
                    "both load."
                )
            else:
                print(f"  Staged folder kept for inspection; delete it when done:\n    {tmp}")
                # Only meaningful without --stage-to; there, tmp stays empty.
                keep_tmp = True
        else:
            print()
            publish(mod_dir, username, args.changenote, verbose=args.verbose)
    finally:
        # A completed dry run keeps its staged folder so the exclude list can be
        # eyeballed; every other exit path cleans up (it is ~800 MB).
        if not keep_tmp:
            shutil.rmtree(tmp, ignore_errors=True)

    print(f"\n  Total time: {elapsed_str(total_start)}\n")


if __name__ == "__main__":
    main()
