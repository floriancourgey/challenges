#! /usr/bin/env python3
# coding: utf-8
from classes.piece import Piece
from classes.bishop import Bishop
from classes.knight import Knight
from classes.rook import Rook
from classes.pawn import Pawn
from classes.queen import Queen
from classes.king import King

# coordinates start in bottom-left corner from (0,0) to (7,7)
# we are white (bottom A-H 0-1)
# target is black (top A-H 6-7)
# code is be 0-indexed but toString version is 1-indexed and uses letters for abscissas

def createFromString(s):
    s = s.lower()
    if s == "pion": return Pawn()
    if s == "cavalier": return Knight()
    if s == "fou": return Bishop()
    if s == "tour": return Rook()
    if s == "dame": return Queen()

target = King(0,4)
print(target)
b = createFromString("Cavalier")
b.moveToNotation("D4")
print(b)
for square in b.squaresAvailableFromTarget():
    print(square)
