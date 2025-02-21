"""2.2. Напишите функцию, которая возвращает True, если текст содержит правильную скобочную последовательность.
И False - если нет.
Вариант для трёх видов скобок (){}[].
"""


def is_valid_brackets(sequence: str) -> bool:
    stack = []
    for char in sequence:
        if char in '([{':
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                last = stack.pop()
                if char == ')' and last != '(':
                    return False
                elif char == ']' and last != '[':
                    return False
                elif char == '}' and last != '{':
                    return False
    return not stack


print(is_valid_brackets("()") == True)  # True
print(is_valid_brackets("([])") == True)  # True
print(is_valid_brackets("{[()]}") == True)  # True
print(is_valid_brackets("{[(])}") == False)  # True
print(is_valid_brackets("{[}") == False)  # True
print(is_valid_brackets("[({})]") == True)  # True
print(is_valid_brackets("[({})](]") == False)  # True
