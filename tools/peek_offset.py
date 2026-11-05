#!/usr/bin/env python3
"""Disassemble the code around "module+0xOFFSET" crash locations in a Windows exe/dll.

Usage:
    python peek_offset.py hoi4.exe 0x1070ce6 0x122bbcc 0x12283ab
    python peek_offset.py game.exe 1070ce6 --after 60 --before 80

Needs:  pip install pefile capstone

Crash reports such as "hoi4.exe+0x1070ce6" give an offset from the start of the loaded module (an RVA).
This tool maps it into the file, backs up to a real instruction boundary (x86 instructions vary in
length, so starting at a random byte gives garbage), and marks the crashing instruction.

It prints the section the offset falls in and the address as Ghidra/IDA show it (ImageBase + RVA), so you
can jump to the same spot in a disassembler. Read-only: it never modifies the file.

Caveats: the offsets only mean something for the exact build that produced the crash. If the code looks
like nonsense, the exe is probably a different version. Whether a register was null is inferred from the
code, not observed; confirm with the exception address from the crash dump.
"""
import argparse
import sys

import pefile
from capstone import CS_ARCH_X86, CS_MODE_32, CS_MODE_64, Cs


def section_of(pe, rva):
    for s in pe.sections:
        start = s.VirtualAddress
        if start <= rva < start + max(s.Misc_VirtualSize, s.SizeOfRawData):
            return s.Name.rstrip(b"\0").decode(errors="replace"), s.Characteristics
    return None, 0


def disasm_around(pe, md, image, rva, before, after):
    """Return the instruction list from the earliest start in [rva-before, rva) that lands exactly on rva."""
    base = pe.OPTIONAL_HEADER.ImageBase
    target = base + rva
    for back in range(before, 0, -1):
        start = rva - back
        if start < 0:
            continue
        ins = list(md.disasm(image[start:rva + after], base + start))
        if any(i.address == target for i in ins):
            return ins, target
    return [], target


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("exe", help="path to the exe/dll that crashed")
    ap.add_argument("offsets", nargs="+", help="module offsets (hex), e.g. 0x1070ce6")
    ap.add_argument("--before", type=int, default=64, help="max bytes to search back for a start boundary (default 64)")
    ap.add_argument("--after", type=int, default=40, help="bytes to disassemble after the crash (default 40)")
    args = ap.parse_args()

    pe = pefile.PE(args.exe)
    is64 = pe.OPTIONAL_HEADER.Magic == 0x20B
    md = Cs(CS_ARCH_X86, CS_MODE_64 if is64 else CS_MODE_32)
    image = pe.get_memory_mapped_image()
    base = pe.OPTIONAL_HEADER.ImageBase
    print(f"{args.exe}: {'x64' if is64 else 'x86'}  ImageBase {base:#x}  TimeDateStamp {pe.FILE_HEADER.TimeDateStamp:#x}")

    for text in args.offsets:
        rva = int(text, 16)
        name, flags = section_of(pe, rva)
        print(f"\n=== +{rva:#x}  ->  address {base + rva:#x}  section {name}")
        if name is None:
            print("  not inside any section: wrong module or wrong build?")
            continue
        if not flags & 0x20000000:  # IMAGE_SCN_MEM_EXECUTE
            print("  section is not executable: this offset is data, not code (wrong module or build?)")
            continue
        ins, target = disasm_around(pe, md, image, rva, args.before, args.after)
        if not ins:
            print("  could not find an instruction boundary at this offset: likely the wrong build")
            continue
        for i in ins:
            mark = "   <== CRASH" if i.address == target else ""
            print(f"  {i.address:x}  {i.mnemonic:6} {i.op_str}{mark}")


if __name__ == "__main__":
    sys.exit(main())
