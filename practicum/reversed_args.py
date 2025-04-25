"""Напишите декоратор, который делает так,
что задекорированная функция принимает все свои порядковые аргументы
 в порядке, обратном тому, в котором их передали.
(для именованных аргументов (kwargs) порядок не важен,
поэтому мы их здесь не учитываем).
"""
from functools import wraps


def reverse_args_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*reversed(args), **kwargs)

    return wrapper


@reverse_args_decorator
def print_args(a, b, c):
    print(f'a: {a}, b: {b}, c: {c}')


print_args(1, 2, 3)
# a: 3, b: 2, c: 1
