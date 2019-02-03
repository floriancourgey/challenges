#!/usr/bin/env python3
# coding: utf-8
import os
if not os.path.isfile('./NC-MIB.txt'):
    exit('missing NC-MIB.txt')
import sys
sys.path.insert(0, '../..')
from config import *
import subprocess
import re
MIB_FOLDER = os.getcwd() # should contain NC-MIB.txt and SNMPv2-SMI
CMD = ['snmpwalk', '-M', MIB_FOLDER, '-t', '10', '-Os', '-c', 'public', '-v', '2c', URLS['prog']['mib'], '1.3.6.1.4.1.9999.2.1.3']
ret = subprocess.run(CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
for line in ret.split('\n'):
    m = re.search('^.+\.(\w+) = INTEGER: 99', line)
    if not m:
        continue
    print(line)
    mib_id = m.group(1)
    print('mib_id', mib_id)
    CMD[0], CMD[-1] = 'snmpset', '1.3.6.1.4.1.9999.2.1.4.'+mib_id
    CMD.append('s')
    CMD.append('stopped')
    print('CMD', CMD)
    ret = subprocess.run(CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
    print('ret', ret)
