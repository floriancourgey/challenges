#! /usr/bin/env python3
# coding: utf-8
from .piece import Piece
from .rook import Rook
from .bishop import Bishop
from .square import Square

class Queen(Piece):
    def type(self):
        return "t"
    def getPermutations(self):
        couples = []
        b = Bishop()
        r = Rook()
        for x in b.getPermutations(): couples.append(x)
        for x in r.getPermutations(): couples.append(x)
        return couples
