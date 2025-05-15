"""https://tortocake.com/

Скачайте 5 изображений тортов с указанного сайта.
(Для справки: в имени файла изображения должно быть "tort-")
"""



import requests
from bs4 import BeautifulSoup

URL = 'https://tortocake.com/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

imgs = soup.find_all('img')

urls = []
for img in imgs:
    src = str(img.get('src'))
    if 'tort-' in src:
        urls.append(src)

res = [URL+url for url in urls]

for i in range(1, len(res) + 1):
    with open(f"img{i}.jpg", "wb") as f:
        f.write(requests.get(res[i-1]).content)

