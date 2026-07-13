#!/usr/bin/env python3
"""soak_test.py -- unattended HOI4 soak run using -hands_off.

Launches hoi4.exe with -hands_off -debug -crash_data_log (per
Wiki_LaunchOptions.txt, -hands_off auto-starts a game unpaused at max speed
with human AI on; this mod's defines re-point HANDS_OFF_START_TAG to LLA) and
lets the AI play for --duration minutes, watching for crashes and errors that
only surface over extended play.

Because logs/ is overwritten every launch (CLAUDE.md), error.log and game.log
are snapshotted to a timestamped run folder every --snapshot-interval minutes
DURING the run, not just at the end -- transient mid-run errors survive.

If a new hoi4_* crash folder appears under crashes/, the run stops and hands
off to tools/crash_triage.py (it is not re-implemented here).

At the end (crash, duration reached, or Ctrl+C) a summary is written covering
errors seen across ALL interval snapshots: each unique normalized error line,
its occurrence count, and which snapshot it first appeared in.

Validated on this machine 2026-07-08: ~40-60s from launch to auto-start,
~40 in-game days per wall-clock minute at max speed, logs flush continuously,
30s polling is reliable.

LIMITS -- this does NOT replace the "user performs the action and reports
back" workflow for everything; see the run summary footer and CLAUDE.md.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

DOCS = Path.home() / "Documents" / "Paradox Interactive" / "Hearts of Iron IV"
DEFAULT_GAME_DIR = Path(
    r"D:\Program Files\SteamLibrary\steamapps\common\Hearts of Iron IV"
)
DEFAULT_LOGS_DIR = DOCS / "logs"
DEFAULT_CRASHES_DIR = DOCS / "crashes"
DEFAULT_RUNS_DIR = DOCS / "soak_runs"
CRASH_TRIAGE = Path(__file__).resolve().parent / "crash_triage.py"

SNAPSHOT_LOGS = ["error.log", "game.log"]
EXTRA_FINAL_LOGS = ["setup.log", "ai.log", "system.log", "system_debug.log", "time.log"]

# [HH:MM:SS][game.date][src.cpp:123]: message  ->  strip volatile prefixes so
# identical errors dedupe across snapshots.
STAMP_RE = re.compile(r"^\[[0-9:]+\]\[[^\]]*\]")


def now() -> str:
    return datetime.now().strftime("%H:%M:%S")


def log(msg: str) -> None:
    print(f"[{now()}] {msg}", flush=True)


def hoi4_running() -> bool:
    out = subprocess.run(
        ["tasklist", "/FI", "IMAGENAME eq hoi4.exe", "/NH"],
        capture_output=True, text=True,
    ).stdout
    return "hoi4.exe" in out


def list_crash_folders(crashes_dir: Path) -> set[str]:
    if not crashes_dir.is_dir():
        return set()
    return {p.name for p in crashes_dir.iterdir()
            if p.is_dir() and p.name.startswith("hoi4_")}


def take_snapshot(logs_dir: Path, run_dir: Path, label: str,
                  names: list[str]) -> Path:
    dest = run_dir / f"snapshot_{label}"
    dest.mkdir(parents=True, exist_ok=True)
    for name in names:
        src = logs_dir / name
        if src.is_file():
            try:
                shutil.copy2(src, dest / name)
            except OSError as e:
                log(f"  snapshot copy failed for {name}: {e}")
    log(f"snapshot -> {dest.name}")
    return dest


def normalize(line: str) -> str:
    # Strip a stray BOM/zero-width char so it can't crash the summary print on a
    # cp1252 console (mod .txt files that carry a BOM leak U+FEFF into log lines).
    return STAMP_RE.sub("", line).replace("﻿", "").strip()


def summarize(run_dir: Path, outcome: str, new_crashes: set[str]) -> None:
    """Aggregate error.log lines across every snapshot taken during the run."""
    snapshots = sorted(p for p in run_dir.iterdir()
                       if p.is_dir() and p.name.startswith("snapshot_"))
    first_seen: dict[str, str] = {}   # normalized line -> snapshot label
    counts: dict[str, int] = {}
    for snap in snapshots:
        err = snap / "error.log"
        if not err.is_file():
            continue
        seen_this_snap: set[str] = set()
        for raw in err.read_text(encoding="utf-8", errors="replace").splitlines():
            n = normalize(raw)
            if not n:
                continue
            if n not in seen_this_snap:
                seen_this_snap.add(n)
                counts[n] = counts.get(n, 0) + 1
            first_seen.setdefault(n, snap.name)
    baseline = snapshots[0].name if snapshots else "?"
    mid_run = {k: v for k, v in first_seen.items() if v != baseline}

    lines: list[str] = []
    lines.append("=" * 74)
    lines.append(f"SOAK RUN SUMMARY  ({outcome})")
    lines.append("=" * 74)
    lines.append(f"run dir           : {run_dir}")
    lines.append(f"snapshots taken   : {len(snapshots)}")
    lines.append(f"unique error lines: {len(first_seen)} across all snapshots")
    lines.append(f"new crash folders : {sorted(new_crashes) if new_crashes else 'none'}")
    lines.append("")
    if mid_run:
        lines.append(f"--- {len(mid_run)} error(s) FIRST APPEARED MID-RUN "
                     f"(not present in {baseline}) ---")
        for n, snap in sorted(mid_run.items(), key=lambda kv: kv[1]):
            lines.append(f"  [{snap}] {n}")
    else:
        lines.append(f"--- no NEW errors appeared after the first snapshot "
                     f"({baseline}) ---")
    lines.append("")
    lines.append("--- all unique errors (count = snapshots containing it) ---")
    for n in sorted(first_seen, key=lambda k: (first_seen[k], -counts[k])):
        lines.append(f"  x{counts[n]:<3} first={first_seen[n]}  {n}")
    lines.append("")
    lines.append("LIMITS: -hands_off exercises AI-driven play only. It can catch "
                 "loading errors,\nAI/tick crashes (client_ping / hourly_tick "
                 "class), and script errors the AI\ntriggers over time. It does "
                 "NOT exercise: human-only UI paths, specific manual\ndecisions/"
                 "diplomatic actions, country-selection of arbitrary tags, or "
                 "content\nthe AI never picks. Those still need the CLAUDE.md "
                 "'user performs the action\nand reports back' workflow.")
    text = "\n".join(lines)
    try:
        print(text, flush=True)
    except UnicodeEncodeError:
        enc = sys.stdout.encoding or "utf-8"
        print(text.encode(enc, "replace").decode(enc), flush=True)
    (run_dir / "summary.txt").write_text(text, encoding="utf-8")
    log(f"summary written -> {run_dir / 'summary.txt'}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Unattended -hands_off soak test; snapshots logs on an "
                    "interval and hands crashes to crash_triage.py.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--duration", type=float, default=60,
                   help="Minutes of game runtime after launch.")
    p.add_argument("--poll", type=float, default=30,
                   help="Seconds between liveness/crash checks.")
    p.add_argument("--snapshot-interval", type=float, default=5,
                   help="Minutes between log snapshots.")
    p.add_argument("--game-dir", type=Path, default=DEFAULT_GAME_DIR,
                   help="HOI4 install dir containing hoi4.exe.")
    p.add_argument("--logs-dir", type=Path, default=DEFAULT_LOGS_DIR,
                   help="Live HOI4 logs directory.")
    p.add_argument("--crashes-dir", type=Path, default=DEFAULT_CRASHES_DIR,
                   help="HOI4 crashes directory to watch.")
    p.add_argument("--runs-dir", type=Path, default=DEFAULT_RUNS_DIR,
                   help="Parent folder for timestamped run output.")
    p.add_argument("--autosave", default="NEVER",
                   choices=["NEVER", "DAILY", "WEEKLY", "MONTHLY", "HALFYEAR", "YEARLY"],
                   help="-autosave= override for the run (NEVER avoids "
                        "max-speed autosave churn).")
    p.add_argument("--no-triage", action="store_true",
                   help="On crash, skip invoking crash_triage.py.")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    exe = args.game_dir / "hoi4.exe"
    if not exe.is_file():
        print(f"ERROR: hoi4.exe not found at {exe}", file=sys.stderr)
        return 2
    if hoi4_running():
        print("ERROR: hoi4.exe is already running. Close it first -- a second "
              "instance would fight over the same logs/ directory.",
              file=sys.stderr)
        return 2

    run_dir = args.runs_dir / datetime.now().strftime("run_%Y%m%d_%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=True)
    pre_crashes = list_crash_folders(args.crashes_dir)
    log(f"run dir: {run_dir}")
    log(f"pre-existing crash folders: {len(pre_crashes)}")

    # -start_minimized: Wiki_LaunchOptions.txt says Debug/Release_D builds
    # only. Verified empirically 2026-07-08 (IsIconic on the hoi4 window):
    # NO-OP on this retail build (meta.yml BuildType: Release). Kept because
    # it is harmless and would work on a Release_D build.
    launch = [str(exe), "-hands_off", "-debug", "-crash_data_log",
              "-start_minimized", f"-autosave={args.autosave}"]
    log(f"launching: {' '.join(launch)}")
    proc = subprocess.Popen(launch, cwd=str(args.game_dir))
    log(f"pid={proc.pid}; duration={args.duration}min, "
        f"snapshot every {args.snapshot_interval}min, poll {args.poll}s")

    duration_s = args.duration * 60
    snap_every_s = args.snapshot_interval * 60
    start = time.monotonic()
    snap_idx = 0
    new_crashes: set[str] = set()
    outcome = "duration reached"

    # First snapshot ~90s in (once setup is done and error.log is populated),
    # or at the interval if it is shorter. After each snapshot the next one is
    # scheduled a full interval later -- a single schedule variable, so the
    # early first snapshot can never make the second fire immediately after.
    next_snap_at = min(90.0, snap_every_s)

    try:
        while True:
            elapsed = time.monotonic() - start
            if elapsed >= duration_s:
                break
            time.sleep(min(args.poll, max(1.0, duration_s - elapsed)))
            elapsed = time.monotonic() - start

            alive = proc.poll() is None
            new_crashes = list_crash_folders(args.crashes_dir) - pre_crashes
            if new_crashes:
                outcome = f"CRASH FOLDER APPEARED: {sorted(new_crashes)}"
                log(outcome)
                break
            if not alive:
                outcome = f"game exited on its own (exit code {proc.poll()})"
                log(outcome)
                break

            if elapsed >= next_snap_at:
                snap_idx += 1
                next_snap_at = elapsed + snap_every_s
                take_snapshot(args.logs_dir, run_dir,
                              f"{snap_idx:02d}_t+{int(elapsed)//60}min",
                              SNAPSHOT_LOGS)
    except KeyboardInterrupt:
        outcome = "interrupted by user (Ctrl+C)"
        log(outcome)
    finally:
        if proc.poll() is None:
            log(f"terminating pid={proc.pid}")
            proc.terminate()
            try:
                proc.wait(timeout=30)
            except subprocess.TimeoutExpired:
                log("terminate timed out; killing")
                proc.kill()
                proc.wait(timeout=15)
        time.sleep(5)  # let the OS flush file buffers
        snap_idx += 1
        take_snapshot(args.logs_dir, run_dir, f"{snap_idx:02d}_final",
                      SNAPSHOT_LOGS + EXTRA_FINAL_LOGS)

    summarize(run_dir, outcome, new_crashes)

    if new_crashes and not args.no_triage:
        if CRASH_TRIAGE.is_file():
            log("handing off to crash_triage.py ...")
            for name in sorted(new_crashes):
                subprocess.run([sys.executable, str(CRASH_TRIAGE),
                                "--crash-folder", str(args.crashes_dir / name),
                                "--lines", "20"])
        else:
            log(f"crash_triage.py not found at {CRASH_TRIAGE}; triage manually.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
