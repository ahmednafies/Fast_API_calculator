from functools import lru_cache
from app.validators import is_valid_number
from app.utils import eval_time
import config
import math

results = []


def compute(fact, next_value, num):

    while next_value <= num:
        fact = fact * next_value
        next_value += 1
        results.append(fact)
    return results[-1]


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
        return results[num - 1]

    elif num > len(results):
        fact = results[-1]
        next_value = results.index(fact) + 2
        return compute(fact, next_value, num)

    else:
        return results[-1]


@eval_time
def python_factorial(n):
    return math.factorial(n)
