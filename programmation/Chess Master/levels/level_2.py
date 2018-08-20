#! /usr/bin/env python3
# coding: utf-8
from classes.pawn import Pawn

class Level_2:
    def __init__(self, target, attacker):
        print('Level 2 init for target=',target,'and attacker=', attacker)
        self.target, self.attacker = target, attacker
    def solve(self):
        pawn = Pawn()
        squarePawn = pawn.capturesAvailableToTarget(self.target.square, [], True)
        pawn.moveToSquare(squarePawn)
        blacklist = self.target.movesAvailable()
        blacklist.append(squarePawn)
        blacklist.append(self.target.square)
        squareAttacker = self.attacker.capturesAvailableToTarget(pawn.square, blacklist, True)
        self.attacker.moveToSquare(squareAttacker)
        solution = pawn, self.attacker
        print('Level 2 solved with solution:', solution)
        return solution
