"""Во входном файле задаётся число.
Необходимо в выходной файл вывести треугольник Паскаля,
который будет занимать верхний левый угол.
Воспользуйтесь расчётом биномиального коэффициента в цикле.
ВАЖНО: Деление одного факториала на произведение двух других ВСЕГДА
даёт целочисленный результат!
"""
from math import factorial as f


def bk(n, k):
    """Расчёт биномиального коэффициента"""
    return f(n) // (f(k) * f(n - k))


def pascal_triangle(num):
    with open('pascal_triangle.txt', 'w', encoding='utf-8') as pt:
        longest = len(str(bk(num - 1, num // 2))) + 2  # длина самого большого числа в треугольнике
        for i in range(num):
            line = ''
            for j in range(i + 1):
                line += f'{bk(i, j):^{longest}d}'  # центрируем числа по длине наибольшего числа и собираем в строку
            print(line.center(longest * num), file=pt)  # центрируем строку по длине наибольшей строки


with open('practicum/num.txt', 'r') as file:
    number = int(file.read().strip())  # считываем число из файла

pascal_triangle(number)
