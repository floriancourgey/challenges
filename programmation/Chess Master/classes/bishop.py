#! /usr/bin/env python3
# coding: utf-8
from .piece import Piece

class Bishop(Piece):
    def type(self):
        return "f"
    def getPermutations(self):
        # axis      SW/NE      +         NW/SE
        x = list(range(-7, 8)) + list(range(-7, 8))
        y = list(range(-7, 8)) + list(range(7, -8, -1))
        return zip(x,y) # [(-7,-7), (-6,-6)...(7,7), (-7,7), (-6,6)...(7-,7)]
