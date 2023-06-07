from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    global msg1
    a = ''
    url = 'https://www.banki.ru' # передаем необходимый URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    allCars = soup.find('div', class_='trades-informer')  # всё вышеперечисленное, плюс краткое описание
    dollars = allCars.findAll('span')[1].text
    dollars = dollars.replace("\n", "")
    for data in dollars:
        a += (dollars)
        break
    msg1=float(a)
    print(msg1)
