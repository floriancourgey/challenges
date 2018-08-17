#! /usr/bin/env python3
# coding: utf-8

class Square:
    def __init__(self, x=0, y=0):
        if(x<0 or x>7 or y<0 or y>7):
            raise ValueError("Wrong params ("+str(x)+","+str(y)+"): 0 <= x,y <= 7")
        self.x, self.y = x, y
        self.letters = 'ABCDEFGH'
    def __str__(self):
        return self.letters[self.x]+str(self.y+1)
    ''' 2 squares are equal is they have the same (x,y) '''
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
