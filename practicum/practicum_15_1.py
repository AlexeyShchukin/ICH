"""Создать декоратор, который замеряет время работы функции.
Предусмотреть различное число итераций для сглаживания показателя.

Пример:
@param_decorator(5)
def get_request(url: str):
    return requests.get(url).text

get_request('https://google.com')

pip install requests
"""

from functools import wraps
from random import randint
from time import perf_counter, sleep


def param_decorator(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            end = 0
            for i in range(1, n + 1):
                print(f"Iteration {i}/5")
                start = perf_counter()
                func(*args, **kwargs)
                end += perf_counter() - start
            print(f"Average time for get_request: {end / n:.4f} seconds")

        return wrapper

    return decorator


@param_decorator(5)
def get_request():
    x = randint(0, 2)
    sleep(x)
    print(f"   Delay is {x} seconds")


get_request()

# Iteration 1/5
#    Delay is 2 seconds
# Iteration 2/5
#    Delay is 2 seconds
# Iteration 3/5
#    Delay is 0 seconds
# Iteration 4/5
#    Delay is 2 seconds
# Iteration 5/5
#    Delay is 0 seconds
# Average time for get_request: 1.200120 seconds
