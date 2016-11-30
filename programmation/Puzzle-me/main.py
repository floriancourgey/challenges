#! /usr/bin/env python
# coding: utf-8

l_px = 120 # largeur en pixels
h_px = 120 # hauteur en pixels
l_n = 6 # nombre de pièces en largeur
h_n = 6 # nombre de pièces en hauteur

from PIL import Image
im1 = Image.open("prog15.png")
im2 = Image.new("RGB", (120, 120))

def copier(x1,y1, x2,y2):
    im2.paste(regions1[y1][x1], (20*x2,20*y2,20*x2+20,20*y2+20))
def is_border(pixels):
    for r,g,b in pixels:
        if r!=0 and g!=0 and b!=255:
            return False
    return True;
def border_nord(x,y, im=im1):
    pixels = []
    for k in range(0, 20):
        pixels.append(im.getpixel((x*20+k, y*20)))
    return pixels
def border_sud(x,y, im=im1):
    pixels = []
    for k in range(0, 20):
        pixels.append(im.getpixel((x*20+k, y*20+19)))
    return pixels
def border_ouest(x,y, im=im1):
    pixels = []
    for k in range(0, 20):
        pixels.append(im.getpixel((x*20, y*20+k)))
    return pixels
def border_est(x,y, im=im1):
    pixels = []
    for k in range(0, 20):
        pixels.append(im.getpixel((x*20+19, y*20+k)))
    return pixels
def pixels_proches(pixels1, pixels2):
    differences = []
    for i in range(0, 20):
        differences[i*3] = abs(pixels1[i][0] - pixels2[i][0])
        differences[i*3+1] = abs(pixels1[i][1] - pixels2[i][1])
        differences[i*3+2] = abs(pixels1[i][2] - pixels2[i][2])
    print(sum(differences)/3/20)
    # return
regions1 = []
regions_ok = []
for y in range(0,6):
    regions_horizontales = []
    for x in range(0,6):
        regions_horizontales.append(im1.crop((20*x, 20*y, 20*x+20, 20*y+20)))
    regions1.append(regions_horizontales)
# print(regions1)
# on fait les angles
for y in range(0,6):
    for x in range(0,6):
        if is_border(border_nord(x, y)):
            if is_border(border_ouest(x,y)):
                copier(x,y,0,0)
                regions_ok.append((x,y))
            elif is_border(border_est(x,y)):
                copier(x,y,5,0)
                regions_ok.append((x,y))
        elif is_border(border_sud(x, y)):
            if is_border(border_ouest(x,y)):
                copier(x,y,0,5)
                regions_ok.append((x,y))
            elif is_border(border_est(x,y)):
                copier(x,y,5,5)
                regions_ok.append((x,y))
# bordures désordonnées
compteur_nord = 1
compteur_sud = 1
compteur_ouest = 1
compteur_est = 1
for y in range(0,6):
    for x in range(0,6):
        if (x,y) in regions_ok:
            continue
        if is_border(border_nord(x,y)):
            copier(x,y,compteur_nord,0)
            compteur_nord=compteur_nord+1
        elif is_border(border_sud(x,y)):
            copier(x,y,compteur_sud,5)
            compteur_sud=compteur_sud+1
        elif is_border(border_ouest(x,y)):
            copier(x,y,0,compteur_ouest)
            compteur_ouest=compteur_ouest+1
        elif is_border(border_est(x,y)):
            copier(x,y,5,compteur_est)
            compteur_est=compteur_est+1



# copier(1,1, 2,2)
im2.show()
#

# def border_nord(x,y):
#     pixels = []
#     for k in range(0, 20):
#         pixels.append(in.getpixel((x*20+k, y*20)))
#     return pixels
# def is_border(pixels):
#     for r,g,b in pixels:
#         if r!=0 and g!=0 and b!=255:
#             return False
#     return True;

# # on résoud la première ligne
# # on cherche toutes les pièces avec une bordure en haut
# for y in range(0, 6):
#     for x in range(0, 6):
#         #  on get la bordure haute
#         print('('+str(x)+';'+str(y)+') : '+ str(is_border_nord(x,y)))

# out = im.point(lambda i:i*5000)
# out.save("test.bmp")
