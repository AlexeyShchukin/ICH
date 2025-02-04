"""1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и
выводит на экран наиболее часто встречающиеся слова. Для решения задачи используйте класс Counter
из модуля collections. Создайте функцию count_words, которая принимает текст в качестве аргумента и
возвращает словарь с количеством вхождений каждого слова. Выведите наиболее часто встречающиеся слова
и их количество.
Пример вывода: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
Вывод:
Sed: 2
Lorem: 1"""

from collections import Counter


def count_words(s: str) -> dict:
    mod_s = s.translate(str.maketrans('', '', ",:;!?'."))  # delete spec-symbols
    mod_s_list = mod_s.split() # list of original words
    mod_s_lower_list = mod_s.lower().split() # list of lowercase words
    sorted_lower_s = Counter(mod_s_lower_list).most_common()  # list of sorted tuples like (key, value)
    res = {}
    for k, v in sorted_lower_s: # iterate over sorted tuples
        original_word = mod_s_list[mod_s_lower_list.index(k)]
        res[original_word] = v
        if v == 1:
            break
    return res


if __name__ == '__main__':
    for key, value in count_words(input('Enter a text: ')).items():
        print(f'{key}: {value}')

# Без учёта регистра всё проще:
# from collections import Counter
#
#
# def count_words(s: str) -> dict:
#     mod_s = s.translate(str.maketrans('', '', ",:;!?'.")).lower() # delete spec-symbols, make lowercase
#     res = {}
#     for k, v in Counter(mod_s.split()).most_common(): # sorted tuples like (key, value)
#         res[k] = v
#         if v == 1:
#             break
#     return res
#
#
# if __name__ == '__main__':
#     for k, v in count_words(input('Enter a text: ')).items():
#         print(f'{k}: {v}')
