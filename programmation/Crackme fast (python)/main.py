#! /usr/bin/env python
# coding: utf-8
import urllib2
import config
# import re
import os
import pefile
# opener = urllib2.build_opener()
# opener.addheaders.append(('Cookie', config.COOKIE))
# url = 'https://www.newbiecontest.org/epreuves/prog/prog_crackmefast.php'
# f = opener.open(url)#.read()
# with open('./crackeme.exe', "wb") as local_file:
#     local_file.write(f.read())

pe =  pefile.PE('./crackeme.exe')

print(pe.OPTIONAL_HEADER.AddressOfEntryPoint)
print(pe.OPTIONAL_HEADER.ImageBase)
print(pe.FILE_HEADER.NumberOfSections)

for section in pe.sections:
  print (section.Name, hex(section.VirtualAddress),
    hex(section.Misc_VirtualSize), section.SizeOfRawData )

for entry in pe.DIRECTORY_ENTRY_IMPORT:
  print entry.dll
  for imp in entry.imports:
    print '\t', hex(imp.address), imp.name

print pe.dump_info()

print [entry.id for entry in pe.DIRECTORY_ENTRY_RESOURCE.entries]
