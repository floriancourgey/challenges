#! /usr/bin/env python3
# coding: utf-8
# import re
import os
import pefile
# opener = urllib2.build_opener()
# opener.addheaders.append(('Cookie', config.COOKIE))
# url = URL
# f = opener.open(url)#.read()
# with open('./crackeme.exe', "wb") as local_file:
#     local_file.write(f.read())

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
