"""Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы
и уровень заголовков, а затем использует библиотеку Beautiful Soup для парсинга HTML
и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом."""

import requests
from bs4 import BeautifulSoup

# url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D0%BE%D0%B2_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F_HTTP"

data = input("Please enter valid URL and title level(1-6) separated by space: ")
url, level = data.split()

response = requests.get(url)

if response.status_code == 200:
    html_code = response.text
    soup = BeautifulSoup(html_code, "html.parser")
    titles = soup.find_all("h" + level)

    # titles = soup.find_all("h2")

    for title in titles:
        print(title)
