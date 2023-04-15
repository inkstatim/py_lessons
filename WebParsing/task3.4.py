"""
1. Откройте сайт "https://parsinger.ru/task/1"
2. На нём есть 500 ссылок и только 1 вернёт статус код 200
3. Напишите код который поможет найти правильную ссылку
4. По этой ссылке лежит секретный код, который необходимо вставить в поле ответа.
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://parsinger.ru/task/1"
response = requests.get(url=base_url)
soup = BeautifulSoup(response.text, "html.parser")

successful_links = []
for i, link in enumerate(soup.find_all('a'), start=1):
    print(i)

    href = link.get('href')
    full_url = urljoin(base_url, href)
    response = requests.get(full_url)
    if response.status_code == 200:
        successful_links.append(link)
        break
    else:
        print(response.status_code)

print(successful_links)



# здесь вы можете использовать секретный код в соответствии с требованиями вашей задачи
