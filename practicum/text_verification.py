"""Написать функцию count_vowels, которая возвращает количество гласных в тексте,
где гласные vowels = 'aeiouy'.

Пример:
text = 'hEllO world'
result = 3
"""


def count_vowels(t: str) -> int:
    vowels = 'aeiouy'
    cnt = 0
    for char in t:
        if char.lower() in vowels:
            cnt += 1
    return cnt


if __name__ == '__main__':
    text = 'hEllO world'
    print(count_vowels(text))
