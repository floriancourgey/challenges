#! /usr/bin/env python3
# coding: utf-8
# import re
import sys
sys.path.insert(0, '../..')
from config import *
from datetime import datetime
import os
import requests
# import pefile
url = URLS['prog']['crackme']
print('Downloading crackme')
r = requests.get(url, cookies=COOKIE_DICT)
filename = './crackme.exe'+datetime.now().strftime('-%Y%m%d-%H%M%S.exe')
print('Saving as '+filename)
with open(filename, "wb") as local_file:
    local_file.write(r.content)
exit()
pe =  pefile.PE('./crackeme.exe')

print('AddressOfEntryPoint:', pe.OPTIONAL_HEADER.AddressOfEntryPoint)
print('ImageBase:', pe.OPTIONAL_HEADER.ImageBase)

print('NumberOfSections:', pe.FILE_HEADER.NumberOfSections)
for i,section in enumerate(pe.sections):
  print('Section '+str(i+1)+': ',section.Name, hex(section.VirtualAddress),
    hex(section.Misc_VirtualSize), section.SizeOfRawData )

print('NumberOfDll:', len(pe.DIRECTORY_ENTRY_IMPORT))
for i,entry in enumerate(pe.DIRECTORY_ENTRY_IMPORT):
  print('DLL '+str(i+1)+': ',entry.dll)
  for imp in entry.imports:
    print('\t', hex(imp.address), imp.name)

# print(pe.dump_info())

for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
  print(hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal)
# print([entry.id for entry in pe.DIRECTORY_ENTRY_RESOURCE.entries])
