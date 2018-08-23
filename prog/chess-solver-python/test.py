#! /usr/bin/env python3
# coding: utf-8
import re
import time
from classes.square import Square
from classes.piece import Piece
from classes.bishop import Bishop
from classes.knight import Knight
from classes.rook import Rook
from classes.pawn import Pawn
from classes.queen import Queen
from classes.king import King


a = Square(3,1)
assert a.toTuple() == (3, 1)
assert a.__str__() == 'D2'
assert a.rot90().toTuple() == (1, -3)
assert a.rot90().rot90().toTuple() == (-3, -1)
assert a.rot90().rot90().rot90().toTuple() == (-1, 3)
assert a.rot90(2).toTuple() == (-3, -1) # rotate 180
assert a.rot90(3).toTuple() == (-1, 3) # rotate 270
b = Square(2, 5)
assert b.__str__() == 'C6'
assert (a + b).toTuple() == (5, 6)
assert (a * 2).toTuple() == (6, 2)
exit('tests passed successfully')
