import sys
from functools import lru_cache
from app.utils import eval_time

sys.setrecursionlimit(10000)


def compute(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return compute(m - 1, 1)

    if m > 0 and n > 0:
        return compute(m - 1, compute(m, n - 1))


@eval_time
@lru_cache(100)
def ackermann(m, n):
    result = compute(m, n)
    return result
