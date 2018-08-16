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
    def squaresAvailableFromTarget(self, piece=None):
        pass
