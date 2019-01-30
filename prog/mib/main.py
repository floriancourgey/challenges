#!/usr/bin/env python3
import subprocess
import os
import re
MIB_FOLDER = os.getcwd() # should contain NC-MIB.txt and SNMPv2-SMI
MIB_WALK = ['snmpwalk', '-M', MIB_FOLDER, '-t', '10', '-Os', '-c', 'public', '-v', '2c', 'www.***.org', '1.3.6.1.4.1.9999.2.1.3']
ret = subprocess.run(MIB_WALK, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
for line in ret.split('\n'):
	#if 'INTEGER: 99' in line:
	m = re.search('^.+\.(\w+) = INTEGER: 99', line)
	if not m:
		continue
	print(line)
	mib_id = m.group(1)
	print('mib_id', mib_id)
	MIB_WALK[-1] = "1.3.6.1.4.1.9999.2.1.1."+mib_id
	print('MIB_WALK', MIB_WALK)
	ret = subprocess.run(MIB_WALK, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
	print('ret', ret)
	m = re.search('^.+ = INTEGER: (\w+)', ret)
	cpu = m.group(1)
	print('cpu', cpu)
