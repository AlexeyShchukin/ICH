"""01 Напишите бесконечный генератор, который возвращает последовательность целых чисел,
где каждое следующее больше предыдущего в 2 раза.
"""
from typing import Callable, Generator


def gen_double_num():
    num = 1
    while True:
        yield num
        num *= 2


g = gen_double_num()
print(g.__next__())  # 1
print(g.__next__())  # 2
print(g.__next__())  # 4
print(g.__next__())  # 8
print(g.__next__())  # 16

""" ===========================================================


02 Напишите генератор, в который
 - передаются строки разной длины
 и который возвращает строки фиксированной длины 7 символов.

Если длина переданной строки  больше 7 символов,
    то возвращаются первые 7 символов.
Если длина переданной строки меньше 7 символов,
    то недостающие символы присоединяются к строке слева в виде нулей (“abcd” -> “000abcd”).
"""


def gen_7_symbols():
    res = ''
    while True:
        s = yield res
        res = f'{s[:7]:>07}'


# def gen_7_symbols():
#     res = ''
#     while True:
#         s = yield res
#         res = s.zfill(7)[:7]


g = gen_7_symbols()
next(g)

print(g.send('123456789'))  # 1234567
print(g.send('12345'))  # 0012345

"""  ==================================================================
03  У вас есть текстовый файл names.txt, где каждая строка - имя человека.
Написать программу, которая выводит следующее приветствие:
    “Привет, <имя 1>, <имя 2>,... <имя n> и добро пожаловать!”.
Программу реализовать с помощью генератора и суб-генератора, где
    - суб-генератор возвращает имена из файла,
    - а основной генератор в нужный момент считывает и возвращает значения из суб-генератора.
"""

with open('names.txt', 'w') as output:
    print("""Alice
John
Max
Maria""", file=output)


def gen_read_f(file: str) -> Generator[str]:
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def gen_main(func: Callable, file: str):
    yield from func(file)


print(f"{', '.join([x for x in gen_main(gen_read_f, "names.txt")])} и добро пожаловать!")
# Привет, Alice, John, Max, Maria и добро пожаловать!


""" ===============================================================


04  Возьмите json файл с предыдущего практикума, с клиентами
(имя, фамилия, дата рождения, номер счета)
и реализуйте генератор, который возвращает строки с информацией о клиентах.
Убедитесь, что после вычитывания всех строк из файла,
файловый ресурс корректно освобождается (использования исключения GeneratorExit и очистку ресурсов).
"""
import json


def gen_clients(file: str):
    try:
        with open(file, "r", encoding="utf-8") as f:
            for customer in json.load(f):
                yield customer
    except GeneratorExit:
        pass


gen = gen_clients("customers.json")
for client in gen:
    print(client)
gen.close()

# {'name': '', 'surname': 'Doe', 'birth_date': '2005-03-28', 'iban': 'DE44443333222211110000'}
# {'name': 'John', 'surname': 'Smith', 'birth_date': '2008-10-25', 'iban': 'XE345678901234567890'}
# {'name': 'Michael', 'surname': 'Brown', 'birth_date': '1990-05-15', 'iban': 'DE89370400440532013000'}
# {'name': 'Anna', 'surname': 'Johnson', 'birth_date': '1985-12-07', 'iban': '5511112222333344445555'}
# {'name': 'Emily', 'surname': 'Taylor', 'birth_date': '1999-08-03', 'iban': 'DE9876543210987654321A'}
# {'name': '', 'surname': 'Taylor', 'birth_date': '2020-08-03', 'iban': '1465DE9876543210987654321A'}
# {'name': 'Robert', 'surname': 'Davis', 'birth_date': '1992-04-12', 'iban': 'DE1234567890123456789012'}
