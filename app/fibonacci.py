from functools import lru_cache

results = []


def compute(n) -> int:
    if n <= 1:
        return n
    return compute(n - 1) + compute(n - 2)


def compute_next(diff, sequence) -> int:
    for index in range(diff):
        sequence.append(results[-1] + results[-2])
    return sequence


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
        diff = n - len(results)
        results = results + compute_next(diff, results)
        return results[-1]

    return results[-1]
