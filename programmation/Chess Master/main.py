#! /usr/bin/env python3
# coding: utf-8
from classes.piece import Piece
from classes.bishop import Bishop
from classes.knight import Knight

# coordinates start in bottom-left corner from (0,0) to (7,7)
# we are white (bottom A-H 0-1)
# target is black (top A-H 6-7)
# code is be 0-indexed but toString version is 1-indexed and uses letters for abscissas

class King(Piece):
    def type(self):
        return "r"
    def squaresAvailableFromTarget(self):
        return []
class Queen(Piece):
    def squaresAvailableFromTarget(self):
        return []
class Rook(Piece):
    def squaresAvailableFromTarget(self):
        return []
class Pawn(Piece):
    def squaresAvailableFromTarget(self):
        return []

target = King(0,4)
print(target)
b = Knight();b.moveToNotation("D4")
print(b)
for square in b.squaresAvailableFromTarget():
    print(square)