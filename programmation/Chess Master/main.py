#! /usr/bin/env python3
# coding: utf-8
import config
import re
import requests
from classes.piece import Piece
from classes.bishop import Bishop
from classes.knight import Knight
from classes.rook import Rook
from classes.pawn import Pawn
from classes.queen import Queen
from classes.king import King
from levels.level_1 import Level_1
from levels.level_2 import Level_2

# coordinates start in bottom-left corner from (0,0) to (7,7)
# we are white (bottom A-H 0-1)
# target is black (top A-H 6-7)
# code is be 0-indexed but toString version is 1-indexed and uses letters for abscissas

def callNC(url):
    print('Calling URL:', url)
    r = requests.get(url, cookies={'SMFCookie89':config.COOKIE})
    return r.text

def createFromString(s):
    s = s.lower()
    if s == "pion": return Pawn()
    if s == "cavalier": return Knight()
    if s == "fou": return Bishop()
    if s == "tour": return Rook()
    if s == "dame": return Queen()

target = King()
target.getPermutationsMove()
l1url = 'https://www.newbiecontest.org/epreuves/prog/prog_chessmaster1.php'
l1regex = re.compile('; en (?P<target>[A-H][1-8])\..+<br\/>(?P<attacker>\w+)<br')
l1data = callNC(l1url)
m = l1regex.search(l1data)
print('Level 1 data: Target ', m.group('target'), ', attacker', m.group('attacker'))
target.moveToNotation(m.group('target'))
attacker = createFromString(m.group('attacker'))
l1 = Level_1(target, attacker)
solution = l1.solve()
l2data = callNC(l1url+'?struct='+str(solution))
print(l2data)

l2regex = re.compile('en (?P<target>[A-H][1-8]) tout en.+>(?P<attacker>\w+)<br\/><\/p>')
m = l2regex.search(l2data)
print('Level 2 data: Target ', m.group('target'), ', attacker', m.group('attacker'))

target.moveToNotation(m.group('target'))
attacker = createFromString(m.group('attacker'))
l2 = Level_2(target, attacker)
solution = l2.solve()
l3data = callNC(l1url+'?struct='+str(solution[0])+str(solution[1]))
print(l3data)
