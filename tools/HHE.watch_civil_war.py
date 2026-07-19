#!/usr/bin/env python3
"""HHE.watch_civil_war.py -- live-tail game.log for HHE civil-war milestones.

Watches the debug trails written by common/on_actions/aNCFO.debug_on_actions.txt
(daily capital line, monthly civil-war-stage line, monthly crusade-focus-path
line, monthly MRC-war line) and prints each MILESTONE the moment it appears:

  - capital (state 5) lost / recovered            (daily granularity)
  - civil-war stage transitions                    (local -> regional -> full -> WON)
  - crusade focus-path milestones                  (great_victory_parades ->
                                                    trilateral_preparations ->
                                                    trilateral_crusade)
  - first war with MRC / HHE capitulation

Repeated identical stage lines are deduped -- only CHANGES print, so a multi-
hour soak run produces a short, readable timeline instead of a monthly spam.

Supersedes HHE.watch_civil_war_capital.py (capital-only watcher).

Usage:
    python tools/HHE.watch_civil_war.py
    python tools/HHE.watch_civil_war.py --from-start     # replay a finished run's log
    python tools/HHE.watch_civil_war.py --logs-dir PATH --poll 2
"""
from __future__ import annotations

import argparse
import time
from datetime import datetime
from pathlib import Path

DOCS = Path.home() / "Documents" / "Paradox Interactive" / "Hearts of Iron IV"
DEFAULT_LOGS_DIR = DOCS / "logs"

HELD_MARKER = "HHE capital (state 5) held"
LOST_MARKER = "HHE capital (state 5) LOST"
STAGE_MARKER = "CW stage:"
FOCUS_MARKER = "focus path:"
FORM_MARKER = "formable race:"
CRISIS_MARKER = "collapse crisis"
CHAIN_MARKER = "chain next:"
GATE_MARKER = "chain gate:"
ECON_MARKER = "crisis economy:"
ECON_EXACT_MARKER = "crisis economy exact:"
BOP_MARKER = "civil-war BoP band:"
GOAL_MARKER = "secondary goal:"
PLAYER_MARKER = "player track:"
MRC_WAR_MARKER = "at war with MRC"
MRC_CAP_MARKER = "at war with MRC, HHE has capitulated"


def now() -> str:
    return datetime.now().strftime("%H:%M:%S")


def log(msg: str) -> None:
    print(f"[{now()}] {msg}", flush=True)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Live-tail game.log for HHE civil-war stage transitions, "
                    "crusade focus milestones, capital loss, and the first MRC war.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--logs-dir", type=Path, default=DEFAULT_LOGS_DIR,
                   help="Live HOI4 logs directory containing game.log.")
    p.add_argument("--poll", type=float, default=3.0,
                   help="Seconds between reads of new log content.")
    p.add_argument("--from-start", action="store_true",
                   help="Scan game.log from the beginning instead of only new "
                        "lines (use to replay an already-finished run's log).")
    return p


def extract_payload(line: str, marker: str) -> str:
    """Return the message from the marker onward, stripped of log prefixes."""
    idx = line.find(marker)
    return line[idx:].strip() if idx >= 0 else line.strip()


class State:
    """Deduped milestone state; reset on each new hoi4 launch."""

    def __init__(self) -> None:
        self.capital_held: bool | None = None
        self.last_stage: str | None = None
        self.last_focus: str | None = None
        self.seen_payloads: set[str] = set()  # formable-race / collapse-crisis dedupe
        self.mrc_war_seen = False
        self.capitulation_seen = False


def handle_line(line: str, st: State) -> None:
    if LOST_MARKER in line:
        if st.capital_held is not False:
            log(f"MILESTONE capital LOST: {line.strip()}")
        st.capital_held = False
    elif HELD_MARKER in line:
        if st.capital_held is False:
            log(f"MILESTONE capital recovered: {line.strip()}")
        st.capital_held = True
    elif STAGE_MARKER in line:
        payload = extract_payload(line, STAGE_MARKER)
        if payload != st.last_stage:
            log(f"MILESTONE {line.strip()}")
            st.last_stage = payload
    elif FOCUS_MARKER in line:
        payload = extract_payload(line, FOCUS_MARKER)
        if payload != st.last_focus:
            log(f"MILESTONE {line.strip()}")
            st.last_focus = payload
    elif (FORM_MARKER in line or CRISIS_MARKER in line
          or CHAIN_MARKER in line or GATE_MARKER in line
          or ECON_MARKER in line or ECON_EXACT_MARKER in line
          or BOP_MARKER in line or GOAL_MARKER in line
          or PLAYER_MARKER in line):
        # ECON_EXACT / PLAYER lines carry live numbers that change constantly, so
        # echo them every time rather than deduping on payload.
        always = ECON_EXACT_MARKER in line or PLAYER_MARKER in line
        for marker in (ECON_EXACT_MARKER, FORM_MARKER, CRISIS_MARKER,
                       CHAIN_MARKER, GATE_MARKER, ECON_MARKER, BOP_MARKER,
                       GOAL_MARKER, PLAYER_MARKER):
            if marker in line:
                break
        payload = extract_payload(line, marker)
        if always:
            log(f"MILESTONE {line.strip()}")
            return
        if payload not in st.seen_payloads:
            log(f"MILESTONE {line.strip()}")
            st.seen_payloads.add(payload)
    elif MRC_CAP_MARKER in line:
        if not st.capitulation_seen:
            log(f"MILESTONE HHE CAPITULATED in MRC war: {line.strip()}")
            st.capitulation_seen = True
    elif MRC_WAR_MARKER in line and "not yet" not in line:
        if not st.mrc_war_seen:
            log(f"MILESTONE first MRC war: {line.strip()}")
            st.mrc_war_seen = True


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    game_log = args.logs_dir / "game.log"

    if not args.from_start:
        log(f"waiting for {game_log} to exist ...")
        while not game_log.is_file():
            time.sleep(args.poll)
        log("watching for new lines (use --from-start to replay from the "
            "beginning instead)")

    st = State()
    pos = 0 if args.from_start else (game_log.stat().st_size
                                     if game_log.is_file() else 0)

    try:
        while True:
            if not game_log.is_file():
                time.sleep(args.poll)
                continue

            size = game_log.stat().st_size
            if size < pos:
                # Logs are overwritten at each hoi4 launch (CLAUDE.md); a
                # shrink means a fresh run started, so restart from the top.
                log("game.log shrank (new hoi4 launch) -- restarting scan")
                pos = 0
                st = State()

            if size > pos:
                with game_log.open("r", encoding="utf-8", errors="replace") as f:
                    f.seek(pos)
                    chunk = f.read()
                    pos = f.tell()
                for line in chunk.splitlines():
                    handle_line(line, st)

            if args.from_start:
                # Replay mode: one pass over current content, then exit.
                return 0
            time.sleep(args.poll)
    except KeyboardInterrupt:
        log("stopped by user (Ctrl+C)")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
