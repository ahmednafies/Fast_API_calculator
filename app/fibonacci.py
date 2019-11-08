from functools import lru_cache
from app.exceptions import ValidationError
from app.utils import eval_time

results = {0: 0, 1: 1}
last_num = 1


def compute_next(start, end) -> int:
    global last_num
    count = start
    while count < end:
        results.append(results[-2] + results[-1])
        count += 1


@eval_time
@lru_cache(1000)
def fibonacci(n) -> int:
    global last_num

    if n < 0:
        raise ValidationError("Negative numbers are not allowed")

    if n == 0 or n == 1:
        return n

    if len(results) == 2:
        n = n - 1  # because we already have values in the results
        compute_next(0, n)
        return results[-1]

    if n < len(results):
        return results[n]

    if n > len(results):
        compute_next(len(results), n + 1)
        return results[-1]

    return results[-1]
