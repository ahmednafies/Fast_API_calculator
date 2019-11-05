from functools import lru_cache


@lru_cache(100)
def factorial(n):
    # TODO: raise negative numbers exceptions
    # TODO: add maximum number validation
    # TODO: Save last computation
    if n > 1:
        return n * factorial(n - 1)
    return 1
