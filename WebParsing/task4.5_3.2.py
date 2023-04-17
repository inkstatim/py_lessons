"""
1. Открываем сайт
2. Проходимся по всем страницам в категории мыши (всего 4 страницы)
3. На каждой странице посещаем каждую карточку с товаром (всего 32 товаров)
4. В каждой карточке извлекаем при помощи bs4 артикул <class="article"> Артикул: 80244813 </p>
5. Складываем(плюсуем) все собранные значения
6. Вставляем получившийся результат в поле ответа
"""
from bs4 import BeautifulSoup
import requests

total = 0
ap = []
for i in range(1, 5):
    url = f"https://parsinger.ru/html/index3_page_{i}.html"
    r = requests.get(url=url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.content, 'html.parser')

    product_cards = soup.find_all('div', class_='item')
    shema = "https://parsinger.ru/html/"
    for card in product_cards:

        product_url = shema + card.find('a', class_='name_item')['href']

        r = requests.get(url=product_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        article = soup.find('p', class_='article')
        if article:
            article_number = int(article.text.split()[-1])
            total += article_number
            ap.append(article_number)

print(total)
print(len(ap))
