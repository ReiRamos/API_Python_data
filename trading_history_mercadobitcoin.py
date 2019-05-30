import requests

r = requests.get('https://www.mercadobitcoin.net/api/BTC/trades').json()


for d in r:
  dt = d['date']
  p = d['price']
  a = d['amount']
  tid = d['tid']
  ty = d['type']
  print(f'Date: {dt} \nPrice: {p} \nAmount: {a} \nTransaction ID: {tid} \nType: {ty}')
  print()