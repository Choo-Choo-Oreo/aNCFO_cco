"""override_audit.py [--mod MOD] [--vanilla DIR] [--area common]

A mod file with the same relative path as a vanilla file REPLACES it. List top-level
definitions (depth-0 keys) that vanilla's file defines and the mod's version no longer
does, unless another file in the mod's same folder defines that key.
Replaced folders (replace_path) are skipped: nothing is inherited there anyway.
"""
import argparse, re, sys
from pathlib import Path

def top_keys(text):
    keys, depth, i, n = set(), 0, 0, len(text)
    tok = re.compile(r'[A-Za-z_@][\w.:@\-]*')
    while i < n:
        c = text[i]
        if c == '#':
            while i < n and text[i] != '\n': i += 1
        elif c == '"':
            i += 1
            while i < n and text[i] != '"': i += 1
            i += 1
        elif c == '{': depth += 1; i += 1
        elif c == '}': depth -= 1; i += 1
        elif depth == 0 and (c.isalpha() or c in '_@'):
            m = tok.match(text, i); keys.add(m.group(0)); i = m.end()
            # skip the rest of "key = value" simple values
        else: i += 1
    return keys

def read(p): return p.read_text(encoding="utf-8-sig", errors="replace")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mod", default="New-Horizons")
    ap.add_argument("--vanilla", default=r"D:\Program Files\SteamLibrary\steamapps\common\Hearts of Iron IV")
    ap.add_argument("--area", default="common")
    a = ap.parse_args()
    mod, van = Path(a.mod).resolve(), Path(a.vanilla)
    desc = read(mod / "descriptor.mod")
    replaced = [p.strip("/") for p in re.findall(r'replace_path\s*=\s*"([^"]+)"', desc)]
    total = 0
    for mf in sorted((mod / a.area).rglob("*.txt")):
        rel = mf.relative_to(mod).as_posix()
        if any(rel.startswith(r + "/") for r in replaced): continue
        vf = van / rel
        if not vf.is_file(): continue
        vk, mk = top_keys(read(vf)), top_keys(read(mf))
        lost = vk - mk
        if not lost: continue
        others = set()
        for of in mf.parent.glob("*.txt"):
            if of != mf: others |= top_keys(read(of))
        real = sorted(lost - others)
        if real:
            total += 1
            print(f"{rel}: vanilla={len(vk)} mod={len(mk)} LOST {len(real)}: {' '.join(real[:25])}{' ...' if len(real)>25 else ''}")
    print(f"\n{total} overriding files lost definitions")
main()
