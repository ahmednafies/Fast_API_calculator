from functools import lru_cache

results = [0, 1]


def compute_next(start, end) -> int:
    count = start
    while count < end:
        results.append(results[-2] + results[-1])
        count += 1


@lru_cache(100)
def fibonacci(n) -> int:
    # TODO: raise negative numbers exceptions
    # TODO: add maximum number validation
    # TODO: save last computation
    if n < 0:
        print("Please enter a positive integer")

    if n == 0 or n == 1:
        return n

    if len(results) == 2:
        n = n - 1  # because we already have values in the results
        compute_next(0, n)
        return results[-1]

    if n < len(results):
        return results[n]

    if n > len(results):
        compute_next(len(results), n + 1)
        return results[-1]

    return results[-1]
