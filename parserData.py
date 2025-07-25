import requests
from bs4 import BeautifulSoup

url = 'https://midlcode.com/ru/books/?ysclid=mdj0l6iie1411729315'
r = requests.get(url)
soup_ing = str(BeautifulSoup(r.content, 'lxml'))

print(soup_ing)