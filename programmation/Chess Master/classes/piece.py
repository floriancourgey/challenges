#! /usr/bin/env python3
# coding: utf-8
from abc import ABC, abstractmethod
from .square import Square

class Piece(ABC):
    def __init__(self, x=0, y=0):
        self.square = Square(x, y)
    def __str__(self):
        return self.type()+self.square.__str__()
    def moveToSquare(self, square):
        self.square = square
    def moveToNotation(self, notation="A1"):
        self.square.x = self.square.letters.index(notation[0].upper())
        self.square.y = int(notation[1])-1
    ''' returns NC piece notation: p for pawn, c for knight.. '''
    @abstractmethod
    def type(self):
        pass
    ''' returns theoric relative coordinates where the piece is allowed to capture '''
    @abstractmethod
    def getPermutationsCapture(self):
        pass
    ''' returns theoric relative coordinates where the piece is allowed to move '''
    @abstractmethod
    def getPermutationsMove(self):
        pass
    '''
    @return a list of squares where this piece can move to,
    excluding a backlist of squares (controlled by the opponent)
    '''
    def movesAvailable(self, blacklist=[], stopAtFirst=False):
        squares = []
        for x,y in self.getPermutationsMove():
            x += self.square.x
            y += self.square.y
            if (x,y) == (self.square.x,self.square.y): continue # don't include self
            if not 0 <= x <= 7 or not  0 <= y <= 7: # stay in board boundaries
                continue
            square = Square(x, y)
            if square in blacklist:
                continue
            if stopAtFirst:
                return square
            squares.append(square)
        return squares
    '''
    @return a list of squares where this piece can be to capture the target,
    excluding a blacklist of squares (controlled by opponent)
    '''
    def capturesAvailableToTarget(self, target, blacklist=[], stopAtFirst=False):
        squares = []
        for x,y in self.getPermutationsCapture():
            xTest = target.square.x - x
            yTest = target.square.y - y
            if (xTest,yTest) == (self.square.x,self.square.y): continue # don't include self
            if (xTest,yTest) == (target.square.x,target.square.y): continue # don't include target
            if not 0 <= xTest <= 7 or not  0 <= yTest <= 7: # stay in board boundaries
                continue
            square = Square(xTest, yTest)
            if square in blacklist:
                continue
            if stopAtFirst:
                return square
            squares.append(square)
        return squares
