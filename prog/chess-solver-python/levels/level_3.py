#! /usr/bin/env python3
# coding: utf-8
from levels.level import Level
from classes.square import Square
from classes.queen import Queen
from classes.rook import Rook
from classes.bishop import Bishop
from classes.knight import Knight

class Level_3(Level):
    def __init__(self, target, attackers):
        print('Level 3 init for target=',target,'attackers=',attackers)
        self.target, self.attackers = target, attackers
        self.closest = self.getClosestSideFrom(self.target) # closest side (N,E..)
        self.furthest = self.closest.rot90(2)
    def solve(self):
        # define which solver to use
        # result = [x for x in self.attackers if x.canPerpendicular]
        if self.hasPiece(Queen) and len(self.attackers)>1:
            return self.solveWithOneQueen()
        elif self.nbPerpendicular() > 1:
            return self.solveWithTwoPerpendiculars()
        elif self.nbOfPieces(Rook)>0 and self.nbOfPieces(Bishop)>0 and self.nbOfPieces(Knight)>0:
            return self.solveWithRookBishopKnight()
        exit('not yet solved')

    ''' 1 queen + anything '''
    def solveWithOneQueen(self):
        print('solveWithOneQueen')
        # move the queen right behind the target
        queen = self.getFirstPiece(Queen)
        queen.moveToSquare( self.target.square + self.furthest )
        # move first attacker to defend the queen
        blacklist = self.target.movesAvailable()
        blacklist.append(self.target.square)
        self.attackers[1].square = self.attackers[1].capturesAvailableToTarget(queen.square, blacklist, True)
        # move other attackers far away
        for i,attacker in enumerate(self.attackers[2:]):
            sq = self.target.square + (self.furthest * (6-i))
            attacker.moveToSquare(sq)
        solution = ""
        for attacker in self.attackers:
            solution += str(attacker)
        return solution

    ''' 2 queens / queen+rook / 2 rooks '''
    def solveWithTwoPerpendiculars(self):
        exit('solveWithTwoPerpendiculars but not yet solved')

    ''' Rook+Bishop+Knight '''
    def solveWithRookBishopKnight(self):
        exit('solveWithRookBishopKnight but not yet solved')
