#! /usr/bin/env python3
# coding: utf-8
from classes.square import Square

class Level_3:
    def __init__(self, target, attackers):
        print('Level 3 init for target=',target)
        self.target, self.attackers = target, attackers
    def solve(self):
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
