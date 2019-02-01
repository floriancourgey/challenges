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
matrix = [['-' for x in range(SIZE)] for y in range(SIZE)] # create matrix of 1
# printMatrix()

with open('sample.html', 'r') as f:
    lines = f.read()
lines = lines.replace('<html><p style="font-family:courier, monospace">', '')
lines = lines.replace('<br /></p></html>', '')
lines = lines.replace('&nbsp;', ' ')
lines = lines.replace('-', ' ')
lines = lines.replace('<br />', '\n')
print(lines)
with open('sample.txt', 'w') as f:
    lines = f.write(lines)
exit()
lines = f.readlines()[0:SIZE+2]
print(lines)
# find rays
rays = {}
for y,line in enumerate(lines):
    for x,char in enumerate(line):
        if char.isdigit():
            i = int(char)
            # x
            if x == 0: xCoord = 0
            elif x >= SIZE: xCoord = SIZE-1
            else: xCoord = x-1
            # y
            if y == 0: yCoord = 0
            elif y >= SIZE: yCoord = SIZE-1
            else: yCoord = y-1
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
    # vertical line if same x and y is border and y=SIZE-1
    if ray['start'][0] == ray['end'][0] and isBorder(ray['start'][1]) and isBorder(ray['end'][1]) and ray['start'][1]+ray['end'][1] == SIZE-1:
        # print('vertical line for ray', i, ray)
        for y in range(SIZE):
            matrix[y][ray['start'][0]] = i
        ray['done'] = True
    # horizontal line if same y
    if ray['start'][1] == ray['end'][1] and isBorder(ray['start'][0]) and isBorder(ray['end'][0]) and ray['start'][0]+ray['end'][0] == SIZE-1:
        # print('horizontal line for ray', i, ray)
        for x in range(SIZE):
            matrix[ray['start'][1]][x] = i
        ray['done'] = True
printMatrix()
