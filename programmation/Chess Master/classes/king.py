#! /usr/bin/env python3
# coding: utf-8
from .piece import Piece

class King(Piece):
    def type(self):
        return "r"
    def getPermutations(self):
        pass
