import requests as requests
from bs4 import BeautifulSoup

# Получаем HTML-код страницы
response = requests.get('https://de.wiktionary.org/wiki/habt ')
html = response.text

# Используем BeautifulSoup для парсинга HTML-кода
soup = BeautifulSoup(html, 'html.parser')

# Находим нужный элемент на странице
element = soup.find('div', {'class': 'some-class'})

# Проверяем, что элемент найден
if element is not None:
    # Получаем текстовое содержимое элемента
    data = element.text
    # Сохраняем данные в файл
    with open('data.txt', 'w') as file:
        file.write(data)
else:
    print('Элемент не найден на странице')