"""
1. На сайте расположена таблица;
2. Цель: Собрать числа с 1го столбца и суммировать их;
3. Полученный результат вставить в поле ответа.
"""
import requests
from bs4 import BeautifulSoup

nums = []
url = "https://parsinger.ru/table/1/index.html"
r = requests.get(url=url)
soup = BeautifulSoup(r.text, 'lxml')
total = 0
for row in soup.find_all('tr')[1:]:  # исключаем первую строку с заголовками
    cells = row.find('td')
    try:
        number = float(cells.text.strip())
        total += number
    except ValueError:
        pass

print(total)