#! /usr/bin/env python3
# coding: utf-8
import sys
sys.path.insert(0, '../..')
from pyquery import PyQuery as pq
from functions import *
from bar import Bar
from datetime import datetime

# d = pq(filename='sample1.html')
# filename = 'samples/'+datetime.now().isoformat().replace(':', '')+'.html'
# local_file = open(filename, "w", encoding="utf-8")
html = get(config.URLS['prog']['bars']['problem'], True).content.decode('utf-8')
d = pq( html )
# print(html)
# save to file
# local_file.write(html)

bars = {}
drinks = [] # drinks taken
NB_DRINKS = 10 # 10 drinks per bar

body = d('html>body')
# get bars list
lines = body.find("table.map>tr")
for y,line in enumerate(lines):
    cells = d(line).find('td')
    for x, cell in enumerate(cells):
        text = d(cell).text().strip()
        if len(text) == 0:
            continue
        barId = int(text)
        bars[barId] = Bar(barId, x, y)
if len(bars)<10:
    raise ValueError('Incorrect number of bars')
# print(bars)
# get first bar
FIRST_BAR_ID = int(body.find('span.bar_initial').text())
if FIRST_BAR_ID < 1:
    raise ValueError('Incorrect value for initial bar')
print('Initial bar:', FIRST_BAR_ID)
# get drinks list
for li in body.find('ul.consos>li'):
    drinks.append(d(li).text())
if len(drinks)<10:
    raise ValueError('Incorrect number of drinks')
print('Drinks taken:', len(drinks), drinks)
# get drinks price for each bar
menus = body.find('table.menu')
for i,menu in enumerate(menus):
    for tr in d(menu).find('tr'):
        dTr = d(tr)
        name = dTr.find('td.boisson').text()
        price = int(dTr.find('td.prix').text().replace('€', '').strip())
        bars[i+1].addDrinkToMenu(name, price)
# check each bar should have the same number of drinks
for id,bar in bars.items():
    if len(bar.menu) != NB_DRINKS:
        raise ValueError('Invalid number of drinks for bar', bar)

def getProbas(bars, currentBar, nextDrink):
    probas = []
    for id,bar in bars.items():
        # ignore current bar
        if bar == currentBar:
            continue
        # get distance + price
        distance = float(currentBar.distanceToBar(bar))
        price = float(bar.menu[nextDrink])
        Pdistance = round(1 / distance, 2)
        Pprice = round(1 / proba['priceAbs'], 2)
        Px = round(Pdistance * Pprice, 2)
        probas.append({'id':id,'Px':Px})
    maxProba = max(probas, key=lambda x: x.Px)
    return maxProba

solution = [str(FIRST_BAR_ID)]
currentBar = bars[FIRST_BAR_ID]
for drink in drinks[1:]:
    print('- Get Proba for drink:', drink, 'and currentBar:', currentBar)
    maxProba = getProbas(bars, currentBar, drink)
    print('maxProba:', maxProba)
    currentBar = maxProba['bar']
    solution.append(str(currentBar.id))
print(len(solution))
solution = '-'.join(solution)
print(solution)
html = get(config.URLS['prog']['bars']['solution']+'?sequence='+solution)
print(html)
