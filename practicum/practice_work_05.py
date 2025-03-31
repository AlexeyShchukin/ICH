"""Считать текст из файла anna-karenina.txt,
обработать его, и в итоге вернуть итератор,
состоящий из слов длиной более десяти символов.
"""
from typing import Iterator


def read_file(path: str) -> str:
    """
    Читает содержимое файла и возвращает его в виде строки.

    :param path: Путь к файлу.
    :return: Текст из файла.
    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def clean_word(word: str) -> str:
    """
    Очищает слово от небуквенных символов.

    :param word: Исходное слово.
    :return: Очищенное слово, содержащее только буквы.
    """
    return "".join(alpha for alpha in word if alpha.isalpha())


def clean_and_split(text: str) -> Iterator[str]:
    """
    Приводит текст к нижнему регистру, разбивает на слова и очищает их.

    :param text: Исходный текст.
    :return: Итератор очищенных слов.
    """
    text = text.replace("-", " ")
    res = map(lambda x: x.strip(), text.lower().split())
    return res


def process_text(path: str) -> Iterator[str]:
    """
    Обрабатывает текст из файла:
    - Читает файл.
    - Разбивает текст на слова и очищает их.
    - Фильтрует слова длиной более 10 символов.

    :param path: Путь к файлу.
    :return: Итератор отфильтрованных слов.
    """
    text = read_file(path)
    clean_words = clean_and_split(text)
    return (clean_word(word) for word in clean_words if len(clean_word(word)) > 10)


file_path = 'anna-karenina.txt'
long_words = process_text(file_path)
print(*long_words, sep='\n')

# несчастливая
# несчастлива
# француженкою
# гувернанткой
# продолжалось
# ...
