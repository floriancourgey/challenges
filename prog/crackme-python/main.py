#! /usr/bin/env python3
# coding: utf-8
# import re
import sys
sys.path.insert(0, '../..')
from config import *
from datetime import datetime
import requests
import r2pipe
import re

urlProblem = URLS['prog']['crackme']['problem']
urlSolution = URLS['prog']['crackme']['solution']
print('Downloading crackme')
r = requests.get(urlProblem, cookies=COOKIE_DICT)
filename = './crackme.exe'+datetime.now().strftime('-%Y%m%d-%H%M%S.exe')
print('Saving as '+filename)

with open(filename, "wb") as local_file:
    local_file.write(r.content)

password = ''
# filename = 'crackme.exe-20210110-183417.exe'
# open file with r2
r = r2pipe.open(filename)
r2cmd = 'pi 10 @ 0x004012d2'
# parse output and store it into a dict {i: val,}
lines = r.cmd(r2cmd)
characters = {}
for line in lines.split('\n')[:-1]:
  print('- '+line)
  match = re.search('ebp - 0x(.+)], 0x(.+)', line)
  key = int(match.group(1), 16)
  value = bytearray.fromhex(match.group(2)).decode()
  print('key '+str(key)+', value '+value)
  characters[key] = value

for value in (characters[i] for i in sorted(characters, reverse=True)):
  password += value

print('PASSWORD: '+password)

url = urlSolution.replace('REPONSE', password)
print('calling: '+url)
r = requests.get(url, cookies=COOKIE_DICT)
print(r.content)
print((r.content).decode('utf-8'))
