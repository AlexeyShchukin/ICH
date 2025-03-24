"""Создайте бесконечный генератор square_generator(), который принимает целое число и возвращает его квадрат.
А если ничего не передано, генератор возвращает 1.
Если число отрицательное, то оно возводится в третью степень
"""


def square_generator():
    res = 0
    while True:
        num = yield res
        if num is None:
            res = 1
        elif num < 0:
            res = num ** 3
        else:
            res = num ** 2


gen = square_generator()
# Инициализация генератора
next(gen)

print(gen.send(3))  # 9
print(gen.send(4))  # 16
print(next(gen))  # 1
print(gen.send(5))  # 25
print(gen.send(-4))  # -64
