#! /usr/bin/env python3
# coding: utf-8
from .piece import Piece

class Pawn(Piece):
    def type(self):
        return "p"
    def getPermutationsCapture(self):
        return [(-1,1), (1,1)]
    def getPermutationsMove(self):
        return [(0,1)]
