#! /usr/bin/env python3
# coding: utf-8
from classes.pawn import Pawn

class Level_2:
    def __init__(self, target, attacker):
        print('Level 2 init for target=',target,' and attacker=', attacker)
        self.target, self.attacker = target, attacker
    def solve(self):
        pawn = Pawn()
        squarePawn = pawn.capturesAvailableToTarget(self.target, [], True)
        pawn.moveToSquare(squarePawn)
        squareAttacker = self.attacker.capturesAvailableToTarget(pawn, self.target.movesAvailable(), True)
        self.attacker.moveToSquare(squareAttacker)
        solution = pawn, self.attacker
        print('Level 2 solved with solution:', solution)
        return solution
