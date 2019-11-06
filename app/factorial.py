from functools import lru_cache
from app.exceptions import ValidationError

results = []


def validate(num):
    if not isinstance(num, int):
        raise TypeError("Only Integer Values are allowed")
    if num < 0:
        raise ValidationError("Negative numbers are not allowed")
    if num > 10000:
        # Try to compute factorial on google calculator with more than 170
        # it will return undefined
        raise ValidationError("Input exceed maximum allowed limit")


def compute(fact, next_value, num):
    while next_value <= num:
        fact = fact * next_value
        next_value += 1
        results.append(fact)
    return results[-1]


@lru_cache(100)
def factorial(num):
    validate(num)

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
