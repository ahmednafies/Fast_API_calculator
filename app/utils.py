import time
import functools
from app.exceptions import ValidationError


def eval_time(func):
    def timed(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        total_time = f"{(end - start) * 1000} ms"
        return result, total_time

    return timed


def is_valid_number(num, max_val):
    if not isinstance(num, int):
        raise TypeError("Only Integer Values are allowed")
    if num < 0:
        raise ValidationError("Negative numbers are not allowed")
    if num > max_val:
        raise ValidationError("Input exceed maximum allowed limit")


def validate(max_val=100):
    def decorator_validate(func):
        @functools.wraps(func)
        def wrapper_validate(*args, **kwargs):
            num = args[0]
            is_valid_number(num, max_val)
            return func(*args, **kwargs)

        return wrapper_validate

    return decorator_validate
