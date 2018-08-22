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
        print('Level 3 init for target=',target)
        self.target, self.attackers = target, attackers

    def solve(self):
        # define which solver to use
        # result = [x for x in self.attackers if x.canPerpendicular]
        if self.has(Queen):
            return self.solveWithOneQueen()
        elif self.nbPerpendicular() > 1:
            return self.solveWithTwoPerpendiculars()
        elif self.nbOf(Rook)>0 and self.nbOf(Bishop)>0 and self.nbOf(Knight)>0:
            return self.solveWithRookBishopKnight()
        exit('not yet solved')

    ''' 1 queen + anything '''
    def solveWithOneQueen(self):
        print('solveWithOneQueen')

    ''' 2 queens / queen+rook / 2 rooks '''
    def solveWithTwoPerpendiculars(self):
        print('solveWithTwoPerpendiculars')

    ''' Rook+Bishop+Knight '''
    def solveWithRookBishopKnight(self):
        print('solveWithRookBishopKnight')
        
    def old(self):
        # find perpendicular
        perpendicular = None
        for attacker in self.attackers:
            if attacker.canPerpendicular:
                perpendicular = attacker
                break
        print('perpendicular found', perpendicular)
        self.attackers.remove(perpendicular)
        print('attackers', self.attackers)
        # at first, the blacklist is all the squares surrounding the target and itself
        blacklist = self.target.movesAvailable()
        blacklist.append(self.target.square)
        # find closest side (N, E, S, W)
        directions = {'N':7-self.target.square.y, 'E':7-self.target.square.x,
                      'S':self.target.square.y, 'W':self.target.square.x}
        closest = min(directions, key=directions.get)
        # define perpendicular squares (P) (absolute coord)
        if closest == 'N':
            pSquaresAbs = [(-1,-1), (0,-1), (1,-1)]
        elif closest == 'E':
            pSquaresAbs = [(-1,-1), (-1,0), (-1,1)]
        elif closest == 'S':
            pSquaresAbs = [(-1,1), (0,1), (1,1)]
        elif closest == 'W':
            pSquaresAbs = [(1,-1), (1,0), (1,1)]
        # convert absolute to relative to target
        pSquaresRel = []
        for x,y in pSquaresAbs:
            pSquaresRel.append( Square(self.target.square.x+x, self.target.square.y+y ) )
        P = perpendicular.capturesAvailableToTargets(pSquaresRel, blacklist, True)
        perpendicular.moveToSquare(P)
        blacklist.append(P) # place first piece
        print('squarePerpendicular', P)
        # find the other 2 side squares (S1, S2)
        if closest in ['N', 'S']:
            permutations = [Square(-1,0), Square(1,0)]
        else:
            permutations = [Square(0,-1), Square(0,1)]
        S1 = self.attackers[0].capturesAvailableToTarget(self.target.square+permutations[0], blacklist, True)
        self.attackers[0].moveToSquare(S1)
        blacklist.append(S1) # place second piece
        S2 = self.attackers[1].capturesAvailableToTarget(self.target.square+permutations[1], blacklist, True)
        self.attackers[1].moveToSquare(S2)
        return (perpendicular, self.attackers[0], self.attackers[1])
