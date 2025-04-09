from functools import wraps
from random import randint
from typing import Callable


def decorator(exceptions: list[tuple[Exception, Callable[[], None]]]):
    def wrapper(func):
        @wraps(func)
        def wrapper1(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                for ex, handler in exceptions:
                    if isinstance(e, ex):
                        handler()
                        raise e
            return res
        return wrapper1
    return wrapper



def bar():
    print(1)


@decorator([(KeyError, bar), (IndexError, lambda: print(2))])
def foo():
    if randint(1,2 ) == 1:
        raise KeyError("bar")
    else:
        raise IndexError


foo()