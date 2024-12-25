a = input('Введите первое логическое значение (True или False): ') == 'True'
b = input('Введите второе логическое значение (True или False): ') == 'True'
c = input('Введите третье логическое значение (True или False): ') == 'True'
d = input('Введите четвёртое логическое значение (True или False): ') == 'True'
formula_1 = not ((a or b) and (c or d))
formula_2 = (not a and not b) or (not c and not d)
print('Формулы эквивалентны' if formula_1 == formula_2 else 'Формулы не эквивалентны')
