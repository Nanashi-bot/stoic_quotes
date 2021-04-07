import requests
import json
import random

url = 'https://randomstoicquotesapi.herokuapp.com/api/v1/quotes'
headers = {
    'Accept': 'application/vnd.api+json',
}
response = requests.get(url, headers=headers)
data = response.json()

x = random.randint(0, 31)
author_id = data['data'][x]['relationships']['author']['data']['id']
for i in range(0, 7):
    if author_id == data['included'][i]['id']:
        author = data['included'][i]['attributes']['name']
        break

quote = data['data'][x]['attributes']['text']

print(quote)
print(author)
