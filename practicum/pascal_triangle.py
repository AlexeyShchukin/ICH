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
    res = f(n) // (f(k) * f(abs(n - k)))
    return res


with open('num.txt', 'r') as file:
    with open('pascal_triangle.txt', 'w') as pt:
        num = int(file.read().strip())
        for i in range(num):
            print(end='' if i == 0 else '\n', file=pt) # удаление первого переноса строки
            print(' ' * (num - i - 1), end='', file=pt)  # выравнивание треугольника
            print(' ' * (num - i - 1), end='', file=pt)
            for j in range(i + 1):
                print(f'{bk(i, j):<3d}', end=' ', file=pt)
