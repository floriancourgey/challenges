#! /usr/bin/env python3
# coding: utf-8
from levels.level import Level
from classes.pawn import Pawn

class Level_2(Level):
    def solve(self):
        attacker = self.attackers[0]
        pawn = Pawn()
        squarePawn = pawn.capturesAvailableToTarget(self.target.square, [], True)
        pawn.moveToSquare(squarePawn)
        blacklist = self.target.movesAvailable()
        blacklist.append(squarePawn)
        blacklist.append(self.target.square)
        squareAttacker = attacker.capturesAvailableToTarget(pawn.square, blacklist, True)
        attacker.moveToSquare(squareAttacker)
        solution = pawn, attacker
        print('Level 2 solved with solution:', solution)
        return solution
