"""Напишите программу, которая
 - открывает текстовый файл с именем input.txt,
 - построчно считывает его содержимое и
 - записывает в файл с именем output.txt, меняя порядок слов на обратный.
Каждое слово должно быть записано на отдельной строке.
Используйте цикл for и методы readlines(), split() и reverse() для решения задачи.

Пример содержимого файла input.txt:
Hello, World! How are you?

Пример содержимого файла output.txt:
you?
are
How
World!
Hello,
"""

with open('input.txt', 'r', encoding='utf-8') as f:
    with open('output.txt', 'a', encoding='utf-8') as out:
        for line in f.readlines():
            words = line.split()
            words.reverse()
            for word in words:
                print(word, file=out)
