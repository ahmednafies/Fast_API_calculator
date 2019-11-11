# -*- coding: utf-8 -*-
"""Utils Module

This module contains all extra functionality required.

    1. Time calculation for functions.
    2. validators for functions.

"""
import time
import functools
from app.exceptions import ValidationError


def eval_time(func):
    """Decorator Function computes time taken for decorated function to excute
    
    """

    def timed(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        total_time = f"{(end - start) * 1000} ms"
        return result, total_time

    return timed


def is_valid_number(num, max_val: int):
    """Function validate a number. 
    
    Args:
        num (int): number to be validated.
        max_val (int): number cannot exceed this value.
    
    Raises:
        TypeError: raised when input is not of type "int".
        ValidationError: raised when the integer number is < 0 or > max_val.
    """

    if not isinstance(num, int):
        raise TypeError("Only Integer Values are allowed")
    if num < 0:
        raise ValidationError("Negative numbers are not allowed")
    if num > max_val:
        raise ValidationError("Input exceed maximum allowed limit")


def validate(max_val=100):
    """Decorator function validated the 1st argument of decorated function
    
    Args:
        max_val (int, optional): max value to be validated for 1st argument. Defaults to 100.
    
    """

    def decorator_validate(func):
        @functools.wraps(func)
        def wrapper_validate(*args, **kwargs):
            num = args[0]
            is_valid_number(num, max_val)
            return func(*args, **kwargs)

        return wrapper_validate

    return decorator_validate
