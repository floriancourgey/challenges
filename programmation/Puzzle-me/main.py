#! /usr/bin/env python2
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

urlPuzzle = 'https://www.newbiecontest.org/epreuves/prog/prog15.php'
urlValidation = 'https://www.newbiecontest.org/epreuves/prog/verifpr15.php?chaine='

# ouverture puzzle
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', config.COOKIE))
print('Chargement de '+urlPuzzle)
img = opener.open(urlPuzzle).read()
time1 = time.clock()
print("Chargé")
try:
    imPuzzle = Image.open(StringIO.StringIO(img))
except Exception, e:
    print("erreur", e)
    exit()
print("Image ok, ouverture..")
imPuzzle.show()
print("Lancement des bails")


# imPuzzle = Image.open("img_puzzle.png")
imResolue = Image.new("RGB", (120, 120))

# permet de ne pas parser les régions déjà placées
regions_deja_placees = []

# table de correspondance utilisée pour renvoyer la solution
table_de_correspondance = [[(-1,-1) for i in range(6)] for j in range(6)]

# objet mathématique box
def box(x,y):
    return (20*x, 20*y, 20*x+20, 20*y+20)
# region pillow
def region(x,y,img):
    return img.crop(box(x,y))
# copier imPuzzle(x1,y1) dans im2(x2,y2)
def copier(x1,y1,imPuzzle, x2,y2,im2):
    # copie
    im2.paste(region(x1,y1,imPuzzle), box(x2,y2))
    # ajout dans les régions placées
    regions_deja_placees.append((x,y))
    # ajout dans la table de correspondance
    table_de_correspondance[y1][x1] = (x2, y2)

def is_border(pixels):
    for r,g,b in pixels:
        if r!=0 and g!=0 and b!=255:
            return False
    return True;
def border_nord(x,y, im=imPuzzle):
    pixels = []
    for k in range(0, 20):
        pixels.append(im.getpixel((x*20+k, y*20)))
    return pixels
def border_sud(x,y, im=imPuzzle):
    pixels = []
    for k in range(0, 20):
        pixels.append(im.getpixel((x*20+k, y*20+19)))
    return pixels
def border_ouest(x,y, im=imPuzzle):
    pixels = []
    for k in range(0, 20):
        pixels.append(im.getpixel((x*20, y*20+k)))
    return pixels
def border_est(x,y, im=imPuzzle):
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
    return sum(differences)/3/20

# on place les angles (et en même temps, on met de côté toutes les bordures)
regions_nord = []
regions_sud = []
regions_ouest = []
regions_est = []
for y in range(0,6):
    for x in range(0,6):
        if is_border(border_nord(x, y)):
            # placement angle N/O
            if is_border(border_ouest(x,y)):
                copier(x,y,imPuzzle ,0,0,imResolue)
            # placement angle N/E
            elif is_border(border_est(x,y)):
                copier(x,y,imPuzzle ,5,0,imResolue)
            # bordure nord
            else:
                regions_nord.append((x,y))
        elif is_border(border_sud(x, y)):
            # placement angle S/O
            if is_border(border_ouest(x,y)):
                copier(x,y,imPuzzle ,0,5,imResolue)
            # placement angle S/E
            elif is_border(border_est(x,y)):
                copier(x,y,imPuzzle ,5,5,imResolue)
            # bordure sud
            else:
                regions_sud.append((x,y))
        # bordure ouest
        elif is_border(border_ouest(x,y)):
            regions_ouest.append((x,y))
        # bordure_est
        elif is_border(border_est(x,y)):
            regions_est.append((x,y))

# on ordonne les regions de la bordure nord (et sud avec le paramètre latitude)
for latitude in (0,5):
    for j in range(1,5):
        couple_ok = (-1,-1)
        moyenne_min = 999
        regions = regions_nord if (latitude == 0) else regions_sud;
        for (x,y) in regions:
            moyenne_actuelle = moyenne(border_est(j-1,latitude,imResolue), border_ouest(x,y,imPuzzle))
            if moyenne_min > moyenne_actuelle:
                moyenne_min = moyenne_actuelle
                couple_ok = (x,y)
        copier(couple_ok[0],couple_ok[1],imPuzzle, j,latitude,imResolue)

# on ordonne les regions de la bordure ouest (et est avec le paramètre longitude)
for longitude in (0,5):
    for j in range(1,5):
        couple_ok = (-1,-1)
        moyenne_min = 999
        regions = regions_ouest if (longitude == 0) else regions_est;
        for (x,y) in regions:
            moyenne_actuelle = moyenne(border_sud(longitude,j-1,imResolue), border_nord(x,y,imPuzzle))
            if moyenne_min > moyenne_actuelle:
                moyenne_min = moyenne_actuelle
                couple_ok = (x,y)
        copier(couple_ok[0],couple_ok[1],imPuzzle, longitude,j,imResolue)

# enfin, il reste à matcher chaque région restante
for x_master in range(1,5):
    for y_master in range(1,5):
        # on compare les bordures ouest et nord
        couple_ok = (-1,-1)
        moyenne_min = 9999
        for y in range(0,6):
            for x in range(0,6):
                if (x,y) in regions_deja_placees:
                    continue
                moyenne_nord_actuelle = moyenne( border_sud(x_master,y_master-1,imResolue), border_nord(x,y,imPuzzle) )
                moyenne_ouest_actuelle = moyenne( border_est(x_master-1,y_master,imResolue), border_ouest(x,y,imPuzzle) )
                if moyenne_min > moyenne_nord_actuelle+moyenne_ouest_actuelle:
                    moyenne_min = moyenne_nord_actuelle+moyenne_ouest_actuelle
                    couple_ok = (x,y)
        copier(couple_ok[0],couple_ok[1],imPuzzle, x_master,y_master,imResolue)


# SHOW
imResolue.show()

# table de correspondance
solutions = []
print(table_de_correspondance)
for ligne in  table_de_correspondance:
    for correspondance in ligne:
        solutions.append( str(correspondance[0]+correspondance[1]*6) )
solution = "-".join(solutions)
print(solution)

url = urlValidation+solution
print("ouverture de "+url)
html = opener.open(url).read()
print(html)
