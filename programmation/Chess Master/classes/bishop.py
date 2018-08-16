#! /usr/bin/env python3
# coding: utf-8
from .piece import Piece
from .square import Square

class Bishop(Piece):
    def type(self):
        return "f"
    def squaresAvailableFromTarget(self, piece=None, stopAtFirst=False):
        origin = piece.square if piece else self.square
        squares = []
        for i in range(-7,7):
            x, y = origin.x+i, origin.y-i # axis NW/SE
            if (x,y) == (origin.x,origin.y): continue # don't include self
            if 0 <= x <= 7 and  0 <= y <= 7:
                squares.append(Square(x, y))
            x, y = origin.x+i, origin.y+i # axis SW/NE
            if (x,y) == (origin.x,origin.y): continue # don't include self
            if 0 <= x <= 7 and  0 <= y <= 7:
                squares.append(Square(x, y))
            if stopAtFirst and len(squares) >= 1:
                return squares[0]
        return squares
