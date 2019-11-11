# -*- coding: utf-8 -*-
"""Fibonacci Module

This module contains all functionality required to calculate Fibonacci(n) = Fibonacci(n - 1) +  Fibonacci(n - 2)

In order to make this computation faster and since Fibonacci is primitive recursive (can be converted to loops)
and in python, recursion is expensive since everytime a function is called a stack frame is allocated. However, that
does not happen with loops which makes it much cheaper to use.

Of course, tail recursion can be utilized to optmize the recursive calls, 
however it is simpler and faster to use loops.

To make it more efficient, values will be stored in a dict.
since average time complexity for retreiveing values is O(1), better than a list O(n)
hence the ugly `last_num` global variable, to keep track of the last computed Fibonacci number

Caching is utilized to give back previously computed results even faster

for example:
    if we are computing f(5), we have to compute f(4), f(3), f(2), f(1)
    and thus previous values will be stored, if we need f(n) where n < 5
    we already have it and get it from the dict right away.

    Now if we need to compute f(n) where n > `last_num` (last saved value for Fibonacci)
    lets assume that the last saved Fibonacci is f(5) and we need to compute f(7).

    f(6) = f(5) + f(4)
    f(7) = f(6) + f(5)

    to minimize the number of iterations.

"""
from functools import lru_cache
from app.utils import eval_time, validate
import config

results = {0: 0, 1: 1}
last_num = 1


@eval_time
@lru_cache(500)
@validate(max_val=config.FIBONACCI_MAX_VALUE)
def fibonacci(num: int) -> int:
    """Function validates input and computes the Fibonacci number.
    Args:
        num (int): num -> fibonacci(num)

    Returns:
        int: result of fibonacci(num) e.g f(10) = 55

    """
    global last_num

    if num < last_num:
        return results[num]

    if num > last_num:
        while last_num < num:
            results[last_num + 1] = results[last_num] + results[last_num - 1]
            last_num += 1

    return results[last_num]
