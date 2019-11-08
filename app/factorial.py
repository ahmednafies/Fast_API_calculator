from functools import lru_cache
from app.validators import is_valid_number
from app.utils import eval_time
import config
import math

results = {}
last_number = 1


def compute(fact, next_num, num):
    while next_num <= num:
        fact = fact * next_num
        results[next_num] = fact
        last_number = next_num
        next_num += 1

    return results[last_number]


@eval_time
@lru_cache(100)
def factorial(num):
    is_valid_number(
        num, config.FACTORIAL_MIN_VALUE, config.FACTORIAL_MAX_VALUE
    )

    if num == 0:
        return 1

    if not results:
        return compute(1, 1, num)

    if num < len(results):
        print(len(results))
        print(last_number)
        return results[num]

    elif num > len(results):
        fact = results[last_number]
        next_num = last_number + 1
        return compute(fact, next_num, num)

    else:
        return results[last_number]


@eval_time
def python_factorial(n):
    return math.factorial(n)
