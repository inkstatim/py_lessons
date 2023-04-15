import requests
import time
url = '........'
responce = requests.get(url=url, stream=True)

with open('file2.mp4', 'wb') as vid:
    for peic in responce.iter_content(chunk_size=100000):
        vid.write(peic)
