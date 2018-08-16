#! /usr/bin/env python3
# coding: utf-8
from abc import ABC, abstractmethod
from .square import Square

class Piece(ABC):
    def __init__(self, x=0, y=0):
        self.square = Square(x, y)
    def __str__(self):
        return self.type()+self.square.__str__()
    def moveToNotation(self, notation="A1"):
        self.square.x = self.square.letters.index(notation[0].upper())
        self.square.y = int(notation[1])-1
    @abstractmethod
    def type(self):
        pass
    @abstractmethod
    def getPermutations(self):
        pass
    def squaresAvailableFromTarget(self, piece=None, stopAtFirst=False):
        origin = piece.square if piece else self.square
        squares = []
        for x,y in self.getPermutations():
            x += origin.x # axis NW/SE
            y += origin.y
            if (x,y) == (origin.x,origin.y): continue # don't include self
            if 0 <= x <= 7 and  0 <= y <= 7:
                squares.append(Square(x, y))
                if stopAtFirst:
                    return squares[0]
        return squares
