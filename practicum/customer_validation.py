"""Написать функцию validate_customers(customer), которая принимает на входе список кортежей:
    Имя
    Фамилия
    Дата рождения
    Номер банковского счёта (IBAN)

Функция возвращает словарь, где
    - ключом является строка имя+фамилия,
    - а значением - список сообщений об ошибках, возникших при валидации пользователя по следующим правилам:
        - Имя и фамилия не должны быть пустыми.
        - Возраст валиден, если он больше 18 лет.
        - Ошибки валидации IBAN (см. примечание в конце условий)

IBAN должен соответствовать стандарту длины (начинаться с кода страны и содержать правильное количество символов)
https://en.wikipedia.org/wiki/International_Bank_Account_Number

Решение должно использовать исключения и итераторы.

PS
Параметры IBAN в значительной степени зависят от страны-нахождения банка.
Поэтому для простоты считаем, что все счета - только из Германии.
Например, IBAN: DE89370400440532013000
Проверяем:
 - длина (после удаления внутренних пробелов) - 22 символа
 - первые 2 символа - буквы
 - остальные 20 символов - цифры
"""
from collections import defaultdict
from datetime import datetime
from pprint import pprint
from json import load

try:
    with open('customers.json', 'r', encoding='utf-8') as file:
        customers = load(file)
        users = []
        for customer in customers:
            users.append(tuple(customer.values()))
except FileNotFoundError as e:
    print(f'{e.__class__.__name__}: {e}')


class NameException(Exception):
    pass


class AgeException(Exception):
    pass


class IBANException(Exception):
    pass


def name_validation(name, surname) -> bool:
    """Функция проверяет наличие имени и фамилии

    :param name, surname
    :return: True, если имя и фамилия не пустая строка или None
    :raises NameException: Empty name or/and surname
    """
    if not name or not surname:
        raise NameException("Empty name or/and surname")
    return True


def age_validation(birth_date: str) -> bool:
    """Проверяет, исполнилось ли человеку 18 лет на текущую дату.

    :param birth_date: Дата рождения в формате 'YYYY-MM-DD'.
    :return: True, если возраст 18 лет и более.
    :raises AgeException:  The client's age cannot be less than 18 years!
    """
    if datetime.now().year - int(birth_date.split('-')[0]) < 18:
        raise AgeException("The client's age cannot be less than 18 years!")
    return True


def iban_validation(iban: str) -> bool:
    """Проверяет корректность IBAN.

    :param iban: IBAN (DE).
    :return: True, счёт удовлетворяет всем критериям IBAN.
    :raises IBANException: в комментарии может быть набор из ошибок:
        Incorrect Length of IBAN!
        The first two characters must be letters!
        The last twenty characters must be digits!
    """
    message = []
    if not iban.startswith('DE'):
        message.append('The first two characters must be letters DE!')
    if len(iban) != 22:
        message.append('Incorrect Length of IBAN!')
    if not iban[2:].isdigit:
        message.append('The last twenty characters must be digits!')
    if message:
        raise IBANException(f'{'; '.join(message)}')


def validate_customers(list_tuples: list[tuple[str, ...]]) -> dict[str, list[str]]:
    """Функция формирует словарь из всех возможных ошибок по каждому клиентов"""
    d = defaultdict(list)
    for client in list_tuples:
        name, surname, date, iban = client
        try:
            name_validation(name, surname)
        except NameException as e:
            d[f"{name}_{surname}"].append(f"{e.__class__.__name__}: {e}")

        try:
            age_validation(date)
        except AgeException as e:
            d[f"{name}_{surname}"].append(f"{e.__class__.__name__}: {e}")

        try:
            iban_validation(iban)
        except IBANException as e:
            d[f"{name}_{surname}"].append(f"{e.__class__.__name__}: {e}")

    return dict(d)


def main():
    pprint(validate_customers(users))


if __name__ == '__main__':
    main()
