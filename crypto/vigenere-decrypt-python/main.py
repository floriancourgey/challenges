#! /usr/bin/env python3
# coding: utf-8

a = 'XEUGHQQPIKGRQSBUCVRFMMF'
b = 'LEMOTDEPASSEEST'
for i, l in enumerate(a[:len(b)]):
    mi = ord('A')
    decoded = ( (ord(l)-mi) - (ord(b[i])-mi) ) % 26
    print(l, ord(l)-mi, ' - ', b[i], ord(b[i])-mi, ' - ', decoded, decoded+mi, chr(decoded+mi))
