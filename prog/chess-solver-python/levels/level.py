#! /usr/bin/env python3
# coding: utf-8
from classes.square import Square
from classes.queen import Queen

class Level:
    def __init__(self, target, attackers):
        print('>>> Level init with target=',target,'and attackers=',attackers)
        self.target, self.attackers = target, attackers
    ''' return the number of attackers of class @param objectClass '''
    def nbOf(self, objectClass):
        return len( [x for x in self.attackers if isinstance(x, objectClass)] )
    ''' return true/false if we have at least 1 attacker of class @param objectClass '''
    def has(self, objectClass):
        return self.nbOf(objectClass) > 0
    def nbPerpendicular(self):
        return len( [x for x in self.attackers if x.canPerpendicular] )
    def hasPerpendicular(self):
        return self.nbPerpendicular() > 0
