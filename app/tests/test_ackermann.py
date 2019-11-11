"""Ackermann Tests Module
"""
from app.ackermann import ackermann
from app.exceptions import ValidationError
import pytest
from random import randint


def test_ackermann_raises_exception_with_invalid_values():
    """Function tests Ackermann(m,n) with invalid values.
            1. Ackermann(-1, 10) where m is a negative value.
            2. Ackermann(2, -1) where n is a negative value.
            3. Ackermann(6, 1) where m exceeds the max limit (5).
            4. Ackermann(5, 2) where n exceeds the max limit for n (0) when m == 5.
            5. Ackermann("string", "string") testing with non-Integer values.

    """
    with pytest.raises(ValidationError):
        ackermann(-1, 10)

    with pytest.raises(ValidationError):
        ackermann(2, -1)

    with pytest.raises(ValidationError):
        ackermann(6, 1)

    with pytest.raises(ValidationError):
        ackermann(5, 2)

    with pytest.raises(TypeError):
        ackermann("string", "string")


def test_ackermann_with_valid_input():
    """Functions test Ackermann with valid input
    """

    n = randint(0, 1000)
    result, _ = ackermann(0, n)
    assert result == n + 1

    n = randint(0, 1000)
    result, _ = ackermann(1, n)
    assert result == n + 2

    n = randint(0, 1000)
    result, _ = ackermann(1, n)
    assert result == n + 2

    n = randint(0, 100)
    result, _ = ackermann(2, n)
    assert result == 2 * n + 3

    n = randint(0, 100)
    result, _ = ackermann(3, n)
    assert result == 2 ** (n + 3) - 3

    result, _ = ackermann(4, 0)
    assert result == 13

    result, _ = ackermann(4, 1)
    assert result == 65533

    result, _ = ackermann(5, 0)
    assert result == 65533
