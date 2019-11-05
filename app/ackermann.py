import sys
from functools import lru_cache

sys.setrecursionlimit(10000)


@lru_cache(100)
def ackermann(m, n):
    # TODO: raise negative numbers exceptions
    # TODO: max number
    # Save last computation
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)

    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
