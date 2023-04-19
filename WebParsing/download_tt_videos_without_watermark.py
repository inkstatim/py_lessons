from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


def get_video_description(link):
    response = requests.get(link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find('span', class_='tiktok-j2a19r-SpanText efbd9f0')
    return div.text.strip()


def get_download_video(link, video_name):
    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9,en-US;q=0.8,tg;q=0.7,sv;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'hx-current-url': 'https://ssstik.io/de',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/de',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'de',
        'tt': 'Wk5Kbms1',
    }

    response = requests.post('https://ssstik.io/abc', params=params, headers=headers, data=data)
    downloadSoap = BeautifulSoup(response.text, "html.parser")
    downloadLink = downloadSoap.a['href']
    mp4File = urlopen(downloadLink)

    with open(f"media/{video_name}.mp4", "wb") as file:
        while True:
            data = mp4File.read(4096)
            if data:
                file.write(data)
            else:
                break

nickname = input("TT nick: ")
driver = webdriver.Chrome()
driver.get(f"https://www.tiktok.com/@{nickname}")

time.sleep(20)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

print("Scrolling page")
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if screen_height * i > scroll_height:
        break

soup = BeautifulSoup(driver.page_source, "html.parser")
videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})

print(len(videos))

for video in videos:
    url = video.a["href"]
    description = get_video_description(url)
    video_name = description.replace(' ', '_')
    get_download_video(url, video_name)

