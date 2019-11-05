from functools import lru_cache

results = []


def compute(n) -> int:
    if n <= 1:
        return n
    return compute(n - 1) + compute(n - 2)


@lru_cache(100)
def fibonacci(n) -> int:
    # TODO: raise negative numbers exceptions
    # TODO: add maximum number validation
    # TODO: save last computation
    n += 1
    global results
    if not results:
        results = [compute(i) for i in range(n)]
        return results[-1]

    if n < len(results):
        return results[n - 1]

    if n > len(results):
        results = results + [compute(i) for i in range(len(results), n)]
        return results[-1]

    return results[-1]
