"""02. Напишите генератор, который будет генерировать арифметическую прогрессию

В качестве аргументов генераторной функции передаётся
- начальное значение прогрессии,
- шаг (по умолчанию = 1),
- и последний элемент прогрессии (по умолчанию бесконечная прогрессия)"""
from math import inf


def ar_prog(a, d=1, n=inf):
    total = a
    while n:
        yield total
        total += d
        if n:
            n -= 1


first_number = 10
gen = ar_prog(first_number)
for num in gen:
    print(num)
