"""
1. Откройте сайт
2. Извлеките названия товара с каждой страницы (всего 4х страниц)
3. Данные с каждой страницы должны хранится в списке.
4. По итогу работы должны получится 4 списка которые хранятся
5. Отправьте получившийся список списков в поле ответа.
6. Метод strip() использовать не нужно Пример ожидаемого списка в списке (список списков)
"""


from bs4 import BeautifulSoup
import requests

page1 = []
page2 = []
page3 = []
page4 = []

for i in range(1, 5):
    url = f"https://parsinger.ru/html/index3_page_{i}.html"
    r = requests.get(url=url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')

    if i == 1:
        page1 = [name.text for name in soup.find('div', class_="item_card").find_all('a', class_='name_item')]
    elif i == 2:
        page2 = [name.text for name in soup.find('div', class_="item_card").find_all('a', class_='name_item')]
    elif i == 3:
        page3 = [name.text for name in soup.find('div', class_="item_card").find_all('a', class_='name_item')]
    elif i == 4:
        page4 = [name.text for name in soup.find('div', class_="item_card").find_all('a', class_='name_item')]

print(page1)
print(page2)
print(page3)
print(page4)
