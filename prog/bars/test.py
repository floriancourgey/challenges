#! /usr/bin/env python3
# coding: utf-8
from bar import Bar

# example:
# ___1__
# ______
# ______
# ____2_
# 3_____

bars = {
    1: Bar(1, 3, 0),
    2: Bar(2, 4, 3),
    3: Bar(3, 0, 4),
}

assert bars[1].distanceToBar(bars[2]) == 4
assert bars[1].distanceToBar(bars[3]) == 7
assert bars[2].distanceToBar(bars[3]) == 5
