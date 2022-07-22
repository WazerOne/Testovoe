import random

import requests
from bs4 import BeautifulSoup as BS

animals = []             # Список всех животных
letter_counter = {}      # Словарь с первыми буквами животных и их кол-вом
href = "/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
while href:
    url = "https://ru.wikipedia.org"+href
    req = requests.get(url)
    data = BS(req.text, 'html.parser')
    strings = data.find('div', {'id': 'mw-pages'}).find(class_='mw-category-group').find_all('li')
    for animal in strings:
        animals.append(animal.text)
        temp = animal.text[0]
        if temp == 'A':                                           # Отсекаем англоязычные названия
            break
        if temp not in letter_counter:                            # Вносим буквы которых ещё не попадалось
            letter_counter[temp] = letter_counter.get(temp, 0)
        letter_counter[temp] += 1
    if temp == 'A':
        break                                                     # Переходим на следующую страницу с помощью href
    if data.find('div', {'id': 'mw-pages'}).find('a', href=True, text='Следующая страница'):
        href = data.find('div', {'id': 'mw-pages'}).find('a', href=True, text='Следующая страница')['href']
    else:
        break


for k in sorted(letter_counter.keys()):                            # Сортируем полученный результат и получаем ответ
    print(k, ':', letter_counter[k])                               # на поставленную задачу
