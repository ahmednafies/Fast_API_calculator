from functools import lru_cache

results = []


def compute_first(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
        results.append(num)


def accumulate(n):
    num = results[-1]
    last_index = results.index(results[-1])
    while last_index < n:
        num = num * n
        n = n + 1
        results.append(num)


# @lru_cache(100)
def factorial(n):
    # TODO: raise negative numbers exceptions
    # TODO: add maximum number validation
    # TODO: Save last computation
    if n < 1:
        return 1

    if n > 1:
        compute_first(n)
        return results[-1]

    if n < len(results):
        return results[n]

    if n > len(results):
        accumulate(n)
        return results[-1]
