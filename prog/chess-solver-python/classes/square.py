#! /usr/bin/env python3
# coding: utf-8

class Square:
    def __init__(self, x=0, y=0):
        # if(x<0 or x>7 or y<0 or y>7):
            # raise ValueError("Wrong params ("+str(x)+","+str(y)+"): 0 <= x,y <= 7")
        self.x, self.y = x, y
        self.letters = 'ABCDEFGH'
    def toTuple(self):
        return self.x, self.y
    def rot90(self, k=1):
        new = Square(self.x, self.y)
        for i in range(k):
            x = new.y
            y = -new.x
            new.x, new.y = x, y
        return new
    def rot90ForDirection(self, direction):
        if direction == 'N': k=0;
        elif direction == 'E': k=1;
        elif direction == 'S': k=2;
        elif direction == 'W': k=3;
        return self.rot90(k)
    def rot90from(square):
        x = -(self.y - square.y) + square.x
        y = (self.x - square.px) + square.py
        self.x, self.y = x, y
        return self
    def __str__(self):
        return self.letters[self.x]+str(self.y+1)
    ''' 2 squares are equal is they have the same (x,y) '''
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __add__(self, other):
        return Square(self.x+other.x, self.y+other.y)
    def __sub__(self, other):
        return Square(self.x-other.x, self.y-other.y)
    def __mul__(self, other):
        return Square(self.x*other, self.y*other)
