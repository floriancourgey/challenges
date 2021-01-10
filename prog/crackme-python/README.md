1. Unix file info
```bash
$ file crackeme.exe
crackeme.exe: PE32 executable (console) Intel 80386 (stripped to external PDB), for MS Windows
```
2. Radare2 file info
```bash
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
```

3. Open main (0x00401290):
```bash
/ (fcn) main 193
|   main (int argc, char **argv, char **envp);
|           ; var int local_1ch @ ebp-0x1c
|           ; var int local_18h @ ebp-0x18
|           ; var int local_17h @ ebp-0x17
|           ; var int local_16h @ ebp-0x16
|           ; var int local_15h @ ebp-0x15
|           ; var int local_14h @ ebp-0x14
|           ; var int local_13h @ ebp-0x13
|           ; var int local_12h @ ebp-0x12
|           ; var int local_11h @ ebp-0x11
|           ; var int local_10h @ ebp-0x10
|           ; var int local_fh @ ebp-0xf
|           ; var int local_eh @ ebp-0xe
|           ; var int local_4h_2 @ ebp-0x4
|           ; arg signed int arg_8h @ ebp+0x8
|           ; arg char **s1 @ ebp+0xc
|           ; var char **s2 @ esp+0x4
|           0x00401290      push ebp
|           0x00401291      mov  ebp, esp
|           0x00401293      push edi
|           0x00401294      sub  esp, 0x34 ; '4'
|           0x00401297      and  esp, 0xfffffff0
|           0x0040129a      mov  eax, 0
|           0x0040129f      add  eax, 0xf
|           0x004012a2      add  eax, 0xf
|           0x004012a5      shr  eax, 4
|           0x004012a8      shl  eax, 4
|           0x004012ab      mov  dword [local_1ch], eax
|           0x004012ae      mov  eax, dword [local_1ch]
|           0x004012b1      call fcn.004017a0 ; sym.___w32_sharedptr_initialize+0x240
|           0x004012b6      call sym.___main
|           0x004012bb      movzx eax, byte [0x403000] ; section..rdata ; [0x403000:1]=0
|           0x004012c2      mov  byte [local_18h], al
|           0x004012c5      lea  edi, [local_17h]
|           0x004012c8      cld
|           0x004012c9      mov ecx, 0xa
|           0x004012ce      mov al, 0
|           0x004012d0      rep stosb byte es:[edi], al
|           0x004012d2      mov byte [local_12h], 0x6a ; 'j' ; 106
|           0x004012d6      mov byte [local_16h], 0x6b ; 'k' ; 107
|           0x004012da      mov byte [local_14h], 0x6a ; 'j' ; 106
|           0x004012de      mov byte [local_17h], 0x62 ; 'b' ; 98
|           0x004012e2      mov byte [local_10h], 0x69 ; 'i' ; 105
|           0x004012e6      mov byte [local_15h], 0x63 ; 'c' ; 99
|           0x004012ea      mov byte [local_11h], 0x6b ; 'k' ; 107
|           0x004012ee      mov byte [local_13h], 0x6c ; 'l' ; 108
|           0x004012f2      mov byte [local_fh], 0x69 ; 'i' ; 105
|           0x004012f6      mov byte [local_18h], 0x68 ; 'h' ; 104
|           0x004012fa      mov byte [local_eh], 0
|           0x004012fe      cmp dword [arg_8h], 1 ; [0x1:4]=-1 ; 1
|       ,=< 0x00401302      jg 0x401312
|       |   0x00401304      mov dword [esp], str.Usage_:_crackmefast.exe_pass ; [0x40300b:4]=0x67617355 ; "Usage : crackmefast.exe pass\n" ; const char *format
|       |   0x0040130b      call sym._printf ; int printf(const char *format)
|      ,==< 0x00401310      jmp 0x401347
|      |`-> 0x00401312      lea eax, [local_18h]
|      |    0x00401315      mov edx, dword [s1] ; [0xc:4]=-1 ; 12
|      |    0x00401318      add edx, 4
|      |    0x0040131b      mov dword [s2], eax ; const char *s2
|      |    0x0040131f      mov eax, dword [edx]
|      |    0x00401321      mov dword [esp], eax ; const char *s1
|      |    0x00401324      call sym._strcmp ; int strcmp(const char *s1, const char *s2)
|      |    0x00401329      test eax, eax
|      |,=< 0x0040132b      jne 0x40133b
|      ||   0x0040132d      mov dword [esp], str.Bravo___Validez_votre_reponse_sous_la_forme_http:__p_reponse__pass ; [0x40302c:4]=0x76617242 ; "Bravo ! Validez votre reponse sous la forme http://?reponse=<pass> !\n" ; const char *format
|      ||   0x00401334      call sym._printf ; int printf(const char *format)
|     ,===< 0x00401339      jmp 0x401347
|     ||`-> 0x0040133b      mov dword [esp], str.Rate__dommage___Retente_ta_chance ; [0x4030a4:4]=0x65746152 ; "Rate, dommage ! Retente ta chance !\n" ; const char *format
|     ||    0x00401342      call sym._printf ; int printf(const char *format)
|     ``--> 0x00401347      mov eax, 0
|           0x0040134c      mov edi, dword [local_4h_2]
|           0x0040134f      leave
\           0x00401350      ret
```

4. Get another executable and compare to find the dynamic part:
![Screenshot of dynamic parts in the EXE file](https://raw.githubusercontent.com/floriancourgey/challenges/master/prog/crackme-python/screenshot-text-diff.jpg)
=> Looks like a string generator with 10 chars only lowercase (a-z)

5. A char array of length=10 is filled with random letters and index, from address 0x004012d2 to 0x004012f6. The exe is using little endian order, so first characters come at a lesser address. And as it is a stack, it needs to be reverted.

6. radare2 can output n disassembled instructions with `pi n @ address`, so we will use `pi 10 @ 0x004012d2`.
