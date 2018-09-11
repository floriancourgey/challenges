#! /usr/bin/env python3
# coding: utf-8

class Bar:
    def __init__(self, id, x=0, y=0):
        if id<0 or x<0 or y<0:
            raise ValueError("Wrong params (",id,';',x,";",y+"): 0 <= id or x or y")
        self.id, self.x, self.y = id, x, y
        self.menu = {}
    def distanceToBar(self, otherBar):
        return abs(self.x-otherBar.x) + abs(self.y-otherBar.y)
    def addDrinkToMenu(self, name, price):
        self.menu[name] = price
    def __str__(self):
        return 'Bar id '+str(self.id)+' ('+str(self.x)+';'+str(self.y)+')'
    def __repr__(self):
        return self.__str__()
