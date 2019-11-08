from functools import lru_cache
from app.utils import eval_time, validate
import config

results = {0: 1, 1: 1}
last_num = 1


def compute_next(num):
    global last_num

    while last_num < num:
        next_num = last_num + 1
        fact = next_num * results[last_num]
        results[next_num] = fact
        last_num += 1


@eval_time
@lru_cache(500)
@validate(
    min_val=config.FACTORIAL_MIN_VALUE, max_val=config.FACTORIAL_MAX_VALUE
)
def factorial(num):
    global last_num
    if num < last_num:
        return results[num]

    if num > last_num:
        compute_next(num)

    return results[last_num]
