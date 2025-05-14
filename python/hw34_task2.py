"""Напишите функцию highlight_keywords(text, keywords),
которая выделяет все вхождения заданных ключевых слов в тексте, окружая их символами *.
Функция должна быть регистронезависимой при поиске ключевых слов."""
import re


def highlight_keywords(text, keywords):
    return re.sub(
        pattern=rf"({'|'.join(keywords)})",
        repl=r"*\1*",
        string=text,
        flags=re.I
    )


t = "This is a sample text. We need to highlight Python and programming."

kws = ["python", "programming"]

highlighted_text = highlight_keywords(t, kws)

print(highlighted_text)

# Вывод: "This is a sample text. We need to highlight *Python* and *programming*."
