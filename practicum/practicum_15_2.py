"""Создать декоратор, который замеряет время работы функции.
Предусмотреть различное число итераций для сглаживания показателя.

Пример:
@param_decorator(5)
def get_request(url: str):
    return requests.get(url).text

get_request('https://google.com')

pip install requests
"""

import time
from functools import wraps

import requests
from requests.exceptions import Timeout, RequestException


def param_decorator(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            end = 0
            for i in range(1, n + 1):
                print(f"Iteration {i}/5")
                start = time.perf_counter()
                try:
                    func(*args, **kwargs)
                except Timeout as exc:
                    print(f"{exc.__class__.__name__}: {exc}")
                except RequestException as exc:
                    print(f"{exc.__class__.__name__}: {exc}")
                end += time.perf_counter() - start
            print(f"Average time for get_request: {end / n:.4f} seconds")

        return wrapper

    return decorator


@param_decorator(5)
def get_request(url: str):
    return requests.get(url, timeout=5).text


get_request('https://google.com')

# Iteration 1/5
# Iteration 2/5
# Iteration 3/5
# Iteration 4/5
# Iteration 5/5
# Average time for get_request: 0.767245 seconds
