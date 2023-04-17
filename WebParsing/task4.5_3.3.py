"""
1. Открываем сайт
2. Проходимся по всем категориям, страницам и карточкам с товарами(всего 160шт)
3. Собираем с каждой карточки стоимость товара умножая на количество товара в наличии
4. Складываем получившийся результат
5. Получившуюся цифру с общей стоимостью всех товаров вставляем в поле ответа.
"""
from bs4 import BeautifulSoup
import requests

total = 0
ap = []
for i in range(1, 6):
    for j in range(1, 5):
        url = f"https://parsinger.ru/html/index{i}_page_{j}.html"
        r = requests.get(url=url)

        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.content, 'html.parser')

        product_cards = soup.find_all('div', class_='item')
        shema = "https://parsinger.ru/html/"
        for card in product_cards:

            product_url = shema + card.find('a', class_='name_item')['href']
            r = requests.get(url=product_url)
            soup = BeautifulSoup(r.content, 'html.parser')
            in_stock = soup.find('span', id='in_stock')
            price = soup.find('span', id='price')
            if in_stock:
                in_stock_num = int(in_stock.text.split()[-1])
                price_num = int(price.text.split()[0])
                total += price_num*in_stock_num
                ap.append(price)

print(total)
print(len(ap))
