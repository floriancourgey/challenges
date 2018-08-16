#! /usr/bin/env python3
# coding: utf-8

class Level_1:
    def __init__(self, target, attacker):
        print('Level 1 init for target=',target,' and attacker=', attacker)
        self.target, self.attacker = target, attacker
    def solve(self):
        solution = self.attacker.squaresAvailableFromTarget(self.target, True)
        print('Level 1 solved with solution ', solution)
        self.attacker.square.x, self.attacker.square.y = solution.x, solution.y;
        return self.attacker
