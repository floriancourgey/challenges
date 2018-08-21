$ file crackeme.exe
crackeme.exe: PE32 executable (console) Intel 80386 (stripped to external PDB), for MS Windows
$ rabin2 -I crackeme.exe
arch     x86
binsz    15508
bintype  pe
bits     32
canary   false
class    PE32
cmp.csum 0x0000dc08
compiled Fri Jul  2 22:26:17 2010
crypto   false
endian   little
havecode true
hdr.csum 0x0000aa08
linenum  true
lsyms    false
machine  i386
maxopsz  16
minopsz  1
nx       false
os       windows
overlay  true
pcalign  0
pic      false
relocs   true
signed   false
static   false
stripped false
subsys   Windows CUI
va       true

=> Windows x32 PE file (.exe)
