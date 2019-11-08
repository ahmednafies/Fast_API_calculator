from functools import lru_cache
from app.exceptions import ValidationError
from app.utils import eval_time

results = {0: 0, 1: 1}
last_num = 1


def compute_next(num) -> int:
    global last_num
    while last_num < num:
        results[last_num + 1] = results[last_num - 1] + results[last_num]
        last_num += 1


@eval_time
@lru_cache(100)
def fibonacci(n) -> int:
    global last_num

    if n < 0:
        raise ValidationError("Negative numbers are not allowed")

    if n < last_num:
        return results[n]

    if n > last_num:
        compute_next(n)

    return results[last_num]
