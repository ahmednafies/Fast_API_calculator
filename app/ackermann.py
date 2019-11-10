from functools import lru_cache
from app.utils import eval_time


def knuth_to_power(n):
    result = 2
    while n >= 0:
        result = result ** 2
        n -= 1
    return result


def compute(m, n):
    if m == 0:
        return n + 1

    if m == 1:
        return n + 2

    if m == 2:
        return 2 * n + 3

    if m == 3:
        return 2 ** (n + 3) - 3

    if m == 4:
        return (2 ** knuth_to_power(n)) - 3

    if m == 5:
        return (2 ** knuth_to_power(0)) - 3


@eval_time
@lru_cache(100)
def ackermann(m, n):
    result = compute(m, n)
    return result
