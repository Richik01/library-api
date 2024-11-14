import requests

url = 'http://127.0.0.1:8000/books'

res = requests.get(url)
print(res.json())