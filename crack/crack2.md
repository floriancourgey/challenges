PE Studio 9.56
- tooling: `Visual Studio 6.0 MASM`
- libraries: `MSVBVM60.DLL`

VB Decompiler 12.2
- Startup: `Form1`
- Code -> Form1 -> Command1_Click_4020E0
```bash
loc_00402207: call [0040107Ch] ; __vbaVarAdd
loc_004021FD: mov var_48, edi
loc_00402200: mov var_7C, 00008008h
loc_00402207: call [0040107Ch] ; __vbaVarAdd
loc_0040220D: lea ecx, var_44
loc_00402210: push eax
loc_00402211: lea edx, var_6C
loc_00402214: push ecx
loc_00402215: push edx
loc_00402216: call [00401050h] ; __vbaVarMul
loc_0040221C: push eax
loc_0040221D: call [0040103Ch] ; __vbaVarTstEq
[...]
if flag == 0 ; loc_00402243: cmp bx, di
    loc_0040225C: push 00401994h ; "Password accepté, entrer ce pass pour valider sur le site"
else
    loc_00402285: push 00401A0Ch ; "Password refusé...Essaye encore !"
```
