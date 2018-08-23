#! /usr/bin/env python3
# coding: utf-8
import sys
sys.path.insert(0, '../..')
from config import *
from functions import *
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

'''
coordinates start in bottom-left corner from (0,0) to (7,7)
we are white (bottom A-H 0-1)
target is black (top A-H 6-7)
code is 0-indexed but toString version is 1-indexed and uses letters for abscissas

all permutations point to the north direction and are then rotated
'''
def createFromString(s):
    s = s.lower().replace(' ', '')
    if s == "pion": return Pawn()
    if s == "cavalier": return Knight()
    if s == "fou": return Bishop()
    if s == "tour": return Rook()
    if s == "dame": return Queen()

l1url = URLS['prog']['chess-master']
l1regex = re.compile('Niveau 1.+; en ([A-H][1-8])\..+<br\/>(\w+)<br')
l2regex = re.compile('Niveau 2.+en ([A-H][1-8]) tout en.+>(\w+)<br\/><\/p>')
l3regex = re.compile('Niveau 3.+en ([A-H][1-8]) .+ : <br/>(.+)<br/><\/p>')
l4regex = re.compile('Niveau 4.+en ([A-H][1-8])\.<br/>(.+)<br/><\/p>')

target = King()

l1data = get(l1url)
m = l1regex.search(l1data)
if not m:
    print(l1data)
    exit('Level 1 error')
target.moveToNotation(m.group(1))
attacker = createFromString(m.group(2))
l1 = Level_1(target, [attacker])
solution = l1.solve()
l2data = get(l1url+'?struct='+str(solution))
# print(l2data)
# LEVEL 2
m = l2regex.search(l2data)
if not m:
    print(l2data)
    exit('Level 2 error')
target.moveToNotation(m.group(1))
attacker = createFromString(m.group(2))
l2 = Level_2(target, [attacker])
solution = l2.solve()
l3data = get(l1url+'?struct='+str(solution[0])+str(solution[1]))
print(l3data[-250:])
# LEVEL 3
m = l3regex.search(l3data)
if not m:
    print(l3data)
    exit('Level 3 error')
target.moveToNotation(m.group(1))
attackers = []
sAttackers = m.group(2).split('<br/>')
for sAttacker in sAttackers:
    attackers.append(createFromString(sAttacker))
attackers = sorted(attackers, key=lambda x: x.value, reverse=True) # sort pieces by value
with open("samples/level_3_data.txt", "a") as myfile:
    myfile.write('Level 3 data: Target\t'+m.group(1)+'\tattackers\t'+' '.join(list(map(lambda x:x.typeFull, attackers)))+'\n')
l3 = Level_3(target, attackers)
solution = l3.solve()
print(solution)
l4data = get(l1url+'?struct='+solution)
print(l4data[-250:])
# LEVEL 4
m = l4regex.search(l4data)
if not m:
    print(l4data)
    exit('Level 3 error')
target.moveToNotation(m.group(1))
attackers = []
sAttackers = m.group(2).split('<br/>')
for sAttacker in sAttackers:
    attackers.append(createFromString(sAttacker))
attackers = sorted(attackers, key=lambda x: x.value, reverse=True) # sort pieces by value
with open("samples/level_4_data.txt", "a") as myfile:
    myfile.write('Level 4 data: Target\t'+m.group(1)+'\tattackers\t'+' '.join(list(map(lambda x:x.typeFull, attackers)))+'\n')
