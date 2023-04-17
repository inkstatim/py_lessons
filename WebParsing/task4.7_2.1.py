"""
1. На сайте расположена таблица;
2. Цель: Собрать все уникальные числа из таблицы (кроме цифр в заголовке) и суммировать их;
3. Полученный результат вставить в поле ответа.
"""
import requests
from bs4 import BeautifulSoup

nums = []
url = "https://parsinger.ru/table/1/index.html"
r = requests.get(url=url)
soup = BeautifulSoup(r.text, 'lxml')
tab = soup.find('div', class_='main').find_all('td')

unique_numbers = set()
for i in tab:
    try:
        number = float(i.text.strip())
        unique_numbers.add(number)
    except ValueError:
        pass
total = sum(unique_numbers)
print(total)