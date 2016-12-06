#! /usr/bin/env python
# coding: utf-8

import urllib2
import config
import re
import time

urlBase = "https://www.newbiecontest.org/epreuves/prog/"
urlEnonce = urlBase+"progcrawlme.php"
regex = r'href="([\w\/\.\d]+)"'
phraseTropRapide = 'TROP RAPIDE ! HOP, ON RECOMMENCE !!'
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', config.COOKIE))
# print('Chargement de '+urlEnonce)
# html = opener.open(urlEnonce).read()
# dossier = re.findall(regex, html)[0].replace('./','')
# print(dossier)
#
# time.sleep(.6)
# print("Chargement de "+urlBase+dossier)
# html = opener.open(urlBase+dossier).read()
# print(html)
# dossiers = re.findall(regex, html)
# print(dossiers)

def crawl(url):
    print('wait...')
    time.sleep(.72)
    if not url.endswith('.php') and not url.endswith('/'):
        url = url + '/'
    print('Appel '+url)
    html = opener.open(url).read()
    if html == phraseTropRapide:
        exit('Trop rapide...')
    dossiers = re.findall(regex, html)
    print(str(len(dossiers))+' dossier trouves', dossiers)
    for dossier in dossiers:
        dossier = dossier.replace('./', '')
        if url.endswith('.php'):
            crawl(urlBase+dossier)
        else:
            crawl(url+dossier)

time1 = time.time()
crawl(urlEnonce)
time2 = time.time()
print('Terminé en '+str(time2-time1)+'s')
