import time
import functools
from app.validators import is_valid_number


def eval_time(func):
    def timed(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        total_time = f"{(end - start) * 1000} ms"
        return result, total_time

    return timed


def validate(min_val=0, max_val=100):
    def decorator_validate(func):
        @functools.wraps(func)
        def wrapper_validate(*args, **kwargs):
            num = args[0]
            is_valid_number(num, min_val, max_val)
            return func(*args, **kwargs)

        return wrapper_validate

    return decorator_validate
