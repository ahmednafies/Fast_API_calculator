from app.fibonacci import fibonacci
from app.exceptions import ValidationError
import pytest
import config
import math


def fibonacci_sequence(n):
    result = [0]
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def test_fibonacci_raises_exception_with_invalid_values():
    with pytest.raises(ValidationError):
        fibonacci(config.FIBONACCI_MIN_VALUE - 1)

    with pytest.raises(ValidationError):
        fibonacci(config.FIBONACCI_MAX_VALUE + 1)

    with pytest.raises(TypeError):
        fibonacci("string")


def test_fibonacci_with_valid_data():
    print(fibonacci_sequence(10))
    for index, value in enumerate(fibonacci_sequence(10)):
        fact, _ = fibonacci(index)
        assert fact == value

