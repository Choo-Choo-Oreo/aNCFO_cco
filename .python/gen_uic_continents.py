"""
Generator for the UIC Formable-Continents assets (sub-ideology tier).

Emits four text blobs from canonical repo data so the 215 cosmetic tags stay in
lockstep and are regenerable:
  * cosmetic colour blocks   -> paste into common/countries/cosmetic.txt
  * localisation name lines  -> paste into aNCFO.countries_cosmetic_l_english.yml
  * UIC effect chains        -> paste into UIC.scripted_effects.txt
  * UIC scripted triggers    -> written to UIC.scripted_triggers.txt

Colour = continent_base*0.55 + sub_ideology_colour*0.45 (sub colour taken from
its own `color` in 00_ideologies.txt, else the parent group's colour).
Name = "<continent prefix> <sub modifier> <continent group polity noun>", both
derived from the existing FORM_<C>_<group> / _ADJ loc. The group's "plain" sub
has an empty modifier so it reproduces the current group name verbatim.

HARMONEEMA omits sub_harmonainism / sub_radical_harmonainism (the
form_new_harmonainus_imperious formable already covers Harmonainist europe).

Run from the .python/ folder: `python gen_uic_continents.py`
"""

import re
from pathlib import Path

MOD = Path(__file__).resolve().parent.parent
IDEO = MOD / "common" / "ideologies" / "00_ideologies.txt"
COSMETIC = MOD / "common" / "countries" / "cosmetic.txt"
LOC = MOD / "localisation" / "english" / "aNCFO.countries_cosmetic_l_english.yml"
OUT = Path(__file__).resolve().parent / "_uic_continents_generated"

GROUP_ORDER = ["pluralism", "semidemocracy", "theocratism", "authoritarianism", "unitism"]

# Continent tag stem -> (FORM tag, loc group keys use the lowercase group names).
CONTINENTS = ["HARMONEEMA", "BITU", "ARTEMUM", "TYENREN", "FOUNDLANDS", "HEARTLANDS", "NOVUSAIGA"]

# Per-continent sub exclusions (handled by another formable).
EXCLUDE = {"HARMONEEMA": {"sub_harmonainism", "sub_radical_harmonainism"}}

# Sub-ideology -> short descriptor adjective inserted before the polity noun.
# "" = the group's plain sub, reproducing the existing group name exactly.
SUB_MODIFIER = {
    # pluralism
    "sub_illuminism": "Illumin", "sub_pluralism": "", "sub_constitutionalism": "Constitutional",
    "sub_conservatism": "Conservative", "sub_liberalism": "Liberal",
    "sub_progressivism": "Progressive", "sub_populism": "Populist",
    # semidemocracy
    "sub_obscurism": "Obscurant", "sub_transitional_democracy": "", "sub_traditionalism": "Traditionalist",
    "sub_mercantile_republicism": "Mercantile", "sub_socialism": "Socialist", "sub_illiberalism": "Illiberal",
    # theocratism
    "sub_radical_harmonainism": "Radical", "sub_harmonainism": "", "sub_reformed_harmonainism": "Reformed",
    "sub_pullusism": "Pullusian", "sub_thalassaus": "Thalassaus", "sub_ager_montis": "Ager-Montis",
    "sub_animaekin": "Animaekin", "sub_crownfather": "Crownfather",
    # authoritarianism
    "sub_monarchy": "Royal", "sub_authoritarian": "", "sub_stratocracy": "Martial",
    "sub_auth_harmonainism": "Harmonainist", "sub_oligarchy": "Oligarchic",
    # unitism
    "sub_ultra_nationalism": "Ultranationalist", "sub_national_unitism": "National", "sub_unitism": "",
    "sub_syndicalism": "Syndicalist", "sub_fascism": "Fascist", "sub_harmonization": "Harmonized",
}


def parse_ideologies():
    """Return (sub_group, sub_color) with sub colour inheriting the group's when
    the sub has no explicit color = { } of its own."""
    text = IDEO.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    sub_group, sub_color, sub_order = {}, {}, []
    group = None
    group_color = {}
    in_types = False
    cur_sub = None
    for line in text:
        s = line.strip()
        # group header: one tab of indent, "<name> = {"
        m = re.match(r"^\t([a-z_]+) = \{", line)
        if m and m.group(1) in GROUP_ORDER:
            group = m.group(1)
            in_types = False
            cur_sub = None
            continue
        if group and re.match(r"^\t\ttypes = \{", line):
            in_types = True
            continue
        if in_types:
            ms = re.match(r"^\t\t\t(sub_[a-z_]+) = \{", line)
            if ms:
                cur_sub = ms.group(1)
                sub_group[cur_sub] = group
                sub_order.append(cur_sub)
                continue
            if cur_sub:
                mc = re.match(r"^\s*color = \{\s*(\d+)\s+(\d+)\s+(\d+)\s*\}", line)
                if mc:
                    sub_color[cur_sub] = tuple(int(x) for x in mc.groups())
            if re.match(r"^\t\t\}", line):  # end of types block
                in_types = False
                cur_sub = None
                continue
        # group-level color (indent 2, after types)
        if group and not in_types:
            mgc = re.match(r"^\t\tcolor = \{\s*(\d+)\s+(\d+)\s+(\d+)\s*\}", line)
            if mgc:
                group_color[group] = tuple(int(x) for x in mgc.groups())
    for sub, grp in sub_group.items():
        sub_color.setdefault(sub, group_color[grp])
    return sub_group, sub_color, sub_order


def parse_base_colors():
    text = COSMETIC.read_text(encoding="utf-8", errors="replace")
    out = {}
    for c in CONTINENTS:
        m = re.search(rf"^FORM_{c} = \{{\s*color = rgb \{{\s*(\d+)\s+(\d+)\s+(\d+)\s*\}}",
                      text, re.MULTILINE)
        out[c] = tuple(int(x) for x in m.groups())
    return out


def parse_loc():
    """Return per continent: adjective, prefix (first word of group names), and
    polity noun per group (group name minus that first word)."""
    text = LOC.read_text(encoding="utf-8-sig", errors="replace")
    adj, prefix, polity = {}, {}, {}
    for c in CONTINENTS:
        ma = re.search(rf'^\s*FORM_{c}_ADJ:\s*"([^"]*)"', text, re.MULTILINE)
        adj[c] = ma.group(1)
        polity[c] = {}
        first_word = None
        for g in GROUP_ORDER:
            mg = re.search(rf'^\s*FORM_{c}_{g}:\s*"([^"]*)"', text, re.MULTILINE)
            name = mg.group(1)
            head, rest = name.split(" ", 1)
            polity[c][g] = rest
            first_word = head
        prefix[c] = first_word
    return adj, prefix, polity


def blend(base, sub, w=0.45):
    return tuple(max(0, min(255, round(base[i] * (1 - w) + sub[i] * w))) for i in range(3))


def main():
    sub_group, sub_color, sub_order = parse_ideologies()
    base = parse_base_colors()
    adj, prefix, polity = parse_loc()

    OUT.mkdir(exist_ok=True)
    cos, loc, eff = [], [], []
    trig_lines = {}
    tag_count = 0

    for c in CONTINENTS:
        eff.append(f"\t# --- {c} ---")
        first = True
        trig_tags = [f"FORM_{c}"]
        for sub in sub_order:  # canonical group/sub order
            if sub in EXCLUDE.get(c, set()):
                continue
            grp = sub_group[sub]
            tag = f"UIC_FORM_{c}_ideocos_{sub}"
            trig_tags.append(tag)
            # colour
            r, g, b = blend(base[c], sub_color[sub])
            cos.append(f"{tag} = {{\n\tcolor = rgb {{ {r} {g} {b} }}\n\tcolor_ui = rgb {{ {r} {g} {b} }}\n}}")
            # name
            mod = SUB_MODIFIER[sub]
            name = f"{prefix[c]} {mod + ' ' if mod else ''}{polity[c][grp]}"
            loc.append(f'  {tag}: "{name}"')
            loc.append(f'  {tag}_DEF: "the {name}"')
            loc.append(f'  {tag}_ADJ: "{adj[c]}"')
            # effect branch
            kw = "IF" if first else "ELSE_IF"
            first = False
            eff.append(
                f"\t{kw} = {{\n\t\tlimit = {{ ROOT = {{ has_country_leader_ideology = {sub} "
                f"UIC_is_{c.lower()}_formed = yes }} }}\n\t\tset_cosmetic_tag = {tag}\n\t}}"
            )
            tag_count += 1
        trig_lines[c] = trig_tags
        eff.append("")

    # triggers
    trig = ["# Unique Ideology Cosmetic (UIC) -- Formable Continent 'already formed' checks.",
            "# Each ORs the FORM_<C> marker with every UIC sub-ideology tier tag, so the",
            "# formable's re-form guard AND the UIC swap logic share one tag list.", ""]
    for c in CONTINENTS:
        trig.append(f"UIC_is_{c.lower()}_formed = {{")
        trig.append("\tOR = {")
        for t in trig_lines[c]:
            trig.append(f"\t\thas_cosmetic_tag = {t}")
        trig.append("\t}")
        trig.append("}")
        trig.append("")

    (OUT / "cosmetic_blocks.txt").write_text("\n\n".join(cos) + "\n", encoding="utf-8")
    (OUT / "loc_lines.yml").write_text("\n".join(loc) + "\n", encoding="utf-8-sig")
    (OUT / "effect_blocks.txt").write_text("\n".join(eff), encoding="utf-8")
    (OUT / "triggers.txt").write_text("\n".join(trig), encoding="utf-8")

    print(f"continents: {len(CONTINENTS)}  sub-ideologies: {len(sub_order)}")
    print(f"generated tags: {tag_count} (expect 222 = 6*32 + 30)")
    print(f"loc lines: {len(loc)} (expect {tag_count*3})")
    print(f"output dir: {OUT}")


if __name__ == "__main__":
    main()
