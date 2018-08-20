#! /usr/bin/env python3
# coding: utf-8
import config
import re
import time
import requests
from classes.square import Square
from classes.piece import Piece
from classes.bishop import Bishop
from classes.knight import Knight
from classes.rook import Rook
from classes.pawn import Pawn
from classes.queen import Queen
from classes.king import King
from levels.level_1 import Level_1
from levels.level_2 import Level_2
from levels.level_3 import Level_3

# coordinates start in bottom-left corner from (0,0) to (7,7)
# we are white (bottom A-H 0-1)
# target is black (top A-H 6-7)
# code is be 0-indexed but toString version is 1-indexed and uses letters for abscissas

def callNC(url):
    print('Calling URL:', url)
    r = requests.get(url, cookies={'SMFCookie89':config.COOKIE})
    return r.text

def createFromString(s):
    s = s.lower().replace(' ', '')
    if s == "pion": return Pawn()
    if s == "cavalier": return Knight()
    if s == "fou": return Bishop()
    if s == "tour": return Rook()
    if s == "dame": return Queen()

l1url = URL
l1regex = re.compile('; en ([A-H][1-8])\..+<br\/>(\w+)<br')
l2regex = re.compile('en ([A-H][1-8]) tout en.+>(\w+)<br\/><\/p>')
l3regex = re.compile('en ([A-H][1-8]) .+ : <br/>(.+)<br/><\/p>')

target = King()

l1data = callNC(l1url)
m = l1regex.search(l1data)
if not m:
    exit('Level 1 error')
print('Level 1 data: Target', m.group(1), ', attacker', m.group(2))
target.moveToNotation(m.group(1))
attacker = createFromString(m.group(2))
l1 = Level_1(target, attacker)
solution = l1.solve()
l2data = callNC(l1url+'?struct='+str(solution))
# print(l2data)
# LEVEL 2
m = l2regex.search(l2data)
if not m:
    exit('Level 2 error')
print('Level 2 data: Target', m.group(1), ', attacker', m.group(2))
target.moveToNotation(m.group(1))
attacker = createFromString(m.group(2))
l2 = Level_2(target, attacker)
solution = l2.solve()
l3data = callNC(l1url+'?struct='+str(solution[0])+str(solution[1]))
print(l3data)
# LEVEL 3
m = l3regex.search(l3data)
if not m:
    exit('Level 3 error')
attackers = []
sAttackers = m.group(2).split('<br/>')
for sAttacker in sAttackers:
    attackers.append(createFromString(sAttacker))
attackers = sorted(attackers, key=lambda x: x.value, reverse=True)
print('Level 3 data: Target', m.group(1), '- attackers:',attackers)
with open("results.txt", "a") as myfile:
    myfile.write('Level 3 data: Target\t'+m.group(1)+'\tattackers\t'+' '.join(list(map(lambda x:x.typeFull, attackers)))+'\n')

# target.moveToNotation(m.group(1))
# attackers = [createFromString(m.group(2)), createFromString(m.group(3)), createFromString(m.group(4))]
# l3 = Level_3(target, attackers)
# solution = l3.solve()
# l4data = callNC(l1url+'?struct='+str(solution[0])+str(solution[1])+str(solution[2]))
# print(l4data)
