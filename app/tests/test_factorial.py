from app.factorial import factorial
from app.exceptions import ValidationError
import pytest
import config
import math

factorial_sequence = [math.factorial(num) for num in range(10)]


def test_factorial_raises_exception_with_invalid_values():
    with pytest.raises(ValidationError):
        factorial(-1)

    with pytest.raises(ValidationError):
        factorial(config.FACTORIAL_MAX_VALUE + 1)

    with pytest.raises(TypeError):
        factorial("string")


def test_factorial_with_valid_data():
    for index, value in enumerate(factorial_sequence):
        fact, _ = factorial(index)
        assert fact == value

    fact, _ = factorial(15)
    assert fact == math.factorial(15)
