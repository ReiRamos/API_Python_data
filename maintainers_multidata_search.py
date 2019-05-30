#-*- coding: utf-8 -*-

import requests

r = requests.get('http://apis.io/api/maintainers').json()

for d in r['data']:
  try:
    n = d['FN']
    e = d['email']
    g = d['github']
    print('------------------------------------------------')
    print(f' name: {n} \n e-mail: {e} \n gitHUB: {g}')
    print()
  except KeyError as e:
    continue

for d in r['data']:  
  try:
    n = d['name']
    e = d['email']
    g = d['github']
    print('------------------------------------------------')
    print(f' name: {n} \n e-mail: {e} \n gitHUB: {g}')
    print()
  except KeyError as t:
    continue