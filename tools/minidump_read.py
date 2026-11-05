"""minidump_read.py <minidump.dmp>: faulting RIP as hoi4.exe offset, registers, code bytes, stack return-address candidates. No hoi4.exe symbols exist. Needs .global_tools/_vendor (pip install --target .global_tools/_vendor minidump)."""
import sys, struct, logging
logging.disable(logging.CRITICAL)
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "_vendor"))
from minidump.minidumpfile import MinidumpFile
m = MinidumpFile.parse(sys.argv[1])
ex = m.exception.exception_records[0]
exe = [x for x in m.modules.modules if x.name.lower().endswith("hoi4.exe")][0]
base, size = exe.baseaddress, exe.size
ctx = ex.ThreadContext if hasattr(ex,"ThreadContext") else None
print("fault:", ex.ExceptionRecord.ExceptionCode, hex(ex.ExceptionRecord.ExceptionAddress), [hex(x) for x in ex.ExceptionRecord.ExceptionInformation[:2]])
raw = open(sys.argv[1],"rb").read()[ctx.Rva:ctx.Rva+ctx.DataSize]
names = {"Rax":0x78,"Rcx":0x80,"Rdx":0x88,"Rbx":0x90,"Rsp":0x98,"Rbp":0xA0,"Rsi":0xA8,"Rdi":0xB0,"R8":0xB8,"R9":0xC0,"Rip":0xF8}
class C: pass
c = C()
for k,o in names.items(): setattr(c,k,struct.unpack_from("<Q",raw,o)[0])
print("RIP", hex(c.Rip), "off", hex(c.Rip-base), "RSP", hex(c.Rsp), "RAX", hex(c.Rax), "RCX", hex(c.Rcx), "RDX", hex(c.Rdx), "RBX", hex(c.Rbx), "RSI", hex(c.Rsi), "RDI", hex(c.Rdi), "R8", hex(c.R8))
r = m.get_reader().get_buffered_reader()
r.move(c.Rip-0x30); code = r.read(0x40); print("code:", code.hex())
r.move(c.Rsp)
try: stack = r.read(0x1800)
except Exception: stack = r.read(0x400)
fr=[]
for i in range(0, len(stack)-7, 8):
    v = struct.unpack_from("<Q", stack, i)[0]
    if base <= v < base+size: fr.append(hex(v-base))
print("hoi4 return-addr candidates:", " ".join(fr[:30]))
