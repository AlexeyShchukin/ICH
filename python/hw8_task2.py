n = input('Введите целое число: ')
power = len(n)
original = n = int(n)           # сохраняем исходное значение
res = 0
while n:                        # пока n > 0
    res += (n % 10) ** power    # последнюю цифру числа возводим в степень и добавляем к результату
    n = n // 10                 # обрезаем исходное число на одну цифру с конца
print('Число является числом Армстронга.' if res == original else 'Число не является числом Армстронга.')
