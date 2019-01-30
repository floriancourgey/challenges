#!/usr/bin/env python3
import subprocess
import os
MIB_FOLDER = os.getcwd() # should contain NC-MIB.txt and SNMPv2-SMI
ret = subprocess.run(['snmpwalk', '-M', MIB_FOLDER, '-t', '10', '-Os', '-c', 'public', '-v', '2c', 'www.***.org', '1.3.6.1.4.1.9999.2.1.3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
for line in ret.split('\n'):
	if 'INTEGER: 99' in line:
		print(line)
