#! /usr/bin/env python3
# coding: utf-8
import sys
sys.path.insert(0, '../..')
from config import *
from functions import *

SIZE = 8
ATOMS = 4

def isBorder(x):
    return x == 0 or x == SIZE-1
def printMatrix():
    for y in range(SIZE):
        for x in range(SIZE):
            print(matrix[y][x], end='')
        print()
matrix = [[1 for x in range(SIZE)] for y in range(SIZE)] # create matrix of 1
printMatrix()

f = open('sample.txt', 'r')
lines = f.readlines()[0:SIZE+2]
print(lines)
# find rays
rays = {}
for y,line in enumerate(lines):
    for x,char in enumerate(line):
        if char.isdigit():
            i = int(char)
            xCoord = 0 if x == 0 else x-2
            yCoord = 0 if y == 0 else y-2
            # if it doesn't exist, create Start
            if i not in rays:
                rays[i] = {'start':(xCoord,yCoord)}
            # else create End
            else:
                rays[i]['end'] = (xCoord,yCoord)
for i,ray in rays.items():
    if 'start' not in ray or 'end' not in ray:
        raise Exception('Invalid ray ',i,ray)
print('Number of rays:', len(rays))
print(rays)
# fill straight lines
for i, ray in rays.items():
    # vertical line if same x and y is border
    if ray['start'][0] == ray['end'][0] and isBorder(ray['start'][1]) and isBorder(ray['end'][1]):
        print('vertical line for ray', i, ray)
        for y in range(SIZE):
            matrix[y][ray['start'][0]] = 0
    # horizontal line if same y
    if ray['start'][1] == ray['end'][1] and isBorder(ray['start'][0]) and isBorder(ray['end'][0]):
        print('horizontal line for ray', i, ray)
        for x in range(SIZE):
            matrix[ray['start'][1]][x] = 0
printMatrix()
