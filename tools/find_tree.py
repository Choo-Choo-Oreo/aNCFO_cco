#!/usr/bin/env python3
"""find_tree.py -- project tree snapshot, plain-text indented format.

General-purpose rebuild of localisation/_find_tree.py: instead of dumping the
directory it happens to live in, it takes --root (default: the mod project
root, i.e. the parent of tools/), supports ignore patterns and a depth cap,
and writes to stdout or --output.

Output format is kept from the original:
    Structure for: <root name>
    [dir/]
        file
        [subdir/]
            file
    ==============================
    Total Folders: N
    Total Files:   N

Ignore behavior (so it doesn't dump irrelevant or oversized trees):
  * Built-in defaults: VCS/internals (.git, .svn, .hg), __pycache__,
    node_modules, and this mod's binary-asset dirs (gfx, music, sound).
  * Simple patterns from <root>/.gitignore are added by default (plain names
    and * globs only -- no negations, no anchored paths). Disable with
    --no-gitignore.
  * --ignore PATTERN adds more (repeatable, fnmatch against the entry name
    and the /-separated path relative to root).
  * --no-default-ignores drops the built-ins (gitignore handling is separate).
Everything pruned by ignores is summarized on stderr, never silently.
"""
from __future__ import annotations

import argparse
import fnmatch
import os
import sys
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent  # the mod repo root

DEFAULT_IGNORES = [
    ".git", ".svn", ".hg",          # VCS internals
    "__pycache__", "node_modules",  # tool caches
    "gfx", "music", "sound",        # binary asset dirs (thousands of files)
]


def load_gitignore_patterns(root: Path) -> list[str]:
    """Best-effort read of simple patterns from <root>/.gitignore.

    Only plain names and * globs are used. Negations (!), anchored or nested
    paths (containing /), and comments are skipped -- this is a display
    filter, not a git reimplementation.
    """
    gi = root / ".gitignore"
    if not gi.is_file():
        return []
    patterns: list[str] = []
    for raw in gi.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        line = line.rstrip("/")
        if "/" in line:
            continue  # anchored/nested pattern, out of scope
        patterns.append(line)
    return patterns


def is_ignored(name: str, rel_path: str, patterns: list[str]) -> bool:
    for pat in patterns:
        if fnmatch.fnmatch(name, pat) or fnmatch.fnmatch(rel_path, pat):
            return True
    return False


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Write a plain-text indented tree snapshot of a project.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--root", type=Path, default=DEFAULT_ROOT,
                   help="Directory to snapshot.")
    p.add_argument("--ignore", action="append", default=[], metavar="PATTERN",
                   help="Extra ignore pattern (fnmatch, repeatable).")
    p.add_argument("--no-default-ignores", action="store_true",
                   help="Drop the built-in ignore list "
                        f"({', '.join(DEFAULT_IGNORES)}).")
    p.add_argument("--no-gitignore", action="store_true",
                   help="Do not add simple patterns from <root>/.gitignore.")
    p.add_argument("--depth", type=int, default=None, metavar="N",
                   help="Max directory depth below root (root itself = 0).")
    p.add_argument("--output", "-o", type=Path, default=None,
                   help="Write to this file instead of stdout.")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        print(f"ERROR: --root is not a directory: {root}", file=sys.stderr)
        return 2

    patterns = list(args.ignore)
    if not args.no_default_ignores:
        patterns += DEFAULT_IGNORES
    gitignore_patterns: list[str] = []
    if not args.no_gitignore:
        gitignore_patterns = load_gitignore_patterns(root)
        patterns += gitignore_patterns

    out = open(args.output, "w", encoding="utf-8") if args.output else sys.stdout
    output_abs = args.output.resolve() if args.output else None
    self_abs = Path(__file__).resolve()

    file_count = 0
    dir_count = 0
    pruned: dict[str, int] = {}  # rel path of pruned dir -> approx entry count

    try:
        out.write(f"Structure for: {root.name}\n\n")
        for cur, dirs, files in os.walk(root):
            cur_path = Path(cur)
            rel = cur_path.relative_to(root)
            level = 0 if rel == Path(".") else len(rel.parts)

            # depth cap: show the dir line at --depth, don't descend past it
            if args.depth is not None and level > args.depth:
                dirs[:] = []
                continue

            display = root.name if level == 0 else cur_path.name
            out.write(f"{' ' * 4 * level}[{display}/]\n")

            # prune ignored subdirs (records them, never silent)
            kept = []
            for d in sorted(dirs):
                rel_d = (rel / d).as_posix() if level else d
                if is_ignored(d, rel_d, patterns):
                    try:
                        pruned[rel_d] = sum(1 for _ in (cur_path / d).iterdir())
                    except OSError:
                        pruned[rel_d] = -1
                else:
                    kept.append(d)
            dirs[:] = kept
            dir_count += len(kept)

            sub_indent = " " * 4 * (level + 1)
            for f in sorted(files):
                rel_f = (rel / f).as_posix() if level else f
                fp = cur_path / f
                if fp == self_abs or (output_abs and fp == output_abs):
                    continue  # never list this script or its own output
                if is_ignored(f, rel_f, patterns):
                    key = rel_f
                    pruned[key] = pruned.get(key, 0)
                    continue
                out.write(f"{sub_indent}{f}\n")
                file_count += 1

        out.write("\n" + "=" * 30 + "\n")
        out.write(f"Total Folders: {dir_count}\n")
        out.write(f"Total Files:   {file_count}\n")
        out.write("=" * 30 + "\n")
    finally:
        if args.output:
            out.close()

    # transparency: what was skipped and why (stderr, not in the tree itself)
    note = []
    if gitignore_patterns:
        note.append(f"gitignore patterns used: {', '.join(gitignore_patterns)}")
    if pruned:
        pretty = ", ".join(
            f"{k} ({v} entries)" if v >= 0 else k for k, v in sorted(pruned.items())
        )
        note.append(f"pruned by ignore patterns: {pretty}")
    if note:
        print("[find_tree] " + " | ".join(note), file=sys.stderr)
    if args.output:
        print(f"[find_tree] wrote {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
