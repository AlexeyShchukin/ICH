"""Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы,
использует библиотеку Beautiful Soup для парсинга HTML и выводит список всех ссылок на странице."""
import requests
from bs4 import BeautifulSoup

url = "https://google.com"
# url = input("Please enter valid URL: ")
response = requests.get(url)

if response.status_code == 200:
    html_code = response.text
    soup = BeautifulSoup(html_code, "html.parser")
    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))
