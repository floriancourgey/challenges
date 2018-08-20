#! /usr/bin/env python3
# coding: utf-8
import config
import re
import time
import requests
import pytesseract
from PIL import Image, ImageDraw

i=-1 # number of lines drawn
rapidMode = True # True = don't draw, just move / False = draw
scaleFactor = 10 # scale text smaller/bigger
regex = "(?P<g0>G0)?(?P<g1>G1)?(?P<g52>G52)?(X(?P<x>[\-\d\.]+))?(Y(?P<y>[\-\d\.]+))?"

# offline
# print('Using local Gcode')
# filename = 'samples/3.gcode'
# f = open(filename, 'r')
# text_data = f.read()
# online
print('Downloading Gcode')
filename = 'results/file.gcode'
r = requests.get(URL:config.COOKIE})
print('Challenge started')
text_data = r.text
with open(filename, 'w') as local_file:
    local_file.write(r.text)

relativeX = 0 # last x (modified by moveRelativeToAbsolute() )
relativeY = 0 # last y (modified by moveRelativeToAbsolute() )

absoluteX = scaleFactor*3 # current x origin (modified by G52)
absoluteY = scaleFactor*5 # current y origin (modified by G52)

iPolygon = 0;
polygons = []
iPolygonsInner = [] # some polygons will be interpreted as inner: 2 polygons for an O, 3 for an 8..
lastG = None # Remember the last G52, G0, to know if we face an inner polygon
im = Image.new('RGB', (1200,300))
draw = ImageDraw.Draw(im)

def drawLineAbsolute(fromX, fromY, toX, toY):
    global absoluteX
    global absoluteY

    global polygons
    global iPolygon

    # print('polygons len('+str(len(polygons))+'), iPolygon '+str(iPolygon))
    if len(polygons) <= iPolygon:
        polygons.append([])
    polygons[iPolygon].append( (toX+absoluteX, im.size[1]-toY-absoluteY) )

def drawLineFromRelativeToAbsolute(toX, toY):
    global relativeX
    global relativeY
    if toX is None:
        toX = relativeX
    if toY is None:
        toY = relativeY
    drawLineAbsolute(relativeX, relativeY, toX, toY)
    moveRelativeToAbsolute(toX, toY)

def moveRelativeToAbsolute(toX, toY):
    global relativeX
    global relativeY
    if toX is not None:
        relativeX = toX
    if toY is not None:
        relativeY = toY

print('Starting parsing')
for iLine,line in enumerate(text_data.split('\n')):
    line = line.strip().upper() # strip + upper
    # print('- line '+str(iLine+1)+':', line)
    match = re.match(regex, line)
    if not match:
        continue
    # Rapid mode
    if match.group('g0'):
        # print('* G0: Rapid mode ON')
        lastG = 'G0'
        rapidMode = True
        continue
    if match.group('g1'):
        # print('* G1: Rapid mode OFF')
        lastG = 'G1'
        rapidMode = False
        # print('polygons len('+str(len(polygons))+'), iPolygon '+str(iPolygon))
        if len(polygons) <= iPolygon:
            polygons.append([])
        iPolygon+=1
        continue
    # X/Y with or without G52
    x = y = None
    if match.group('x'):
        x = round(float(match.group('x'))*scaleFactor, 1)
    if match.group('y'):
        y = round(float(match.group('y'))*scaleFactor, 1)
    if x==None and y==None:
        continue
    # change origin
    if match.group('g52'):
        # print('* G52: (X:'+str(x)+', Y:'+str(y)+')')
        lastG = 'G52'
        absoluteX = x
        # absoluteY = y # never change y axis
    # move
    else:
        if rapidMode:
            # print('* move: (X:'+str(x)+', Y:'+str(y)+')')
            moveRelativeToAbsolute(x,y)
        else:
            # print('* draw: (X:'+str(x)+', Y:'+str(y)+')')
            drawLineFromRelativeToAbsolute(x,y)
        # if we had a G0, then a move, that's an inner polygon
        if lastG == 'G0' and iPolygon != 0:
            iPolygonsInner.append(iPolygon+1)
    continue

print('Creating image')
# print('# of polygons:',len(polygons))
# print('Inner polygons 0-i:', iPolygonsInner)
for i,polygonTuples in enumerate(polygons):
    if len(polygonTuples) < 4:
        continue
    # draw inner polygon in black
    if i in iPolygonsInner:
        draw.polygon(polygonTuples, fill=(0,0,0,255) )
    # draw regular polygon in green
    else:
        draw.polygon(polygonTuples, fill=(0,255,0,255) )

print('Saving image')
im.save(filename+'.pil.png')
im.show()

print('Decoding image with pytesseract')
decoded = pytesseract.image_to_string(filename+'.pil.png', lang='eng', config='')
# based on experiences, we know there's no spaces and tesseract reads a | instead of a ]
decoded = decoded.replace(' ', '').replace('|', ']')
print(decoded)

url = URL+decoded
print('Calling '+url)
r = requests.get(url, cookies={'Cookie':config.COOKIE})
print(r.text)

print('Showing image')
im.show()
