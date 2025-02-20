"""2.1. Напишите функцию, которая возвращает True, если текст содержит правильную скобочную последовательность.
И False - если нет.
Вариант для одного вида скобок ().
"""


def is_valid_parentheses(sequence: str) -> bool:
    stack = []
    for char in sequence:
        if char == '(':
            stack.append('(')  # добавляем в стек встречающиеся открытые скобки
        elif char == ')':
            if not stack:  # если стек пустой, то False, так как у нас закрытая скобка идёт раньше открытой
                return False
            stack.pop()  # если стек не пустой, вытаскиваем последний элемент, то есть одну открытую скобку
    return not stack  # если после цикла открытых скобок не осталось в стеке, значит они все закрылись


# Примеры использования
print(is_valid_parentheses("()") == True)  # True
print(is_valid_parentheses("(())") == True)  # True
print(is_valid_parentheses("(()") == False)  # True
print(is_valid_parentheses(")(") == False)  # True
print(is_valid_parentheses("())(") == False)  # True
