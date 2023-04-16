from bs4 import BeautifulSoup
import requests
import lxml
url = "https://www.tiktok.com/@missbeckyjo/video/6871250024089586945?is_copy_url=1&is_from_webapp=v1" #Здесь пишем ссылку на видео
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

div = soup.find('span', class_='tiktok-j2a19r-SpanText efbd9f0') # В класс пишем в каком классе находится описание

print(div.text)