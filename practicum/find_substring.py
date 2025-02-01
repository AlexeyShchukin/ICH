"""Напишите программу, которая запрашивает у пользователя строку и подстроку,
а затем находит все вхождения подстроки в строке и выводит их позиции.
Используйте метод find() для поиска подстроки.
Если подстрока не найдена, выведите соответствующее сообщение на экран.
ПРИМЕЧАНИЕ: поиск должен быть регистронезависимым.

Пример вывода:
Введите строку: Hello, how are you? How's the weather today?
Введите подстроку: How
Подстрока найдена на позициях: 7, 20"""

string = 'Hello, how are you? How\'s the weather today?'
substring = 'how'

res = ''

idx = 0
if substring in string:
    idx = string.lower().find(substring.lower())
    res = '' + str(idx)

idx += len(substring)
while idx < len(string):
    idx = string.lower().find(substring.lower(), idx)
    if idx == -1:
        break
    else:
        res += f', {idx}'
        idx += len(substring)

print(f'Подстрока найдена на позициях: {res}')
