from app.fibonacci import fibonacci
from app.exceptions import ValidationError
import pytest
import config


def fibonacci_sequence(n):
    result = [0]
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def test_fibonacci_raises_exception_with_invalid_values():
    with pytest.raises(ValidationError):
        fibonacci(-1)

    with pytest.raises(ValidationError):
        fibonacci(config.FIBONACCI_MAX_VALUE + 1)

    with pytest.raises(TypeError):
        fibonacci("string")


def test_fibonacci_with_valid_data():
    for index, value in enumerate(fibonacci_sequence(10)):
        fib, _ = fibonacci(index)
        assert fib == value

    fib, _ = fibonacci(15)
    fib = fibonacci_sequence(15)[-1]
