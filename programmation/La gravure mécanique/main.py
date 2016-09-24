#! /usr/bin/python
# coding: utf-8

"""
Florian Courgey
"""

# imports
import urllib2
import re
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import config

# constantes
url = 'https://www.newbiecontest.org/epreuves/prog/proggravure.php/'

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', config.COOKIE))
print('Chargement de '+url)
html = opener.open(url).read().decode("utf-8")
print('html reçu')
html = html.replace("O1234(GRAVURE)", "")
html = html.replace("G28G91Z0.Y0.", "")
html = html.replace("M6T1", "")
html = html.replace("G0G90G54X0.Y0.M3S7500F250.", "")
html = html.replace("G43H1Z2.M8", "")
html = html.replace("G1Z-.1F125.", "")
html = html.replace("G0Z2.", "")
print('html assaini')
regex = "(?P<cle>[GXY])(?P<valeur>[\d\.\-]+)"
facteur = 10;
# liste de tous les x pour avoir leur min/max
xListe = []
xMin = 0*facteur
xMax = 60*facteur
# liste de tous les y pour avoir leur min/max
yListe = []
yMin = -4*facteur
yMax = 11*facteur
# liste des clés/valeurs
liste = []

class SimpleClass(object):
    def __str__(self):
     return self.cle+":"+str(self.valeur)

for match in re.finditer(regex, html):
    cleRaw = match.group('cle')
    valeurRaw = match.group('valeur')
    cle = cleRaw
    valeur = float(valeurRaw)*facteur
    objet = SimpleClass();
    objet.cle = cle;
    objet.valeur = valeur;
    liste.append(objet)
    if cle == "X":
        xListe.append(valeur)
    if cle == "Y":
        yListe.append(valeur)
print('liste buildée')
print(str(min(xListe))+' < x < '+str(max(xListe)))
print(str(min(yListe))+' < y < '+str(max(yListe)))
print(html)

# GUI



def on_draw(widget, cr):
    print('on_draw')
    cr.set_source_rgb(0.6, 0.6, 0.6)
    cr.set_line_width(.2*facteur)

    # cr.line_to(100,100)
    xBase = 0
    yBase = 0
    xBaseADefinir = True
    yBaseADefinir = True

    xPrecedent = 0
    yPrecedent = 0

    gPrecedent = False

    i = 0;

    for objet in liste:
        # print(objet)
        if objet.cle == "G":
            # cht couleur
            cr.set_source_rgba(i*0.1, 0.6, 0.6, 0.2)
            # tracé
            cr.stroke()
            # incrémentation lettre
            i += 1
            print ("i "+str(i))
            # il faut redéfinir la base (x;y)
            xBaseADefinir = True
            yBaseADefinir = True
        else:
            if objet.cle == "X":
                # si base à définir,
                # - on set le x de la base
                # - on move_to x
                if xBaseADefinir:
                    xBase = objet.valeur
                    xBaseADefinir = False
                    cr.move_to(xBase, yPrecedent)
                    xPrecedent = xBase
                # sinon on line_to
                else:
                    cr.line_to(xBase + objet.valeur, yPrecedent)
                    xPrecedent = xBase + objet.valeur
            elif objet.cle == "Y":
                # si base à définir,
                # - on set le y de la base
                # - on move_to y
                if yBaseADefinir:
                    yBase = objet.valeur
                    yBaseADefinir = False
                    cr.move_to(xPrecedent, yBase)
                    yPrecedent = yBase
                # sinon on line_to
                else:
                    cr.line_to(xPrecedent, yBase + objet.valeur)
                    yPrecedent = yBase + objet.valeur




    # cr.move_to(240, 40)
    # cr.line_to(240, 160)
    # cr.line_to(350, 160)
    # cr.fill()
    #
    # cr.move_to(380, 40)
    # cr.line_to(380, 160)
    # cr.line_to(450, 160)
    # cr.curve_to(440, 155, 380, 145, 380, 40)


def main():
    builder = Gtk.Builder()
    builder.add_from_file("main.glade")
    win = builder.get_object("mainWindow")
    win.set_size_request(1280,640)


    zone = builder.get_object("zoneDeDessin")
    zone.connect('draw', on_draw);

    win.connect("delete-event", Gtk.main_quit)

    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
