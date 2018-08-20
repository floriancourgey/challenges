#! /usr/bin/env python3
# coding: utf-8
from .piece import Piece
from .rook import Rook
from .bishop import Bishop
from .square import Square

class Queen(Piece):
    typeFull = 'Dame'
    typeShort = 'd'
    canPerpendicular = True
    value = 9
    def getPermutationsCapture(self):
        couples = []
        b = Bishop()
        r = Rook()
        for x in b.getPermutationsCapture(): couples.append(x)
        for x in r.getPermutationsCapture(): couples.append(x)
        return couples
    def getPermutationsMove(self):
        return self.getPermutationsCapture()
