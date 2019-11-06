from functools import lru_cache
from app.exceptions import NegativeNumbersNotAllowed

results = []


def compute(fact, next_value, num):
    while next_value <= num:
        fact = fact * next_value
        next_value += 1
        results.append(fact)
    return results[-1]


@lru_cache(100)
def factorial(num):
    if num < 0:
        raise NegativeNumbersNotAllowed

    elif num == 0:
        return 1

    if not results:
        return compute(1, 1, num)

    if num < len(results):
        return results[num - 1]

    elif num == len(results):
        return results[-1]
    else:
        fact = results[-1]
        next_value = results.index(fact) + 2
        return compute(fact, next_value, num)
