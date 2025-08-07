import requests
from bs4 import BeautifulSoup
from dabase import dabase
from dotenv import load_dotenv
import os

load_dotenv()
dabase = dabase(os.getenv("DATABASE_URL"))

def parcAndInsert():

    url = 'https://www.metrtv.ru/novostroiki'
    response = requests.get(url)
    # if response.status_code == 200:
    #     with open('data/page.html', 'w', encoding='utf-8') as file:
    #         file.write(response.text)
    #     print('Страница успешно сохранена в файл "page.html"') 

    #     # soup_ing = str(BeautifulSoup(r.content, 'lxml'))
    #     # print(soup_ing)
    # else:
    #     raise "ошибка работы с сайтом"


    with open('data/page.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'lxml')
    content = soup.select('div.text > div.desc')
    for text in content:
        cont = text.get_text()
        if cont != "":
            dabase.insertContent(cont)

    print ("insert OK")
parcAndInsert()