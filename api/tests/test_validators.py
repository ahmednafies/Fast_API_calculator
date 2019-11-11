# -*- coding: utf-8 -*-
"""API Validators Endpoint Tests Module.
"""
from fastapi.exceptions import HTTPException
import pytest
from api.validators import is_valid_input


def test_validator_with_valid_data():
    """Function tests validator with valid data"""

    assert is_valid_input("x", 5, 10) == True


def test_validator_with_invalid_data():
    """Function tests validator with invalid data
        1. Non-integer value
        2. where n is a negative number
        3. where n exceeds the max allowed value.
    """
    with pytest.raises(HTTPException):
        is_valid_input("x", "string", 10)

    with pytest.raises(HTTPException):
        is_valid_input("x", -1, 10)

    with pytest.raises(HTTPException):
        is_valid_input("x", 11, 10)
