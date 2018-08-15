#! /usr/bin/env python3
# coding: utf-8
import config
import pyglet
import re
import time

window = pyglet.window.Window(1200, 300)

i=0 # number of lines drawn
rapidMode = True # True = don't draw, just move / False = draw
scaleFactor = 20 # scale text smaller/bigger
f = open('samples/1.gcode', 'r')

relativeX = 0 # last x (modified by moveRelativeToAbsolute() )
relativeY = 0 # last y (modified by moveRelativeToAbsolute() )

absoluteX = 10 # current x origin (modified by G52)
absoluteY = scaleFactor*4 # current y origin (modified by G52)

def drawLineAbsolute(fromX, fromY, toX, toY):
    global absoluteX
    global absoluteY
    global i
    i+=1
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2f', (fromX+absoluteX, fromY+absoluteY, toX+absoluteX, toY+absoluteY)),
        ('c3B', (255, 255, 255, 255, 255, 255)) # white
        # ('c3B', (0, 255, 0, 255, 0, 255)) # green to purple
    )
    print('draw abs', (fromX+absoluteX, fromY+absoluteY, toX+absoluteX, toY+absoluteY))
    # draw a text helper at the start of the line (for debugging)
    # if i%2 == 1:
    #     pyglet.text.Label(text=str(i), x=fromX+absoluteX, y=fromY+absoluteY).draw()

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


@window.event
def on_draw():
    global absoluteX
    global absoluteY

    window.clear()
    regex = "(?P<g0>G0)?(?P<g1>G1)?(?P<g52>G52)?(X(?P<x>[\-\d\.]+))?(Y(?P<y>[\-\d\.]+))?"
    for iLine,line in enumerate(f):
        line = line.strip().upper() # strip + upper
        print('- line '+str(iLine+1)+':', line)
        match = re.match(regex, line)
        # Rapid mode
        if not match:
            continue
        if match.group('g0'):
            print('* G0: Rapid mode ON')
            rapidMode = True
            continue
        if match.group('g1'):
            print('* G1: Rapid mode OFF')
            rapidMode = False
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
            absoluteX = x
            # absoluteY = y # never change y axis
        else:
            if rapidMode:
                print('* move: (X:'+str(x)+', Y:'+str(y)+')')
                moveRelativeToAbsolute(x,y)
            else:
                print('* draw: (X:'+str(x)+', Y:'+str(y)+')')
                drawLineFromRelativeToAbsolute(x,y)

        continue

pyglet.app.run()
