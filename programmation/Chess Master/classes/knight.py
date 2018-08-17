#! /usr/bin/env python3
# coding: utf-8
from .piece import Piece
from itertools import permutations

class Knight(Piece):
    def type(self):
        return "c"
    def getPermutationsCapture(self):
        couples = []
        for x,y in permutations([-2,-1,1,2], 2): # [(-2,-2), (-2,-2), (-2,1)...]
            # remove (2,2) and (1,1), so we have:
            # [removed, (-2,-2), (-2,1)...]
            if abs(x)+abs(y) != 3:
                continue
            couples.append((x,y))
        return couples
    def getPermutationsMove(self):
        return self.getPermutationsCapture()
