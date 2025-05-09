"""Написать программу, которая скачивает страницу с сайта на выбор
с актуальным курсом валют, выделяет курс доллара к евро и выводит его.
Можно пользоваться регулярными выражениями и Beautiful Soup вместе.

Уточнение: используйте html-код файла <example_table.html>
"""

from bs4 import BeautifulSoup


def get_html(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


html_content = get_html('example_table.html')
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.table

tr_tag = table.find_all("tr")
for tr in tr_tag:
    td_tags = tr.find_all("td")
    if td_tags:
        if td_tags[1].text == "USD":
            usd = float(td_tags[0].text)
        elif td_tags[1].text == "EUR":
            eur = float(td_tags[0].text)

print(f'Курс USD / EUR = {usd / eur}')
# AUD Австралийский доллар 58,0043?
# AZN Азербайджанский манат 51,7600
# AMD Армянских драмов 22,6655
# BYN Белорусский рубль 28,1601
# BGN Болгарский лев 49,1738

# Курс USD / EUR = 0.9244371976920589
