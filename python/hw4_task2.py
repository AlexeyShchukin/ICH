a = input('Введите первое логическое значение (True или False): ') == 'True' # преобразование строки в булево значение
b = input('Введите второе логическое значение (True или False): ') == 'True'
print(f'''Результат логического И: {a and b}
Результат логического ИЛИ: {a or b}
Результат логического НЕ {not a or b}
Результат логического НЕ (для второго значения): {a or not b}
Результат сравнения на равенство: {a == b}
Результат сравнения на неравенство: {a != b}''')