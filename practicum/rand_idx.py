"""2. В функцию передаются длинная строка и длинный список.
Надо вставить элементы из списка в строку следующим образом:
 - для каждого элемента случайно определить позицию для вставки
 - и вставить этот элемент по индексу.

Решите задачу методами для строк и методами для списков.
"""

from random import randrange

text_ex = "В функцию передаются длинная строка и длинный список"
list_ex = ['1', '2', '3', '4', '5']


def fixed_text(text: str, arr: list):
    for e in arr:
        length = len(text)
        rand_idx = randrange(length)
        text = text[:rand_idx] + e + text[rand_idx:]
        length += 1
    return text


print(fixed_text(text_ex, list_ex))
