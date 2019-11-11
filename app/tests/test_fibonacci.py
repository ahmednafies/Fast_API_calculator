"""Fibonacci Tests Module
"""
from app.fibonacci import fibonacci
from app.exceptions import ValidationError
import pytest
import config


def test_fibonacci_raises_exception_with_invalid_values():
    """Function tests Factorial with invalid input
        1. Negative value input
        2. Value that exceeds the max limit
        3. Non-integer value
    """
    with pytest.raises(ValidationError):
        fibonacci(-1)

    with pytest.raises(ValidationError):
        fibonacci(config.FIBONACCI_MAX_VALUE + 1)

    with pytest.raises(TypeError):
        fibonacci("string")


def test_fibonacci_with_valid_data():
    """Function tests Fibonacci with valid data"""
    fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    for index, value in enumerate(fib_sequence):
        fib, _ = fibonacci(index)
        assert fib == value

    fib, _ = fibonacci(15)
    assert fib == 610
