#! /usr/bin/env python
# coding: utf-8
from __future__ import print_function
import urllib2
import config
import re
import time
import hashlib

# on est en base62_encode car 10 chiffres + 26 lettres + 26 lettres
# on compte comme ça : 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
# c'est du pseudo base62 car a00 est devant a0000
def base62_encode(string):
    nombre = 0;
    for i, lettre in enumerate(string):
        ascii = ord(lettre)
        if lettre.isdigit():
            ascii += -ord('0')
        elif lettre.isupper():
            ascii += -ord('A') + (ord('9')-ord('0')+1)
        elif lettre.islower():
            ascii += -ord('a') + (ord('Z')-ord('A')+1) + (ord('9')-ord('0')+1)
        # on est en pseudo base62, on devrait avoir len(string)-i au lieu de 10-i pour un vrai base62
        # 10 est pris car c'est la taille la plus grande que j'ai trouvée
        # 10-i revient à convertir a00 en a000000000 (zero-padding à droite)
        nombre += ascii * 62 ** (10-i)
    return nombre
# custom sort utilisant la base62
def ordonner(dossier1, dossier2):
    base62_encode1 = base62_encode(dossier1)
    base62_encode2 = base62_encode(dossier2)
    if base62_encode1 < base62_encode2:
        return -1
    elif base62_encode1 > base62_encode2:
        return 1
    else:
        return 0
# prend une liste de dossiers
# et retourne le md5 de la solution
def solution(dossiers):
    dossiersOrdonnes = sorted(dossiers, cmp=ordonner)
    print("=== dossiers ordonnés ===")
    print(dossiersOrdonnes)
    m = hashlib.md5()
    m.update("".join(dossiersOrdonnes))
    return m.hexdigest()

# tests unitaires
print("=== TESTS UNITAIRES ===")
dossiers = ['n7th00a', 'b7xs7cD', 'S08gBv4', '2ZxpmmP']
if solution(dossiers) != 'f5d1733a19d66c3d4d42b84433804b33':
    print('algo de sort invalide')
    exit(-1)

urlBase = "https://www.newbiecontest.org/epreuves/prog/"
urlEnonce = urlBase+"progcrawlme.php"
urlValidation = urlBase+"verifprogcrawlme.php?md5="
regex = r'href="([\w\/\.\d]+)"'
phraseTropRapide = 'TROP RAPIDE ! HOP, ON RECOMMENCE !!'
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', config.COOKIE))

dossiers = []
# crawl
# profondeur est juste utilisé pour un joli affichage
def crawl(url, profondeur=0):
    # attente
    time.sleep(.74)
    # fix slash de fin
    if not url.endswith('.php') and not url.endswith('/'):
        url = url + '/'
    # appel http
    html = opener.open(url).read()
    # check trop rapide
    if html == phraseTropRapide:
        exit('Trop rapide...')
    # recherche dossiers
    dossiersTrouves = re.findall(regex, html)
    for dossier in dossiersTrouves:
        # fix ./
        dossier = dossier.replace('./', '')
        # ajout à la liste des dossiers
        dossiers.append(dossier)
        # joli affichage
        for i in range(0,profondeur):
            print("   ", end="")
        print("|")
        for i in range(0,profondeur):
            print("   ", end="")
        print("-"+dossier+"     ("+url+")")
        # crawl
        if url.endswith('.php'):
            crawl(urlBase+dossier, profondeur+1)
        else:
            crawl(url+dossier, profondeur+1)

print("=== LANCEMENT CRAWL ===")
time1 = time.time()
crawl(urlEnonce)

# nettoyage de nos dossiers
for i, dossier in enumerate(dossiers):
    dossiers[i] = dossier.replace("/", "").replace("crawlme", "").replace(".", "")

print("=== "+str(len(dossiers))+" dossiers ===")
print(dossiers)
solution = solution(dossiers)
print("=== md5 ===")
print(solution)
url = urlValidation+solution
time2 = time.time()
print("=== envoi solution ===")
print("Appel "+url+ " au bout de "+str(time2-time1)+"s")
print(opener.open(url).read())
