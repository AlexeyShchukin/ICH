"""1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и
выводит на экран наиболее часто встречающиеся слова. Для решения задачи используйте класс Counter
из модуля collections. Создайте функцию count_words, которая принимает текст в качестве аргумента и
возвращает словарь с количеством вхождений каждого слова. Выведите наиболее часто встречающиеся слова
и их количество.
Пример вывода: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
Вывод:
sed: 2
lorem: 1"""

from collections import Counter, OrderedDict

original_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.'


def count_words(text: str) -> dict:
    clean_text = ''
    for char in text:
        if char.isalpha() or char in (' ', '/n'):
            clean_text += char
    return {k: v for k, v in sorted(OrderedDict(Counter(clean_text.lower().split())).items(), key=lambda x: -x[1])}


temp = set()
for key, value in count_words(original_text).items():
    if value not in temp:
        print(f'{key}: {value}')
        temp.add(value)


def count_words2(text: str) -> dict:
    clean_text = ''
    for char in text:
        if char.isalpha() or char in (' ', '/n'):
            clean_text += char
    res = {}
    for k, v in Counter(clean_text.lower().split()).most_common():  # tuples sorted in decreasing order
        res[k] = v
        if v == 1:
            break
    return res


for key, value in count_words2(original_text).items():
    print(f'{key}: {value}')
