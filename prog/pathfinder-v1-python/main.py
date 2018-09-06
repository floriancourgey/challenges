#! /usr/bin/env python3
# coding: utf-8
import sys
sys.path.insert(0, '../..')
from config import *
from functions import *
from PIL import Image, ImageFilter
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import numpy
import networkx as nx
import matplotlib.pyplot as plt

X_TILE = 5 # a tile is (5,5) wide
Y_TILE = 5
TILE_WALL = (0, 0, 0) # RGB values for tiles
TILE_PATH = (255, 255, 255)
TILE_START = (0, 0, 255)
TILE_END = (255, 0, 0)

im = Image.open("original/maze.png")
# im = Image.open("samples/1.png")

print('image(x,y)', im.size)
xMax = int(im.size[0] / X_TILE) # define horizontal number of tiles
yMax = int(im.size[1] / Y_TILE) # define vertical number of tiles
max = max(xMax, yMax)
print('tiles(x,y)', (xMax,yMax))

# matrix = [[0 for x in range(xMax)] for y in range(yMax)] # create matrix of 0
matrix = [[0 for x in range(max)] for y in range(max)] # create matrix of 0
pixels = im.load() # get the pixel map
# for each tile(x,y)
for y in range(yMax):
    for x in range(xMax):
        rgb = im.getpixel((x*X_TILE,y*Y_TILE))
        if rgb == TILE_WALL:
            continue
        # if not wall, assign weight=1
        matrix[y][x] = 1
        # keep in memory start and end coordinates
        if rgb == TILE_START:
            START = (x,y)
        elif rgb == TILE_END:
            END = (x,y)

# start A*
# grid = Grid(matrix=matrix)
#
# start = grid.node(START[0], START[1])
# end = grid.node(END[0], END[1])
#
# finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
# path, runs = finder.find_path(start, end, grid)
#
# print('operations:', runs, 'path length:', len(path))
# print(grid.grid_str(path=path, start=start, end=end))

# start networkx
A=numpy.matrix(matrix)
G=nx.from_numpy_matrix(A)
G.edges(data=True)
print(G.number_of_nodes())
print(G.graph)

G = nx.petersen_graph()
# plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
