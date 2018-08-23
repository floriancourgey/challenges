#! /usr/bin/env python3
# coding: utf-8
from classes.square import Square
from classes.piece import Piece
from classes.queen import Queen

class Level:
    def __init__(self, target, attackers):
        print('>>> Level init with target=',target,'and attackers=',attackers)
        self.target, self.attackers = target, attackers
    ''' find closest side (@return N, E, S or W) '''
    def getClosestSideFrom(self, square):
        if isinstance(square, Piece):
            square = square.square
        directions = {'N':7-square.y, 'E':7-square.x,
                    'S':square.y, 'W':square.x}
        closest = min(directions, key=directions.get)
        axis = {'N':Square(0,1), 'E':Square(1,0), 'S':Square(-1,0), 'W':Square(-1,-1)}
        return axis[closest]
    def getPieces(self, objectClass):
        return [x for x in self.attackers if isinstance(x, objectClass)]
    def getFirstPiece(self, objectClass):
        return self.getPieces(objectClass)[0]
    ''' return the number of attackers of class @param objectClass '''
    def nbOfPieces(self, objectClass):
        return len( self.getPieces(objectClass) )
    ''' return true/false if we have at least 1 attacker of class @param objectClass '''
    def hasPiece(self, objectClass):
        return self.nbOfPieces(objectClass) > 0

    ''' return the number of pieces that can (in theory) move to along perpendicular axis '''
    def nbPerpendicular(self):
        return len( [x for x in self.attackers if x.canPerpendicular] )
    def hasPerpendicular(self):
        return self.nbPerpendicular() > 0
