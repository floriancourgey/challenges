#! /usr/bin/env python3
# coding: utf-8
import sys
sys.path.insert(0, '../..')
from pyquery import PyQuery as pq
from functions import *
from bar import Bar
from datetime import datetime

# d = pq(filename='sample1.html')
filename = 'samples/'+datetime.now().isoformat().replace(':', '')+'.html'
local_file = open(filename, "w", encoding="utf-8")
html = get(config.URLS['prog']['bars']['problem'], True).content.decode('utf-8')
d = pq( html )
# print(html)
# save to file
local_file.write(html)

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

def getProbas(bars, previousBar, nextDrink):
    probas = {}
    minDist = 99
    minPrice = 99
    for id,bar in bars.items():
        if bar == previousBar:
            continue
        probas[bar.id] = {
            'bar': bar,
            'distanceAbs':float(previousBar.distanceToBar(bar)), # absolute distance
            'priceAbs':float(bar.menu[nextDrink]), # absolute price
        }
        if probas[bar.id]['distanceAbs'] < minDist:
            closestBar = bar
            minDist = probas[bar.id]['distanceAbs']
        if probas[bar.id]['priceAbs'] < minPrice:
            cheapestBar = bar
            minPrice = probas[bar.id]['priceAbs']
    print('Closest bar:', closestBar, 'with dist=', probas[closestBar.id]['distanceAbs'])
    print('Cheapest bar:', cheapestBar, 'with price '+nextDrink+'=', probas[cheapestBar.id]['priceAbs'])
    # compute relative proba
    maxPx = 0
    for id,proba in probas.items():
        proba['distanceRel'] = round(probas[closestBar.id]['distanceAbs'] / proba['distanceAbs'], 2)
        proba['priceRel'] = round(probas[cheapestBar.id]['priceAbs'] / proba['priceAbs'], 2)
        proba['Px'] = round(proba['distanceRel'] * proba['priceRel'], 2)
        if proba['Px'] > maxPx:
            maxProba = proba
            maxPx = proba['Px']
    # print(probas)
    return maxProba

solution = [str(FIRST_BAR_ID)]
previousBar = bars[FIRST_BAR_ID]
for drink in drinks:
    print('- Get Proba for drink:', drink, 'and bar:', previousBar)
    maxProba = getProbas(bars, previousBar, drink)
    print('maxProba:', maxProba)
    previousBar = maxProba['bar']
    solution.append(str(previousBar.id))
print(len(solution))
solution = '-'.join(solution[:-1])
print(solution)
html = get(config.URLS['prog']['bars']['solution']+'?sequence='+solution)
print(html)
