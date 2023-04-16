"""
1. Открываем сайт
2. Извлекаем при помощи
3. Складываем все числа bs4 данные о стоимости часов (всего 8 шт)
4. Вставляем результат в поле ответа
"""
from bs4 import BeautifulSoup
import requests
import lxml
url = "https://parsinger.ru/html/index1_page_3.html"
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
tt = []

prices = soup.find_all('p', class_='price') # В класс пишем в каком классе находится описание
total_p = 0
for price in prices:
    price_text = price.get_text()  # Получаем текст элемента
    price_number = int(price_text.replace('руб', '').replace(' ', ''))  # Преобразуем текст в число
    total_p += price_number  # Добавляем число к общей сумме стоимости

print(total_p)  # Выводим общую стоимость