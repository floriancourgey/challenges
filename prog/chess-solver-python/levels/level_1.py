#! /usr/bin/env python3
# coding: utf-8
from levels.level import Level
from classes.square import Square

class Level_1(Level):
    def solve(self):
        attacker = self.attackers[0]
        solution = attacker.capturesAvailableToTarget(self.target.square, [], True)
        print('Level 1 solved with solution ', solution)
        attacker.square = Square(solution.x, solution.y);
        return attacker
