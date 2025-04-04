"""Напишите генератор, который будет принимать на вход числа и возвращать их сумму.
Генератор должен использовать инструкцию yield для возврата текущей суммы и
должен продолжать принимать новые числа для добавления к сумме.
Если генератор получает на вход число 0, он должен прекращать работу и вернуть окончательную сумму.
Напишите программу, которая будет использовать этот генератор для пошагового расчета суммы чисел, вводимых пользователем.
Пример вывода:

Введите числа для суммирования (0 для окончания):

Введите число: 3
Текущая сумма: 3
Введите число: 5
Текущая сумма: 8
Введите число: 2
Текущая сумма: 10
Введите число: 0
Текущая сумма: 10"""


def sum_nums():
    total = 0
    while True:
        num = yield total  # save send-value in num and return total
        if num == 0:
            break
        total += num
    return total


print('Enter numbers to sum (0 to finish):')
n = ''
gen = sum_nums()
next(gen)
while n != 0:
    n = int(input('Enter a number: '))
    try:
        print(f'Current sum: {gen.send(n)}')
    except StopIteration as exc:
        print(f'Current sum: {exc.value}')
