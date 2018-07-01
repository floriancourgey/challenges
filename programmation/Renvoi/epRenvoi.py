#!/usr/bin/python
# -*- coding: utf-8 -*-
import cookielib, urllib, urllib2

login = 'LE LOGIN'
password = 'LE MOT DE PASSE'

# On active le support des cookies pour urllib2
cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

# On envoie le login et le password à la première page du site qui nous renvoie un cookie de session
values = {'user':login, 'passwrd':password}
data = urllib.urlencode(values)
request = urllib2.Request("https://www.01001110011001010111011101100010011010010110010101100011011011110110111001110100011001010111001101110100.org/forums/index.php?action=login2", data)
url = urlOpener.open(request)  # Notre cookiejar reçoit automatiquement les cookies
page = url.read(500000)

# Affecter les valeurs du cookie à une variable.
# CookieName = [cookie.name for cookie in cookiejar]
# CookieValue = [cookie.value for cookie in cookiejar]
# Afficher les valeurs des variables cookie pour voir si il existe.
# print CookieName
# print CookieValue

# On fait une nouvelle requête sur la deuxième page du site avec le cookie de session qui a été récupéré lors de l'écoute des cookies lors du passage de la première à la deuxième page depuis un navigateur web.
url = urlOpener.open('http://www.01001110011001010111011101100010011010010110010101100011011011110110111001110100011001010111001101110100.org/epreuves/prog/prog1.php')

# Renseigner le header avec la valeur du cookie observé pour SMFCookie89 pour pouvoir lire la deuxième page
headers = {'Cookie: SMFCookie89=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2255733%22%3Bi...%22%3Bi%3A2%3Bi%3A1612301728%3Bi%3A3%3Bi%3A0%3B%7D'}
page = url.read(200000)
print page

# Parser la réponse obtenue sur la deuxième page
nombre = page.replace('Le nombre aléatoire pour valider ta réponse est : ',)

# Stocker la réponse pour être sur qu'on l'ait bien récupérée.
# fichier = open("data.txt", "a")
# fichier.write(nombre)
# fichier.close()

# Concaténer le nombre de la réponse à l'url suivante pour valider la réponse.
# https://www.01001110011001010111011101100010011010010110010101100011011011110110111001110100011001010111001101110100.org/epreuves/prog/verifpr1.php?solution=nombre
resolu = "https://www.01001110011001010111011101100010011010010110010101100011011011110110111001110100011001010111001101110100.org/epreuves/prog/verifpr1.php?solution="+str(nombre)
print resolu

## Consulter l'adresse URL pour valider la réponse.
validation = urlOpener.open(resolu)
validation = validation.read(100000)
print validation

# Un message s'affiche à l'écran pour valider le challenge :
# ['838fa4cdea5d...3145a98f20df9ee', 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2255733%22%3Bi...%22%3Bi%3A2%3Bi%3A1612301728%3Bi%3A3%3Bi%3A0%3B%7D']
# Le nombre aléatoire pour valider ta réponse est : 27....115
# https://www.01001110011001010111011101100010011010010110010101100011011011110110111001110100011001010111001101110100.org/epreuves/prog/verifpr1.php?solution=27....115
# <h3 align="center">Bravo, tu as réussi l'épreuve !</h3><br /><p>Pour valider l'épreuve, le mot de passe est : ******
# Utiliser un navigateur pour aller sur votre compte, dans la partie Challenge, pour valider l'épreuve Renvoi en saisissant le mot de passe reçu dans le terminal.

# Source du tutoriel : https://www.visionduweb.eu/wiki/index.php?title=Utiliser_python#Challenge_de_Connexion_Web_avec_Python
# Challenge sur le site officiel : https://www.01001110011001010111011101100010011010010110010101100011011011110110111001110100011001010111001101110100.org
