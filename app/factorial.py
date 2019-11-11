# -*- coding: utf-8 -*-
"""Factorial Module

This module contains all functionality required to calculate Factorial(n) = n ... 5 * 4 * 3 * 2 * 1

In order to make this computation faster and since Factorial is primitive recursive (can be converted to loops)
and in python, recursion is expensive since everytime a function is called a stack frame is allocated. However, that
does not happen with loops which makes it much cheaper to use.

Of course, tail recursion can be utilized to optmize the recursive calls, 
however it is simpler and faster to use loops.

To make it more efficient, values will be stored in a dict.
since average time complexity for retreiveing values is O(1), better than a list O(n)
hence the ugly `last_num` global variable, to keep track of the last computed Factorial

Caching is utilized to give back previously computed results even faster

for example:
    if we are computing f(5), we have to compute f(4), f(3), f(2), f(1)
    and thus previous values will be stored, if we need f(n) where n < 5
    we already have it and get it from the dict right away.

    Now if we need to compute f(n) where n > `last_num` (last saved value for factorial)
    lets assume that the last saved factorial is f(5) and we need to compute f(7).
    f(6) = 6 * f(5)
    f(7) = 7 * f(6)

    to minimize the number of iterations.

"""
from functools import lru_cache
from app.utils import eval_time, validate
import config

results = {0: 1, 1: 1}
last_num = 1


@eval_time
@lru_cache(500)
@validate(max_val=config.FACTORIAL_MAX_VALUE)
def factorial(num: int) -> int:
    """Function validates and computes Factorial
    
    Args:
        num (int): num -> factorial(num) 
    
    Returns:
        int: result of factorial(num) e.g f(5) = 120
    """
    global last_num
    if num < last_num:
        return results[num]

    if num > last_num:
        while last_num < num:
            next_num = last_num + 1
            fact = next_num * results[last_num]
            results[next_num] = fact
            last_num += 1

    return results[last_num]
