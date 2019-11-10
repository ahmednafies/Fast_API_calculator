from functools import lru_cache
from app.utils import eval_time, validate
import config

results = {0: 0, 1: 1}
last_num = 1


def compute_next(num) -> int:
    global last_num

    while last_num < num:
        results[last_num + 1] = results[last_num] + results[last_num - 1]
        last_num += 1


@eval_time
@lru_cache(500)
@validate(max_val=config.FIBONACCI_MAX_VALUE)
def fibonacci(n) -> int:
    global last_num

    if n < last_num:
        return results[n]

    if n > last_num:
        compute_next(n)

    return results[last_num]
