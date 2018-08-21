#! /usr/bin/env python3
# coding: utf-8
from abc import ABC, abstractmethod
from .square import Square

class Piece(ABC):
    typeFull = 'Piece' # used for debug
    typeShort = '?' # used in solutions
    value = 0 # https://en.wikipedia.org/wiki/Chess_piece_relative_value
    canPerpendicular = False # only rooks+queen can move perpendicular
    def __init__(self, x=0, y=0):
        self.square = Square(x, y)
    def __str__(self):
        return self.typeShort+self.square.__str__()
    def moveToSquare(self, square):
        self.square = square
    def moveToNotation(self, notation="A1"):
        self.square.x = self.square.letters.index(notation[0].upper())
        self.square.y = int(notation[1])-1
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
    @param Square target
    @param Square[] blacklist
    '''
    def capturesAvailableToTarget(self, target, blacklist=[], stopAtFirst=False):
        squares = []
        for x,y in self.getPermutationsCapture():
            xTest = target.x - x
            yTest = target.y - y
            if (xTest,yTest) == (self.square.x,self.square.y): continue # don't include self
            if (xTest,yTest) == (target.x,target.y): continue # don't include target
            if not 0 <= xTest <= 7 or not  0 <= yTest <= 7: # stay in board boundaries
                continue
            square = Square(xTest, yTest)
            if square in blacklist:
                continue
            if stopAtFirst:
                return square
            squares.append(square)
        return squares
    '''
    @return a list of squares where this piece can be to capture multiple targets,
    excluding a blacklist of squares (controlled by opponent)
    '''
    def capturesAvailableToTargets(self, targets, blacklist=[], stopAtFirst=False):
        squares = []
        capturesAvailable = []
        # create 1 list per target
        for target in targets:
            tuples = []
            capturesAvailable.append(self.capturesAvailableToTarget(target, blacklist))
        # then, iterate over the first list, and foreach square, see if it exists in other lists
        for square in capturesAvailable[0]:
            squareFound = True
            for list in capturesAvailable[1:]:
                if square not in list:
                    squareFound = False
                    break
            if squareFound:
                if stopAtFirst:
                    return square
                squares.append(square)
        return squares
