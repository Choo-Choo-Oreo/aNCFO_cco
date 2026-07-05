"""
Splice the generated UIC Formable-Continents assets into the game files.
Idempotent: re-running detects already-applied sections and skips them.
Run from .python/ AFTER gen_uic_continents.py.
"""

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MOD = HERE.parent
G = HERE / "_uic_continents_generated"

COSMETIC = MOD / "common" / "countries" / "cosmetic.txt"
LOC = MOD / "localisation" / "english" / "aNCFO.countries_cosmetic_l_english.yml"
EFFECTS = MOD / "common" / "scripted_effects" / "UIC.scripted_effects.txt"
TRIGGERS = MOD / "common" / "scripted_triggers" / "UIC.scripted_triggers.txt"
DECISIONS = MOD / "common" / "decisions" / "formable_nation_decisions.txt"
CATEGORIES = MOD / "common" / "decisions" / "categories" / "00_formable_categories.txt"

CONTINENTS = ["HARMONEEMA", "BITU", "ARTEMUM", "TYENREN", "FOUNDLANDS", "HEARTLANDS", "NOVUSAIGA"]

cos_blocks = (G / "cosmetic_blocks.txt").read_text(encoding="utf-8").rstrip() + "\n"
loc_lines = (G / "loc_lines.yml").read_text(encoding="utf-8-sig").rstrip("\n")
eff_blocks = (G / "effect_blocks.txt").read_text(encoding="utf-8").rstrip("\n")
trig_body = (G / "triggers.txt").read_text(encoding="utf-8").rstrip("\n") + "\n"

log = []

# 1. Trigger file (new; always regenerate from generator output).
TRIGGERS.write_text(trig_body, encoding="utf-8")
log.append(f"wrote {TRIGGERS.name}")

# 2. cosmetic.txt -- append a UIC Formable Continents section.
txt = COSMETIC.read_text(encoding="utf-8")
if "# UIC Formable Continents" not in txt:
    txt = txt.rstrip() + "\n\n# UIC Formable Continents\n" + cos_blocks
    COSMETIC.write_text(txt, encoding="utf-8")
    log.append("cosmetic.txt: appended 222 colour blocks")
else:
    log.append("cosmetic.txt: already applied, skipped")

# 3. loc -- insert after the existing Formable Continents block.
txt = LOC.read_text(encoding="utf-8-sig")
if "UIC_FORM_HARMONEEMA_ideocos_sub_illuminism:" not in txt:
    anchor = '  FORM_NOVUSAIGA_unitism_DEF: "the Novusaigan Peoples Union"\n'
    assert anchor in txt, "loc anchor not found"
    block = anchor + "\n  # UIC Formable Continents (sub-ideology colour tiers)\n" + loc_lines + "\n"
    txt = txt.replace(anchor, block, 1)
    LOC.write_text(txt, encoding="utf-8-sig")
    log.append("loc: inserted 666 lines")
else:
    log.append("loc: already applied, skipped")

# 4. scripted_effects -- insert before the final closing brace of aNCFO_uic_effects.
txt = EFFECTS.read_text(encoding="utf-8")
if "# === Formable Continents ===" not in txt:
    idx = txt.rstrip().rfind("}")
    assert idx != -1, "no closing brace found in effects"
    insert = "\n\t# === Formable Continents ===\n" + eff_blocks + "\n"
    txt = txt[:idx] + insert + txt[idx:]
    EFFECTS.write_text(txt, encoding="utf-8")
    log.append("scripted_effects: inserted 7 continent chains")
else:
    log.append("scripted_effects: already applied, skipped")

# 5. decisions -- add aNCFO_uic_effects = yes after each set_cosmetic_tag = FORM_X.
txt = DECISIONS.read_text(encoding="utf-8")
added = 0
for c in CONTINENTS:
    # match the set line with its leading indentation, only if the call isn't already next.
    pat = re.compile(rf"([ \t]*)set_cosmetic_tag = FORM_{c}\n(?!\s*aNCFO_uic_effects = yes)")
    def repl(m):
        global added
        added += 1
        ind = m.group(1)
        return f"{ind}set_cosmetic_tag = FORM_{c}\n{ind}aNCFO_uic_effects = yes\n"
    txt = pat.sub(repl, txt)
DECISIONS.write_text(txt, encoding="utf-8")
log.append(f"decisions: added {added} aNCFO_uic_effects calls")

# 6. categories -- swap the re-form guard to the shared trigger.
txt = CATEGORIES.read_text(encoding="utf-8")
swaps = 0
for c in CONTINENTS:
    old = f"NOT = {{ has_cosmetic_tag = FORM_{c} }}"
    new = f"NOT = {{ UIC_is_{c.lower()}_formed = yes }}"
    n = txt.count(old)
    txt = txt.replace(old, new)
    swaps += n
CATEGORIES.write_text(txt, encoding="utf-8")
log.append(f"categories: swapped {swaps} guards")

print("\n".join(log))
