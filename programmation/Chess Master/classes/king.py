#! /usr/bin/env python3
# coding: utf-8
from .piece import Piece
from itertools import permutations, product

class King(Piece):
    def type(self):
        return "r"
    def getPermutationsCapture(self):
        couples = list(product([-1, 0, 1], repeat=2))
        couples.remove((0,0))
        return couples
    def getPermutationsMove(self):
        return self.getPermutationsCapture()
