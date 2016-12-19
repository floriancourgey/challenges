#! /usr/bin/env python3
# coding: utf-8

import config
import requests
import re
import time
from math import sqrt

def get(url):
    print("Appel GET "+url)
    r = requests.get(url, cookies=cookies)
    html = r.text
    print("html reçu", html)
    return html
def post(url, data):
    print("Appel POST "+url, data)
    r = requests.post(url, cookies=cookies, data=data)
    html = r.text
    print("html reçu", html)
    return html

# constantes
cookies = {config.COOKIE_KEY:config.COOKIE_VALUE}
urlBase = 'https://www.newbiecontest.org/epreuves/prog/frok-fichus_nb/'
urlProg1 = urlBase+'prog_1.php'
urlProg1Validation = urlBase+'verif_1.php'
urlProg2 = urlBase+'prog_2.php'
urlProg2Validation = urlBase+'verif_2.php'
urlProg3 = urlBase+'prog_3.php'

# html = "<strong>Bienvenue!</strong><br/><br/>Les sept anagrammes dans l'ordre sont:  0716454-4023366x8527952;6959196'1563139°3531833&8282988<br/><br/>Renvoyez les réponses en moins d'une seco"

# Programme 1
def programme1():
    # ouverture du dico et strip des lignes (car elles contiennent chacune \n)
    dico = []
    with open('anag.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            dico.append(line)

    # appel à l'url
    print("====================")
    print("==== Question 1 ====")
    print("====================")
    html = get(urlProg1)
    print("====================")
    print("====================")
    print("====================")
    matches = re.search(r"sont:\s+(.+)<br/><br/>Renvoyez", html)
    mots = matches.group(1)
    mots = re.findall(r"[\d]+", mots)
    print("mots trouvés : ",mots)
    if(len(mots) != 7):
        print("Erreur, il faut 7 mots")
        exit()

    # recherche des anagrammes
    anagrammes = []
    for mot in mots:
        for anagramme in dico:
            if len(anagramme) == len(mot):
                anagramme_ok = True
                for lettre in mot:
                    if mot.count(lettre) != anagramme.count(lettre):
                        anagramme_ok = False
                        break
                if anagramme_ok:
                    anagrammes.append(anagramme)
                    break
    # envoi de la réponse
    data = {}
    for i,anagramme in enumerate(anagrammes):
        data['rep'+str(i+1)] = anagramme
    html = post(urlProg1Validation, data)
    matches = re.search(r"<br/>Le login est: (.+)\.</body>", html)
    login = matches.group(1)
    print("===================")
    print("==== Réponse 1 ====")
    print("login : "+login)
    print("===================")
    print("===================")
    print()
    return login

# Programme 2
def programme2():
    # get html
    print("====================")
    print("==== Question 2 ====")
    print("====================")
    html = get(urlProg2)
    print("====================")
    print("====================")
    print("====================")
    # matches = re.search(r"(1\).+année\?)", html)
    # questions = matches.group(1)

    # question 1.
    # tout ceci peut se pré-calculer car les données ne changent pas
    # fwords = fibword(45)
    # print("milliardième lettre "+fwords[44][1000000000-1])
    # print("10 lettres avant et 10 lettres après la milliardième : "+fwords[44][1000000000-10:1000000000+10])
    # milliard = fwords[44][0:1000000000]
    # milliard_taille = len(milliard)
    # milliard_nb_hommes = milliard.count('H')
    # milliard_nb_femmes = milliard.count('F')
    # milliard_check = milliard_nb_hommes + milliard_nb_femmes
    # print("len milliard : "+str(milliard_taille)+", nb hommes : "+str(milliard_nb_hommes)+", nb femmes : "+str(milliard_nb_femmes)+', check h+f :'+str(milliard_check))
    # mode normal :
    reponse1_sexe = 'F'
    reponse1_hommes = 381966011
    reponse1_femmes = 618033989

    # avec reverse :
    # reponse1_sexe = 'Femme'
    # reponse1_hommes = 381966011
    # reponse1_femmes = 618033989

    # question 2.
    ## recherche des données :
    matches = re.search(r"extraterrestres pour enlever (\d+) habitants", html)
    nbHabitantsAEnlever = matches.group(1)
    print("2. Combien d'années pour enlever "+nbHabitantsAEnlever+" habitants ?")
    nbHabitantsAEnlever = int(nbHabitantsAEnlever)
    ## calcul réponse :
    reponse2 = get_annees_pour_enlever_n_habitants(nbHabitantsAEnlever)
    print("=> "+str(reponse2)+" années pour enlever "+str(nbHabitantsAEnlever)+" habitants")

    # question 3.
    ## recherche des données :
    matches = re.search(r"captifs durant la (\d+)", html)
    n = matches.group(1)
    print("3. Combien d'habitants enlevés durant la "+n+"ème année ?")
    n = int(n)
    ## calcul réponse
    reponse3 = fibonacci_iteratif(n)
    print("=> "+str(reponse3)+" habitants enlevés sur l'année "+str(n))

    # validation
    data = {
        "rep1":reponse1_sexe,
        "rep2":reponse1_hommes,
        "rep3":reponse1_femmes,
        "rep4":reponse2,
        "rep5":reponse3
    }
    html = post(urlProg2Validation, data=data)
    # matches = re.search(r"<br/>Le login est: (.+)\.</body>", html)
    # login = matches.group(1)
    # print("login : "+login)
# question 1
def fibword(n=38, debug=True):
    # fwords = ['1', '0']
    fwords = ['H', 'F']
    if debug:
        print('%-3s %13s %10s %s' % tuple('N Longueur Secondes Résultat'.split()))
    def pr(n, fwords):
        temps1 = time.time()
        while len(fwords) < n:
            fword = ''.join(fwords[-2:])
            # si reverse order
            # fword = ''.join(fwords[-2:][::-1)
            fwords +=  [fword]
        v = fwords[n-1]
        temps2 = time.time()-temps1
        longueur = format(len(v), ',d')
        secondes = '{0:.2g}'.format(temps2)
        resultat = v if len(v) < 150 else '_'
        if debug:
            print('%3i %13s %10s %s' % (n, longueur, secondes, resultat))
    for n in range(1, n+1): pr(n, fwords)
    return fwords
# question 3
# retourne le nombre d'enlevés sur 1 année (1 indexed)
# préçis
def fibonacci_iteratif(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
# retourne le nombre d'enlevés sur 1 année (1 indexed)
# non préçis
def fibonacci_formule(n):
    return round( ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)) )

def get_annees_pour_enlever_n_habitants(n_habitants):
    n_habitants_total = 0
    n = 0
    while n_habitants_total < n_habitants:
        n += 1
        n_habitants_total += fibonacci_iteratif(n)
        # print("année "+str(n)+" : "+str(n_habitants_total)+" habs enlevés au total")
    return n
def tests_unitaires():
    print('TU fibwords...', end=' ')
    # check fibonacci words
    fwords = fibword(12, False)
    # check année 1
    if fwords[0] != 'H':
        exit('année 1 déconne')
    # check année 2
    if fwords[1] != 'F':
        exit('année 2 déconne')
    # check année 3
    if fwords[2] != 'HF':
        exit('année 3 déconne')
    # check année 4
    if fwords[3] != 'FHF':
        exit('année 4 déconne')
    # check année 5
    if fwords[4] != 'HFFHF':
        exit('année 5 déconne')
    # check année 6
    if fwords[5] != 'FHFHFFHF':
        exit('année 6 déconne')
    # check année 7
    if fwords[6] != 'HFFHFFHFHFFHF':
        exit('année 7 déconne')
    print('OK')

    # on a 2 types de fibonacci :
    # l'approche itérative (précise) et l'approche par formule (non précise
    # car elle repose sur le golden ratio, lui même non précis)
    print('TU fibonacci_iteratif...', end=' ')
    dico = {1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34, 10:55,
        50:12586269025,
        74:1304969544928657,
        100:354224848179261915075}
    for n, resultat_attendu in dico.items():
        resultat_calcule = fibonacci_iteratif(n)
        if resultat_calcule != resultat_attendu:
            exit('fibonacci_iteratif('+str(n)+') déconne : Attendu '+str(resultat_attendu)+' - Calculé '+str(resultat_calcule))
    print('OK')

    # check fibonacci_formule(n) avec http://php.bubble.ro/fibonacci/
    # attention, notre fibonacci_formule(n) utilise la méthode par formule, plutot que la méthode itérative, on est moins préçis
    # on s'en fout de perdre un peu de précision car on ne cherche pas un résultat exact mais une approximation
    # ne pas dépasser nMax=69
    # voir http://mortada.net/fibonacci-numbers-in-python.html
    print('TU fibonacci_formule...', end=' ')
    dico = {1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34, 10:55,
        50:12586269025,
        69:117669030460994}
    for n, resultat_attendu in dico.items():
        resultat_calcule = fibonacci_formule(n)
        if resultat_calcule != resultat_attendu:
            exit('fibonacci_formule('+str(n)+') déconne : Attendu '+str(resultat_attendu)+' - Calculé '+str(resultat_calcule))
    print('OK')

    # combien d'années pour enlever 32 habitants ? 7
    print('TU get_annees_pour_enlever_n_habitants...', end=' ')
    dico = {32:7, 33:7, 34:8, 2971215071:45, 2971215072:45, 2971215073:46}
    for nb_habitants, resultat_attendu in dico.items():
        resultat_calcule = get_annees_pour_enlever_n_habitants(nb_habitants)
        if resultat_calcule != resultat_attendu:
            exit('get_annees_pour_enlever_n_habitants('+str(nb_habitants)+') déconne : Attendu '+str(resultat_attendu)+' - Calculé '+str(resultat_calcule))
    print('OK')

tests_unitaires()
# exit()
programme1()
programme2()

exit()
print('cb H/F sur cent people ? Quel sexe du centième ?')
fwords = fibword(12)

print("sexe du 10eme : "+fwords[6][10-1])
dix = fwords[6][0:10]
dix_taille = len(dix)
dix_nb_hommes = dix.count('H')
dix_nb_femmes = dix.count('F')
dix_check = dix_nb_hommes + dix_nb_femmes
print("len dix : "+str(dix_taille)+", nb hommes : "+str(dix_nb_hommes)+", nb femmes : "+str(dix_nb_femmes)+', check h+f :'+str(dix_check))
print()
print("sexe du 100eme : "+fwords[11][100-1])
cent = fwords[11][0:100]
cent_taille = len(cent)
cent_nb_hommes = cent.count('H')
cent_nb_femmes = cent.count('F')
cent_check = cent_nb_hommes + cent_nb_femmes
print("len milliard : "+str(cent_taille)+", nb hommes : "+str(cent_nb_hommes)+", nb femmes : "+str(cent_nb_femmes)+', check h+f :'+str(cent_check))

# fwords = fibword(45)
# print("milliardième lettre "+fwords[44][1000000000-1])
# print("10 lettres avant et 10 lettres après la milliardième : "+fwords[44][1000000000-10:1000000000+10])
# milliard = fwords[44][0:1000000000]
# milliard_taille = len(milliard)
# milliard_nb_hommes = milliard.count('H')
# milliard_nb_femmes = milliard.count('F')
# milliard_check = milliard_nb_hommes + milliard_nb_femmes
# print("len milliard : "+str(milliard_taille)+", nb hommes : "+str(milliard_nb_hommes)+", nb femmes : "+str(milliard_nb_femmes)+', check h+f :'+str(milliard_check))



#envoi
