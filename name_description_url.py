import requests

r = requests.get('http://apis.io/api/apis').json()

for d in r['data']:
  n = d['name']
  de = d['description']
  u = d['baseURL']
  print(f'Name: {n} \nDescription: {de} \nURL: {u}')
  print()