#!/usr/bin/env python3
"""
SEH.generate_acceptance_reference.py

Reads the SEH (Species / Ethnos / Heritage) script and produces a human
readable Markdown reference of every country's acceptance levels, with the
raw numeric IDs resolved to their full localised names.

Sources (all relative to the mod root):
  common/on_actions/SEH.on_actions.txt              - startup wiring (provenance only)
  common/scripted_effects/SEH.scripted_effects.txt  - per-country accepted arrays
  common/scripted_effects/SEH.species_scripted_effects.txt   - state -> species ID
  common/scripted_effects/SEH.ethnos_scripted_effects.txt    - state -> ethnos ID
  common/scripted_effects/SEH.heritage_scripted_effects.txt  - state -> heritage ID
  localisation/english/**.yml                        - ID names + country names

Output:
  tools/SEH.acceptance_reference.md

The country acceptance data lives in the SEH_initialize_<region>_acceptance
blocks of SEH.scripted_effects.txt. Each block holds one sub-block per country
tag, containing lines of the form:

    add_to_array = { array = SEH_accepted_<category>_<full|partial> value = <ID> }

IDs are resolved through the var_SEH_<category>.<ID> keys in the localisation,
and country tags through their base "TAG:0" localisation key.
"""

import os
import re
import glob
from collections import defaultdict

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MOD_ROOT = os.path.dirname(SCRIPT_DIR)

SCRIPTED_EFFECTS = os.path.join(
    MOD_ROOT, "common", "scripted_effects", "SEH.scripted_effects.txt")
EFFECT_FILES = {
    "species": os.path.join(MOD_ROOT, "common", "scripted_effects",
                            "SEH.species_scripted_effects.txt"),
    "ethnos": os.path.join(MOD_ROOT, "common", "scripted_effects",
                           "SEH.ethnos_scripted_effects.txt"),
    "heritage": os.path.join(MOD_ROOT, "common", "scripted_effects",
                             "SEH.heritage_scripted_effects.txt"),
}
LOC_DIR = os.path.join(MOD_ROOT, "localisation", "english")
HISTORY_DIR = os.path.join(MOD_ROOT, "history", "countries")
OUTPUT_MD = os.path.join(SCRIPT_DIR, "SEH.acceptance_reference.md")

# Category display order + the var_ / array token used for each.
CATEGORIES = ["species", "ethnos", "heritage"]
CATEGORY_TITLE = {"species": "Species", "ethnos": "Ethnos", "heritage": "Heritage"}

# Region init blocks, in the order SEH_initialize_country_acceptance calls them.
REGION_ORDER = ["artemum", "bitu", "harmonainus", "harmoneema", "novusaiga", "tyenren"]
REGION_TITLE = {
    "artemum": "Artemum",
    "bitu": "Bitu",
    "harmonainus": "Harmonainus",
    "harmoneema": "Harmoneema",
    "novusaiga": "Novusaiga",
    "tyenren": "Tyenren",
}


# --------------------------------------------------------------------------
# Generic Paradox-script block parsing
# --------------------------------------------------------------------------
def _read(path):
    with open(path, "r", encoding="utf-8-sig") as fh:
        return fh.read()


def _skip_balanced(text, i):
    """Given text[i] == '{', return the index just past the matching '}'.

    Respects '#' line comments so braces inside comments are ignored.
    """
    depth = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == "#":
            while i < n and text[i] != "\n":
                i += 1
        elif c == "{":
            depth += 1
            i += 1
        elif c == "}":
            depth -= 1
            i += 1
            if depth == 0:
                return i
        else:
            i += 1
    return n  # unbalanced; treat rest of file as the block


def parse_top_blocks(text):
    """Return a list of (key, body) for every `KEY = { ... }` at the top level
    of `text`, in source order. Nested blocks are left untouched inside body."""
    blocks = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == "#":
            while i < n and text[i] != "\n":
                i += 1
            continue
        if c.isspace():
            i += 1
            continue
        if c == "{":
            i = _skip_balanced(text, i)
            continue
        # Read an identifier token.
        j = i
        while j < n and (text[j].isalnum() or text[j] in "_."):
            j += 1
        if j == i:
            i += 1
            continue
        token = text[i:j]
        # Look for `= {` after optional whitespace.
        k = j
        while k < n and text[k] in " \t\r\n":
            k += 1
        if k < n and text[k] == "=":
            k += 1
            while k < n and text[k] in " \t\r\n":
                k += 1
            if k < n and text[k] == "{":
                end = _skip_balanced(text, k)
                blocks.append((token, text[k + 1:end - 1]))
                i = end
                continue
        i = j
    return blocks


# --------------------------------------------------------------------------
# Localisation parsing
# --------------------------------------------------------------------------
LOC_LINE_RE = re.compile(r'^\s*([\w.\-]+):\d*\s+"(.*)"')


def parse_all_loc():
    """Parse every english .yml into a flat {key: value} dict.

    Later files do not override earlier non-empty values for the same key,
    which keeps purpose-built country files from being clobbered by generic
    fallbacks. $ref$ style references are resolved afterwards.
    """
    loc = {}
    for path in sorted(glob.glob(os.path.join(LOC_DIR, "**", "*.yml"), recursive=True)):
        try:
            text = _read(path)
        except OSError:
            continue
        for line in text.splitlines():
            stripped = line.lstrip()
            if not stripped or stripped.startswith("#"):
                continue
            m = LOC_LINE_RE.match(line)
            if not m:
                continue
            key, val = m.group(1), m.group(2)
            if key not in loc or (loc[key] == "" and val != ""):
                loc[key] = val
    _resolve_refs(loc)
    return loc


def _resolve_refs(loc):
    ref_re = re.compile(r"\$([\w.\-]+)\$")
    for key in list(loc.keys()):
        val = loc[key]
        if "$" not in val:
            continue
        # A couple of passes is plenty for the shallow references used here.
        for _ in range(5):
            new = ref_re.sub(lambda m: loc.get(m.group(1), m.group(0)), val)
            if new == val:
                break
            val = new
        loc[key] = val


def build_id_names(loc):
    """{category: {id: name}} from var_SEH_<category>.<id> base keys."""
    names = {c: {} for c in CATEGORIES}
    for cat in CATEGORIES:
        pat = re.compile(r"^var_SEH_" + cat + r"\.(\d+)$")
        for key, val in loc.items():
            m = pat.match(key)
            if m:
                names[cat][int(m.group(1))] = val
    return names


def parse_ruling_parties():
    """{TAG: ideology} from each history/countries file's set_politics block.

    History files are named `TAG - Name.txt`; the tag is the leading token.
    """
    ruling = {}
    party_re = re.compile(r"ruling_party\s*=\s*(\w+)")
    tag_re = re.compile(r"^([A-Z][A-Z0-9]{2})\b")
    for path in glob.glob(os.path.join(HISTORY_DIR, "*.txt")):
        m = tag_re.match(os.path.basename(path))
        if not m:
            continue
        try:
            text = _read(path)
        except OSError:
            continue
        pm = party_re.search(text)
        if pm:
            ruling[m.group(1)] = pm.group(1)
    return ruling


def build_country_names(loc, ruling_parties):
    """{TAG: name} using the localised name of the starting ruling government.

    Preference per country: the ideology-specific `TAG_<ideology>` name that
    matches its history set_politics, then the base `TAG` name, then the tag.
    """
    tag_re = re.compile(r"^[A-Z][A-Z0-9]{2}$")
    base = {k: v for k, v in loc.items() if tag_re.match(k) and v.strip()}
    names = {}
    for tag in set(base) | set(ruling_parties):
        ideology = ruling_parties.get(tag)
        gov = loc.get("{}_{}".format(tag, ideology)) if ideology else None
        if gov and gov.strip():
            names[tag] = gov
        elif base.get(tag):
            names[tag] = base[tag]
    return names


# --------------------------------------------------------------------------
# Acceptance data
# --------------------------------------------------------------------------
ADD_RE = re.compile(
    r"add_to_array\s*=\s*\{\s*array\s*=\s*SEH_accepted_(\w+?)_(full|partial)"
    r"\s+value\s*=\s*(-?\d+)\s*\}")


def parse_country_acceptance():
    """Return ordered {region: {TAG: {category: {'full': [ids], 'partial': [ids]}}}}."""
    text = _read(SCRIPTED_EFFECTS)
    top = dict(parse_top_blocks(text))

    regions = {}
    for region in REGION_ORDER:
        fn = "SEH_initialize_" + region + "_acceptance"
        body = top.get(fn)
        if body is None:
            continue
        countries = {}
        for tag, tag_body in parse_top_blocks(body):
            entry = {c: {"full": [], "partial": []} for c in CATEGORIES}
            for cat, level, value in ADD_RE.findall(tag_body):
                if cat in entry:
                    entry[cat][level].append(int(value))
            countries[tag] = entry
        regions[region] = countries
    return regions


STATE_SET_RE = {
    cat: re.compile(r"(\d+)\s*=\s*\{\s*set_variable\s*=\s*\{\s*SEH_" + cat + r"\s*=\s*(\d+)")
    for cat in CATEGORIES
}


def count_states_per_id():
    """{category: {id: number_of_states_with_that_majority}}."""
    counts = {c: defaultdict(int) for c in CATEGORIES}
    for cat, path in EFFECT_FILES.items():
        try:
            text = _read(path)
        except OSError:
            continue
        for _state_id, value in STATE_SET_RE[cat].findall(text):
            counts[cat][int(value)] += 1
    return counts


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------
def name_for_id(id_names, cat, value):
    name = id_names[cat].get(value)
    if name is None:
        return "`#{}` _(undefined)_".format(value)
    return "{} (`{}`)".format(name, value)


def render_id_list(id_names, cat, ids):
    if not ids:
        return "—"
    return ", ".join(name_for_id(id_names, cat, v) for v in ids)


def render_reference_tables(id_names, state_counts):
    lines = ["## ID reference tables", ""]
    for cat in CATEGORIES:
        lines.append("### {} IDs".format(CATEGORY_TITLE[cat]))
        lines.append("")
        lines.append("| ID | Name | States (majority) |")
        lines.append("|---:|------|------------------:|")
        ids = sorted(set(id_names[cat]) | set(state_counts[cat]))
        for i in ids:
            name = id_names[cat].get(i, "_(undefined)_")
            cnt = state_counts[cat].get(i, 0)
            lines.append("| {} | {} | {} |".format(i, name, cnt))
        lines.append("")
    return lines


def render_country_tables(regions, id_names, country_names):
    lines = ["## Country acceptance", ""]
    for region in REGION_ORDER:
        countries = regions.get(region)
        if not countries:
            continue
        lines.append("### {}".format(REGION_TITLE[region]))
        lines.append("")
        for tag in sorted(countries, key=lambda t: country_names.get(t, t).lower()):
            entry = countries[tag]
            display = country_names.get(tag, tag)
            heading = display if display == tag else "{} (`{}`)".format(display, tag)
            lines.append("#### {}".format(heading))
            lines.append("")
            lines.append("| Category | Full acceptance | Partial acceptance |")
            lines.append("|----------|-----------------|--------------------|")
            for cat in CATEGORIES:
                lines.append("| {} | {} | {} |".format(
                    CATEGORY_TITLE[cat],
                    render_id_list(id_names, cat, entry[cat]["full"]),
                    render_id_list(id_names, cat, entry[cat]["partial"]),
                ))
            lines.append("")
    return lines


def build_markdown(regions, id_names, country_names, state_counts):
    total = sum(len(c) for c in regions.values())
    lines = [
        "# SEH Acceptance Reference",
        "",
        "_Auto-generated by `tools/SEH.generate_acceptance_reference.py`._",
        "_Do not edit by hand; regenerate from the SEH scripts and localisation._",
        "",
        "This document lists every country's **Species / Ethnos / Heritage** "
        "acceptance levels, with the raw numeric IDs resolved to their full "
        "localised names.",
        "",
        "- **Full acceptance** — the group is fully accepted "
        "(`SEH_accepted_<category>_full`).",
        "- **Partial acceptance** — the group is partially accepted "
        "(`SEH_accepted_<category>_partial`).",
        "- A group not listed for a country is non-accepted by default.",
        "",
        "Source data: `common/scripted_effects/SEH.scripted_effects.txt` "
        "(`SEH_initialize_<region>_acceptance` blocks) and ID names from "
        "`localisation/english`. Each country is named after its **starting "
        "ruling government** — the `ruling_party` in its `history/countries` "
        "`set_politics` block, resolved to the `TAG_<ideology>` localisation "
        "key. State majority counts come from the "
        "`SEH.<category>_scripted_effects.txt` files.",
        "",
        "Countries documented: **{}** across **{}** regions.".format(
            total, len([r for r in REGION_ORDER if regions.get(r)])),
        "",
    ]
    lines += render_reference_tables(id_names, state_counts)
    lines += render_country_tables(regions, id_names, country_names)
    return "\n".join(lines).rstrip() + "\n"


def main():
    loc = parse_all_loc()
    id_names = build_id_names(loc)
    ruling_parties = parse_ruling_parties()
    country_names = build_country_names(loc, ruling_parties)
    regions = parse_country_acceptance()
    state_counts = count_states_per_id()

    md = build_markdown(regions, id_names, country_names, state_counts)
    with open(OUTPUT_MD, "w", encoding="utf-8") as fh:
        fh.write(md)

    total = sum(len(c) for c in regions.values())
    print("Wrote {}".format(OUTPUT_MD))
    print("  Countries: {}".format(total))
    for cat in CATEGORIES:
        print("  {} IDs named: {}".format(
            CATEGORY_TITLE[cat], len(id_names[cat])))

    # Flag acceptance IDs that have no localised name (likely data typos).
    missing = defaultdict(set)
    for countries in regions.values():
        for tag, entry in countries.items():
            for cat in CATEGORIES:
                for level in ("full", "partial"):
                    for v in entry[cat][level]:
                        if v not in id_names[cat]:
                            missing[cat].add((v, tag))
    for cat in CATEGORIES:
        if missing[cat]:
            items = ", ".join("{} ({})".format(v, t)
                              for v, t in sorted(missing[cat]))
            print("  WARNING undefined {} IDs used: {}".format(
                CATEGORY_TITLE[cat], items))


if __name__ == "__main__":
    main()
