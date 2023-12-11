```bash
$ binwalk ***.zip 
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, encrypted at least v2.0 to extract, compressed size: 117, uncompressed size: 106, name: pass.txt
225           0xE1            End of Zip archive, footer length: 22
$ fcrackzip -D -u -p /usr/share/wordlists/rockyou.txt ***.zip
PASSWORD FOUND!!!!: pw == ***
```