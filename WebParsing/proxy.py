import requests
from bs4 import BeautifulSoup
url = "https://free-proxy-list.net/"

res = requests.get(url)
soup = BeautifulSoup(res.content, 'lxml')

table = (soup.find('tbody'))

proxy_list = open('proxy.txt', 'w')

for (rows) in table.find_all('tr'):
    details = list(rows)
    ip_address = details[0].text
    port = details[1].text
    country_code = details[2].text
    country_name = details[3].text
    anonymity = details[4].text
    google = details[5].text
    http = details[6].text
    last_checked = details[7].text
    print(ip_address, port, sep=":")
    proxy_list.write(str(ip_address)+":"+str(port)+'\n')

proxy_list.close()