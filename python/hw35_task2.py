"""2. Напишите функцию find_common_words(url_list), которая принимает список
URL-адресов и возвращает список наиболее часто встречающихся слов на веб-страницах.
Для каждого URL-адреса функция должна получить содержимое страницы с помощью запроса GET
и использовать регулярные выражения для извлечения слов. Затем функция должна подсчитать
количество вхождений каждого слова и вернуть наиболее часто встречающиеся слова в порядке убывания частоты."""
from re import findall
from collections import Counter

from requests import get


def find_common_words(url_list: list):
    html_code = "\n".join([get(url).text for url in url_list])
    pattern = r">([a-zA-Z]+)<"
    words = findall(pattern, html_code)
    return " ".join([e[0] for e in Counter(words).most_common()])


print(find_common_words(["https://google.com"]))
