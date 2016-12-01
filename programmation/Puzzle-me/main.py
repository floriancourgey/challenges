#! /usr/bin/env python
# coding: utf-8

l_px = 120 # largeur en pixels
h_px = 120 # hauteur en pixels
l_n = 6 # nombre de pièces en largeur
h_n = 6 # nombre de pièces en hauteur

# get image
import urllib2
from PIL import Image
import StringIO
import config
import time

url = 'https://www.newbiecontest.org/epreuves/prog/prog15.php'
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', config.COOKIE))
print('Chargement de '+url)
img = opener.open(url).read()
time1 = time.clock()
print("Chargé")
try:
    im1 = Image.open(StringIO.StringIO(img))
    # im1.verify()
except Exception, e:
    print("erreur",e)
    exit()
print("Image ok, ouverture..")
im1.show()
print("Lancement des bails")


# im1 = Image.open("img_puzzle.png")
# im1 = Image.open("exemple3.png")
im2 = Image.new("RGB", (120, 120))
im3 = Image.new("RGB", (120, 120))

# copie la région(x1;y1) de im1 dans (x2;y2) de im2
def copier1dans2(x1,y1, x2,y2):
    im2.paste(regions1[y1][x1], (20*x2,20*y2,20*x2+20,20*y2+20))
def copier2dans3(x1,y1, x2,y2):
    im3.paste(regions2[y1][x1], (20*x2,20*y2,20*x2+20,20*y2+20))
def copier1dans3(x1,y1, x2,y2):
    im3.paste(regions1[y1][x1], (20*x2,20*y2,20*x2+20,20*y2+20))
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
def moyenne(pixels1, pixels2):
    differences = []
    for i in range(0, 20):
        differences.append( abs(pixels1[i][0] - pixels2[i][0]) )
        differences.append( abs(pixels1[i][1] - pixels2[i][1]) )
        differences.append( abs(pixels1[i][2] - pixels2[i][2]) )
        # if i < 3:
            # print("r : "+str(pixels1[i][0])+"-"+str(pixels2[i][0])+"="+str(abs(pixels1[i][0] - pixels2[i][0])))
    return sum(differences)/3/20

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
                copier1dans2(x,y,0,0)
                regions_ok.append((x,y))
            elif is_border(border_est(x,y)):
                copier1dans2(x,y,5,0)
                regions_ok.append((x,y))
        elif is_border(border_sud(x, y)):
            if is_border(border_ouest(x,y)):
                copier1dans2(x,y,0,5)
                regions_ok.append((x,y))
            elif is_border(border_est(x,y)):
                copier1dans2(x,y,5,5)
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
            copier1dans2(x,y,compteur_nord,0)
            compteur_nord=compteur_nord+1
            regions_ok.append((x,y))
        elif is_border(border_sud(x,y)):
            copier1dans2(x,y,compteur_sud,5)
            compteur_sud=compteur_sud+1
            regions_ok.append((x,y))
        elif is_border(border_ouest(x,y)):
            copier1dans2(x,y,0,compteur_ouest)
            compteur_ouest=compteur_ouest+1
            regions_ok.append((x,y))
        elif is_border(border_est(x,y)):
            copier1dans2(x,y,5,compteur_est)
            compteur_est=compteur_est+1
            regions_ok.append((x,y))

# création régions2
regions2 = []
for y in range(0,6):
    regions_horizontales = []
    for x in range(0,6):
        regions_horizontales.append(im2.crop((20*x, 20*y, 20*x+20, 20*y+20)))
    regions2.append(regions_horizontales)
# copie des angles
copier2dans3(0,0, 0,0)
copier2dans3(0,5, 0,5)
copier2dans3(5,0, 5,0)
copier2dans3(5,5, 5,5)

# on ordonne les bordures nord/sud
for latitude in (0,5):
    # on répète pour chaque région
    regionsFaites = []
    for j in range(1,5):
        # on compare la border_est de l'angle gauche avec la border_ouest de chaque région
        index_min = -1
        moyenne_min = 999
        for i in range (1,5):
            if i in regionsFaites:
                continue
            print("Région "+str(i))
            moyenne_actuelle = moyenne(border_est(j-1,latitude,im3), border_ouest(i,latitude,im2))
            print("Moyenne "+str(moyenne_actuelle))
            if moyenne_min > moyenne_actuelle:
                moyenne_min = moyenne_actuelle
                index_min = i
                # print(moyenne_min)
        print(index_min)
        regionsFaites.append(index_min)
        # on copie sur im3
        copier2dans3(index_min,latitude, j,latitude)
# on ordonne les bordures ouest/est
for longitude in (0,5):
    # on répète pour chaque région
    regionsFaites = []
    for j in range(1,5):
        # on compare la border_sud de l'angle gauche avec la border_nord de chaque région
        index_min = -1
        moyenne_min = 999
        for i in range (1,5):
            if i in regionsFaites:
                continue
            print("Région "+str(i))
            moyenne_actuelle = moyenne(border_sud(longitude,j-1,im3), border_nord(longitude,i,im2))
            print("Moyenne "+str(moyenne_actuelle))
            if moyenne_min > moyenne_actuelle:
                moyenne_min = moyenne_actuelle
                index_min = i
                # print(moyenne_min)
        print(index_min)
        regionsFaites.append(index_min)
        # on copie sur im3
        copier2dans3(longitude,index_min, longitude,j)
# im3.show()
# exit()
# love
for x_master in range(1,5):
    for y_master in range(1,5):
        # on compare les bordures ouest et nord
        x_ok = -1
        y_ok = -1
        moyenne_min = 9999
        for y in range(0,6):
            for x in range(0,6):
                if (x,y) in regions_ok:
                    continue
                moyenne_nord_actuelle = moyenne( border_sud(x_master,y_master-1,im3), border_nord(x,y,im1) )
                moyenne_ouest_actuelle = moyenne( border_est(x_master-1,y_master,im3), border_ouest(x,y,im1) )
                print(x,y,moyenne_nord_actuelle,moyenne_ouest_actuelle)
                if moyenne_min > moyenne_nord_actuelle+moyenne_ouest_actuelle:
                    moyenne_min = moyenne_nord_actuelle+moyenne_ouest_actuelle
                    x_ok = x
                    y_ok = y
        copier1dans3(x_ok,y_ok,x_master,y_master)
        regions_ok.append((x_ok,y_ok))
time2 = time.clock()
print('Terminé en '+str(time2-time1)+'s')
# im2.show()
im3.show()
# im3.save('exemple2-magnifique.png')
# im2.save('out.png')
#
