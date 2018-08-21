#! /usr/bin/env python3
# coding: utf-8
import sys
sys.path.insert(0, '../..')
from config import *
from functions import *
import re
import math

regex = re.compile('(\d+)\)\*(\d+)&sup2;\+(\d+)')
html = get(URLS['prog']['_langage-tester']['problem'])
print(html)
m = regex.search(html)
if not m:
    exit('Unable to parse equation')
a = float(m.group(1))
b = float(m.group(2))
c = float(m.group(3))
solution = int( math.sqrt(a) * ( b**2 ) + c )
print(get(URLS['prog']['_langage-tester']['solution']+'?solution='+str(solution)))
