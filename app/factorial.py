from functools import lru_cache

results = []


def compute(num):
    fact = 1
    if num < 0:
        return 1
    elif num == 0:
        return 1
    else:
        index = 1
        while index <= num:
            fact = fact * index
            index += 1
            results.append(fact)
    return results[-1]


def accumulate(num):
    fact = results[-1]
    index = results.index(fact) + 2
    while index <= num:
        fact = fact * index
        index += 1
        results.append(fact)
    return results[-1]


def factorial(num):
    global results

    if not results:
        return compute(num)

    if num < len(results):
        return results[num - 1]
    elif num == len(results):
        return results[-1]
    else:
        return accumulate(num)

