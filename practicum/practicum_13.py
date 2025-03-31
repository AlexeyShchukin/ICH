"""01 Дана последовательность слов. Написать функцию,
которая возвращает итератор последовательности слов,
длина которых больше трёх символов
Использовать lambda-функции и filter.
При описании функции использовать аннотации.
"""
from typing import Iterator


def filter_long_words(word_list: list[str]) -> Iterator[str]:
    return filter(lambda x: len(x) > 3, word_list)


# Пример использования функции
words = ["cat", "elephant", "dog", "tiger", "ant", "monkey", "bee", "fox"]
filtered_words = filter_long_words(words)
print(*filtered_words)

# elephant tiger monkey



"""02 ==============================================================
Дан генератор, содержащий последовательность слов words.
Вернуть предложение, составленное из слов данной последовательности.
Слова в полученном предложении разделены пробелами.
При описании генератора использовать аннотации.

"""
from typing import Generator


# Generator[YieldType, SendType, ReturnType]
def gen(lst: list[str]) -> Generator[str, None, None]:
    yield from lst


words = ["This", "is", "a", "simple", "sentence"]
words_iter = ' '.join(gen(words))
print(words_iter)

# This is a simple sentence



"""03 ===========================================
Дана последовательность слов.
Написать функцию, которая возвращает итератор.
В этом итераторе слова из 3-х символов
необходимо перевести в верхний регистр.
При решении использовать функциональны подход.
При описании функции использовать аннотации.

Пример:
[“The”, “quick”, “brown”, “fox”] -> [“THE”, “quick”, “brown”, “FOX”]
"""
from typing import Iterator


def upper_for_3_letters(words: list) -> Iterator[str]:
    return map(lambda x: x.upper() if len(x) == 3 else x, words)


words = ["The", "quick", "brown", "fox"]
new_words = upper_for_3_letters(words)
print(*new_words)

# THE quick brown FOX


"""04 =========================================================
Изменить решение задачи 1 так,
чтобы последовательность слов вычитывалась из текстового файла,
где каждое слово было в новой строке.

Для этого сначала необходимо получить файл:
создать функцию write_file('words.json', words)
Затем - функцию для чтения файла, read_file(),
которая возвращает итератор.
Соответственно, адаптированная функция
"""
import json
from typing import Iterator


def write_file(filename: str, words: list[str]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(words, f)


def read_file(filename: str) -> Iterator[str]:
    with open(filename, "r", encoding="utf-8") as file:
        return iter(json.load(file))


def filter_long_words(words: Iterator[str]) -> Iterator[str]:
    return filter(lambda x: len(x) > 3, words)


words = ["cat", "elephant", "dog", "tiger", "ant", "monkey", "bee", "fox"]
write_file('words.json', words)

words_iter = read_file('words.json')
filtered_words = filter_long_words(words_iter)
print(*filtered_words)

# elephant tiger monkey