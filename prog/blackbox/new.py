#! /usr/bin/env python3
# coding: utf-8
import sys
sys.path.insert(0, '../..')
from config import *
from functions import *

TYPE_OUTER=11
TYPE_ATOM=12
TYPE_EMPTY=13
TYPE_RAY=range(1,10)
ALL_SQUARES=[i for i in range(11,89) if i%10>0 and i%10<9]
print(ALL_SQUARES)

def initial_board():
    board = [TYPE_OUTER for x in range(0, 100)]
    for i in ALL_SQUARES:
        board[i] = TYPE_EMPTY
    return board

def print_board(board):
    txt = ''
    for i in range(0, 100):
        txt += str(board[i])
        if(i>1 and i % 10 == 9):
            txt += '\n'
    print(txt)

board = initial_board()
print_board(board)
