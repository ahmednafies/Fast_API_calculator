"""Factorial Test Module
"""
from app.factorial import factorial
from app.exceptions import ValidationError
import pytest
import config
import math


def test_factorial_raises_exception_with_invalid_values():
    """Function tests Factorial with invalid input
        1. Negative value input
        2. Value that exceeds the max limit
        3. Non-integer value
    """
    with pytest.raises(ValidationError):
        factorial(-1)

    with pytest.raises(ValidationError):
        factorial(config.FACTORIAL_MAX_VALUE + 1)

    with pytest.raises(TypeError):
        factorial("string")


def test_factorial_with_valid_data():
    """Function tests factorial with valid data"""

    factorial_sequence = [math.factorial(num) for num in range(10)]

    for index, value in enumerate(factorial_sequence):
        fact, _ = factorial(index)
        assert fact == value

    fact, _ = factorial(15)
    assert fact == math.factorial(15)
