#!/usr/bin/env python3
from PIL import Image

colors = []
im = Image.open("samples/01.png")
print(im.format, im.size, im.mode)
X, Y = im.size
for y in range(0, Y):
    for x in range(0, X):
        # get pixel RGB
        rgb = im.getpixel((x,y))
        # search if existing
        iExisting = None
        for i, color in enumerate(colors):
            if color['rgb'] == rgb:
                iExisting = i
        if not iExisting:
            colors.append({
                'rgb':rgb,
                'count':1,
            })
        else:
            colors[iExisting]['count'] += 1

print('Nb colors:', len(colors))
[print(c) for c in sorted(colors, key=lambda x: x['count'])]


im = Image.open("samples/04.png")
print(im.format, im.size, im.mode)
X, Y = im.size
for y in range(0, Y):
    for x in range(0, X):
        # get pixel RGB
        rgb = im.getpixel((x,y))
        # search if existing
        iExisting = None
        for i, color in enumerate(colors):
            if color['rgb'] == rgb:
                print('existing RGB:', rgb)
