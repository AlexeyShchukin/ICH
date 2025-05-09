"https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup"

"""Используя библиотеку BeautifulSoup 4 , найдите и выведите все ссылки
 (список значений атрибута href всех тегов ссылок <a> из меню навигации
 (<nav> элемент)  в предоставленном HTML-файле <navbar_links.html>

 Ссылки могут быть как в основном меню, так и в выпадающем подменю.

ВАЖНО: Обратите внимание, что в выборку ссылок НЕ должны попадать:
    1. Ссылки, которые находятся вне меню навигации.
        Wrong link1 - Wrong link5
    2. Ссылки, ВНУТРИ меню навигации, которые не содержат атрибут href
        Wrong link0
"""
from bs4 import BeautifulSoup


def get_html(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


html_content = get_html('example_navbar_links.html')
soup = BeautifulSoup(html_content, 'html.parser')
nav_tag = soup.nav
links = nav_tag.find_all("a")

for link in links:
    if link.get("href"):
        print(f"{link.text.strip()}: {link.get("href")}")



# Navbar (navigation menu):   https://my-site.com
# Features:   https://features.com
# Dropdown link:   https://dropdown.com
# Action:   https://dropdown.com/action
# Another action:   https://dropdown.com/another_action
# Something else here:   https://dropdown.com/something_else