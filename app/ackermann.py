# -*- coding: utf-8 -*-
"""Ackermann Module

This module contains all functionality required to calculate Ackermann(m,n)

"""
from functools import lru_cache

import config
from app.utils import eval_time, is_valid_number, validate


def knuth_to_power(n):
    """Function handels computing powers of powers of 2.
    example:
        knuth_to_power(0) = 2 ** 2
        knuth_to_power(1) = 2 ** (2 ** 2)
        knuth_to_power(2) = 2 ** (2 ** (2 ** 2)
            ...

    Args:
        n (int): Ackermann input value for Ackermann(m,n)
    
    Returns:
        int: computed value
    """
    result = 2
    while n >= 0:
        result = result ** 2
        n -= 1
    return result


def compute(m, n):
    """Function computes Ackermann (m,n).
    
    Function computes results of Ackermann (m,n) where 0 <= m <= 5.
    Implementing recurssion was quite expensive which is why this function
    has changed to compute Ackermann(m,n) in much simpler manner.

    It was easier to split the function into separate types.

        - m = 0 and  n => 0 , A(m,n) = n + 1
        - m = 1 and  n => 0 , A(m,n) = n + 2
        - m = 2 and  n => 0 , A(m,n) = 2 * n + 3
        - m = 3 and  n => 0 , A(m,n) = 2 ** (n + 3) - 3
        - m = 4 and  n => 0 , A(m,n) = (2 ** knuth_to_power(n)) - 3

        here we are only computing the 1st value
        - m = 5 and  n = 0 , A(4,1) = (2 ** knuth_to_power(1)) - 3


    Args:
        m (int): Ackerman function first argument.
        n (int): Ackerman function second argument.
    
    Returns:
        int: result of Ackermann(m,n)
    """
    if m == 0:
        return n + 1

    if m == 1:
        return n + 2

    if m == 2:
        return 2 * n + 3

    if m == 3:
        return 2 ** (n + 3) - 3

    if m == 4:
        return (2 ** knuth_to_power(n)) - 3

    if m == 5:
        return (2 ** knuth_to_power(1)) - 3


@eval_time
@lru_cache(500)
@validate(config.ACKERMANN_M_MAX)
def ackermann(m, n):
    """Function handels the validation and computation of Ackermann (m,n).  

    Args:
        m (int): Ackerman function first argument.
        n (int): Ackerman function second argument.
    
    Returns:
        int: result of Ackermann(m,n)
    """
    n_max_val = config.ACKERMANN_LIMITS["m"][m]["n"]["max"]
    is_valid_number(n, n_max_val)
    return compute(m, n)
