from functools import wraps


def retry_on_exception(retries: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            for r in range(retries):
                try:
                    res = func(*args, **kwargs)
                    print("ok")
                    return res
                except Exception as e:
                    if r == retries - 1:
                        print(f"final {e.__class__.__name__}")
                    else:
                        print(e.__class__.__name__)

        return wrapper

    return decorator
