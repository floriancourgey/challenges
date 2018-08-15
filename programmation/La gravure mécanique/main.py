#! /usr/bin/env python3
# coding: utf-8
import config
import re
import time
from PIL import Image, ImageDraw

i=-1 # number of lines drawn
rapidMode = True # True = don't draw, just move / False = draw
scaleFactor = 20 # scale text smaller/bigger
filename = 'samples/1.gcode'
f = open(filename, 'r')

relativeX = 0 # last x (modified by moveRelativeToAbsolute() )
relativeY = 0 # last y (modified by moveRelativeToAbsolute() )

absoluteX = 10 # current x origin (modified by G52)
absoluteY = scaleFactor*4 # current y origin (modified by G52)

iPolygon = 0;
polygons = []
iPolygonsInner = []
lastG = None
im = Image.new('RGB', (1200,300))
draw = ImageDraw.Draw(im)

def drawLineAbsolute(fromX, fromY, toX, toY):
    global absoluteX
    global absoluteY

    global polygons
    global iPolygon

    print('polygons len('+str(len(polygons))+'), iPolygon '+str(iPolygon))
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

regex = "(?P<g0>G0)?(?P<g1>G1)?(?P<g52>G52)?(X(?P<x>[\-\d\.]+))?(Y(?P<y>[\-\d\.]+))?"
for iLine,line in enumerate(f):
    line = line.strip().upper() # strip + upper
    # print('- line '+str(iLine+1)+':', line)
    match = re.match(regex, line)
    # Rapid mode
    if not match:
        continue
    if match.group('g0'):
        print('* G0: Rapid mode ON')
        lastG = 'G0'
        rapidMode = True
        continue
    if match.group('g1'):
        print('* G1: Rapid mode OFF')
        lastG = 'G1'
        rapidMode = False
        print('polygons len('+str(len(polygons))+'), iPolygon '+str(iPolygon))
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
        print('* G52: (X:'+str(x)+', Y:'+str(y)+')')
        lastG = 'G52'
        absoluteX = x
        # absoluteY = y # never change y axis
    # move
    else:

        #
        if rapidMode:
            # print('* move: (X:'+str(x)+', Y:'+str(y)+')')
            moveRelativeToAbsolute(x,y)
        else:
            # print('* draw: (X:'+str(x)+', Y:'+str(y)+')')
            drawLineFromRelativeToAbsolute(x,y)
        # if we have a G0, then a move, that's an inner polygon
        if lastG == 'G0' and iPolygon != 0:
            iPolygonsInner.append(iPolygon+1)
    continue

print('Creating image')
print('# of polygons:',len(polygons))
print('Inner polygons 0-i:', iPolygonsInner)
for i,polygonTuples in enumerate(polygons):
    if len(polygonTuples) < 4:
        continue
    # draw inner polygon in black
    if i in iPolygonsInner:
        draw.polygon(polygonTuples, fill=(0,0,0,255) )
    # draw regular polygon in green
    else:
        draw.polygon(polygonTuples, fill=(0,255,0,255) )
    # start
    # draw.ellipse( ( (polygonTuples[0][0]-3,polygonTuples[0][1]-3), (polygonTuples[0][0]+3,polygonTuples[0][1]+3)) , fill=(255,0,0,255))
    # draw.ellipse( ( (polygonTuples[-1][0]-3,polygonTuples[-1][1]-3), (polygonTuples[-1][0]+3,polygonTuples[-1][1]+3)) , fill=(0,255,0,255))
    # draw.ellipse( ( (polygonTuples[1][0]-3,polygonTuples[1][1]-3), (polygonTuples[1][0]+3,polygonTuples[1][1]+3)) , fill=(0,0,255,255))

print('Saving image')
# ImageDraw.floodfill(im, (1,1), (255,255,255,255), border=None, thresh=0)
im.save(filename+'.pil.png')
print('Showing image')
im.show()
