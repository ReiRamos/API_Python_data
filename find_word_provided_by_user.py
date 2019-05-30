import requests

r = requests.get('http://apis.io/api/apis').json()

word = input('Type the word you\'re looking for: ')

count = 0

for d in r['data']:
  count += 1
  n = d['name']
  de = d['description']
  u = d['baseURL']
  if word in n:
    print(f'Name: {n} \nDescription: {de} \nURL: {u}')
    print()
  if word in de:
    print(f'Name: {n} \nDescription: {de} \nURL: {u}')
    print()
  if word in u:
    print(f'Name: {n} \nDescription: {de} \nURL: {u}')
    print()
  else:
    print('Word not found in dictionary '+ str(count))
    print()
  