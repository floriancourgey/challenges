#! /usr/bin/env python3
# coding: utf-8
from .piece import Piece
from .square import Square

class Knight(Piece):
    def type(self):
        return "c"
    def squaresAvailableFromTarget(self):
        return []
