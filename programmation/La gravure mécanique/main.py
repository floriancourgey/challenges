#! /usr/bin/env python3
# coding: utf-8
import config
import pyglet
import re
import time

window = pyglet.window.Window(1200, 300)

i=0 # number of lines drawn
facteur = 20 # scale text smaller/bigger
f = open('samples/1.gcode', 'r')

relativeX = 0 # last x (modified by moveRelativeToAbsolute() )
relativeY = 0 # last y (modified by moveRelativeToAbsolute() )

absoluteX = 10 # current x origin (modified by G52)
absoluteY = 30 # current y origin (modified by G52)

def drawLineAbsolute(fromX, fromY, toX, toY):
    global absoluteX
    global absoluteY
    global i
    i+=1
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2f', (fromX+absoluteX, fromY+absoluteY, toX+absoluteX, toY+absoluteY)),
        ('c3B', (0, 255, 0, 255, 0, 255))
    )
    print('draw abs', (fromX+absoluteX, fromY+absoluteY, toX+absoluteX, toY+absoluteY))
    # on trace 1 i sur 2
    if i%2 == 1:
        pyglet.text.Label(text=str(i), x=fromX+absoluteX, y=fromY+absoluteY).draw()

def drawLineFromRelativeToAbsolute(toX, toY):
    global relativeX
    global relativeY
    if toX == 0:
        toX = relativeX
    if toY == 0:
        toY = relativeY
    drawLineAbsolute(relativeX, relativeY, toX, toY)
    moveRelativeToAbsolute(toX, toY)

def moveRelativeToAbsolute(toX, toY):
    global relativeX
    global relativeY
    if toX != 0:
        relativeX = toX
    if toY != 0:
        relativeY = toY

@window.event
def on_draw():
    global absoluteX
    global absoluteY

    window.clear()
    regex = "(?P<g52>G52)?(X(?P<x>[\-\d\.]+))?(Y(?P<y>[\-\d\.]+))?"
    for match in re.finditer(regex, f.read()):
        x = y = 0
        if match.group('x'):
            x = round(float(match.group('x'))*facteur, 1)
        if match.group('y'):
            y = round(float(match.group('y'))*facteur, 1)
        if x==0 and y==0:
            continue
        # change origin
        if match.group('g52'):
            print('- line "'+match.group(0).strip()+'": G52 :', x, y)
            absoluteX = x
            # absoluteY = y # we don't want to change the y axis
        else:
            print('- line "'+match.group(0).strip()+'": draw :', x, y)
            drawLineFromRelativeToAbsolute(x,y)

        continue

pyglet.app.run()
