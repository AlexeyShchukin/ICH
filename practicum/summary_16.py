"""Создайте класс Char, который будет представлять
заглавную латинскую букву от A до Z

    Атрибуты:
        char: заглавная буква от A до Z
        code: код символа char в десятичной кодировке

При создании класса в качестве аргумента возможно строка из нескольких символов
В этом случае остаётся только первый символ, который необходимо перевести
в верхний регистр.
Если он окажется не буковой от A до Z - выбрасывается исключение:
    ValueError(f"Invalid character: {char}")

При выводе на печать объекта - выводится символ.
Допустимо сложение:
  - сложение двух объектов Char
  - или Char + целое число.
(см примеры ниже)
Реализовать вычисление суммы кода символа с целым числом
в виде отдельного защищённого (protected) метода.
"""
from typing import Union


class Char:
    def __init__(self, char: str):
        if char.isalpha():
            self.char = char[0].upper()
        else:
            raise ValueError(f"Invalid character: {char}")
        self.code = ord(self.char)

    def __str__(self):
        return self.char

    def __add__(self, other: Union['Char', int]) -> 'Char':
        if isinstance(other, Char):
            shift = other.code - 65
        elif isinstance(other, int):
            shift = other
        else:
            raise ValueError("Operand must be either Char or int")
        res = (self.code - 65 + shift) % 26 + 65
        return Char(chr(res))

    def __repr__(self) -> str:
        return f"Char('{self.char}')"


c1 = Char('A')
print(c1 + c1)  # A

c2 = Char('B')
print(c1 + c2)  # B

c3 = Char('z')
print(c3)  # Z
print(c3 + 1)  # A

c4 = Char('Y')
print(c4 + 3)  # B
print(c4 + -3)  # V
print(c4 + 1000)  # K

c5 = Char('abba')
print(c5)  # A
try:
    c6 = Char('1')  # Должен выбросить ValueError
except ValueError as e:
    print(e)  # Invalid character: 1
