#! /usr/bin/env python3
# coding: utf-8

key = 'FULL'
iKey = 0
pwd = ''
s = '\u000A\u0010L\u001C\u0007\u0006\u001FL\u0003\u0006\u0018L\u000A\u0014\u0002\u000B\u0013\u0014\u000B\u0009'
print('s:', s)
for i,c in enumerate(s):
    print('c', i, c, ord(c), key[iKey], ord(key[iKey]), ord(c) ^ ord(key[iKey]), chr(ord(c) ^ ord(key[iKey])) )
    pwd += chr(ord(c) ^ ord(key[iKey]))
    iKey += 1
    iKey = iKey % len(key)
print(pwd)
