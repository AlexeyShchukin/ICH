n = int(input('Введите целое положительное число: '))
x = 2
flag = True
while x < n:
    if n % x == 0:
        flag = False
    x += 1
print(f'Число {n} является простым.' if flag else f'Число {n} не является простым.')
