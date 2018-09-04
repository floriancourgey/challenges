#! /usr/bin/env python3
# coding: utf-8
import sys
sys.path.insert(0, '../..')
from config import *
from functions import *
from PIL import Image, ImageFilter
import config
import cv2
from datetime import datetime
from OcrMonotype import OcrMonotype
sys.path.insert(0, '../vigenere-python')
from vigenere import Vigenere

pngSignature = b'\x89\x50\x4E\x47'

# init OCR & its dic
# X_LTR, Y_LTR, X_ORIGIN, Y_ORIGIN, X_MARGIN, Y_MARGIN, dicoPath, addUnknownToDic
ocr = OcrMonotype(8, 10, 5, 8, 0, 5, 'dico_8_10.txt', True)

# offline
# filename = 'samples/2018-09-03T18:06:36.096125file.png'
# print('Offline mode with file: '+filename)
# f = open(filename, 'rb')
# bin_data = f.read()
# online
bin_data = get(config.URLS['prog']['ocr-v3']['problem'], True).content
filename = 'results/'+datetime.now().isoformat()+'file.png'
with open(filename, "wb") as local_file:
    local_file.write(bin_data)
    print(filename+' ok')
# split whole file by PNG signature
chunks = bin_data.split(pngSignature) # ['', file1, file2, file3]
if len(chunks) != 4:
    exit('wrong input file format')
del chunks[0] # remove first empty
# create the 3 files
for i,chunk in enumerate(chunks):
    with open(filename+str(i)+".png", "wb") as file:
        file.write(pngSignature)
        file.write(chunk)
master = Image.open(filename+"0.png")
print('size(x,y)', master.size)
xMax = master.size[0]
yMax = master.size[1]
vertical = Image.open(filename+"1.png")
horizontal = Image.open(filename+"2.png")
# create output file, with the size of the master
output = Image.new('RGB', master.size)
finalFilename = filename+"final.png"
output.save(finalFilename) # create black PNG file
pixels = output.load() # create the pixel map
# for each pixel(x,y) in master
for y in range(yMax):
    for x in range(xMax):
        r, g, b = master.getpixel((x,y))
        if r+g+b == 0:
            continue
        if r>0:
            # horizontal offset first
            deltaY = horizontal.getpixel((x,0))[0]
            yNew = (y-deltaY)%yMax
            # then vertical offset
            deltaX = vertical.getpixel((0,yNew))[0]
            xNew = (x-deltaX)%xMax
            # write it
            pixels[xNew,yNew] = (255, 255, 255)

output.save(finalFilename) # save pixels modification

# execute OCR
ocr.loadFile(finalFilename)
lines = ocr.compute()
print('OCR data: ', lines)
if len(lines) != 3:
    raise Exception('OCR Unable to find 3 lines in OCR data')
sentence = lines[0].strip()
key = lines[1].strip()
index = int(lines[2][0])
index0 = index-1
print('Vigenere decypher for sentence: '+sentence, 'with key: '+key)
vigenere = Vigenere(key)
result = vigenere.decrypt(sentence)
print('Vigenere result: '+result)
words = result.split(' ')
if index0 >= len(words):
    exit('Index mismatch with number of words')
solution = words[index0]
html = get(config.URLS['prog']['ocr-v3']['solution']+'?solution='+solution)
print(html)
