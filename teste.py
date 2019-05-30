import requests

r = requests.get('https://apis.io/api/apis')

r.text

print(r.text)