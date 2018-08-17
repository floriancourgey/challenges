#! /usr/bin/env python3
# coding: utf-8
from .piece import Piece

class Rook(Piece):
    def type(self):
        return "t"
    def getPermutationsCapture(self):
        # axis      W/E      +         N/S
        x = list(range(-7, 8)) + ([0] * 15)
        y = ([0] * 15)         + list(range(-7, 8))
        return zip(x,y) # [(-7,0), (-6,0)...(7,0), (0,-7), (0,-6)...(0,7)]
    def getPermutationsMove(self):
        return self.getPermutationsCapture()
