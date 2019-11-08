from functools import lru_cache
from app.validators import is_valid_number
from app.utils import eval_time
import config
import math

results = {}
last_number = 1


def compute(fact, next_num, num):
    global last_number

    while next_num <= num:
        fact = fact * next_num
        results[next_num] = fact
        last_number = next_num
        next_num += 1

    return results[last_number]


@eval_time
@lru_cache(1000)
def factorial(num):
    global last_number

    is_valid_number(
        num, config.FACTORIAL_MIN_VALUE, config.FACTORIAL_MAX_VALUE
    )

    if num == 0:
        return 1

    if not results:
        return compute(1, 1, num)

    if num < last_number:
        return results[num]

    elif num > last_number:
        fact = results[last_number]
        next_num = last_number + 1
        return compute(fact, next_num, num)

    else:
        return results[last_number]
