from functools import lru_cache

results = {}


@lru_cache(100)
def factorial(n):
    # TODO: raise negative numbers exceptions
    # TODO: add maximum number validation
    # TODO: Save last computation
    global results
    if n > 1:
        index = 1
        fact = 1
        while index <= n:
            fact = fact * index
            index += 1
        return fact
    return 1
