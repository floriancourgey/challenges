```bash
# check ASLR is off
$ cat /proc/sys/kernel/randomize_va_space
0
# check (E)xecutable stack
$ readelf -l bin01a
GNU_STACK      0x000000 0x00000000 0x00000000 0x00000 0x00000 RW  0x4
