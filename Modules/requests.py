import requests

request_bbc = requests.get('https://www.bbc.co.uk/', auth=('user', 'pass'))

print(request_bbc.content)
