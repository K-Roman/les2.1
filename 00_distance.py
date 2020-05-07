#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

msc=sites['Moscow']
lnd=sites['London']
pr=sites['Paris']
msc_lnd=((msc[0]-lnd[0])**2 +(msc[1]-lnd[1])**2)**0.5
lnd_pr=((lnd[0]-pr[0])**2+(lnd[1]-pr[1])**2)**0.5
pr_msc=((pr[0]-msc[0])**2+(pr[1]-msc[1])**2)**0.5
distances['msc_lnd']=msc_lnd
distances['lnd_pr']=lnd_pr
distances['pr_msc']=pr_msc

pprint(distances)




