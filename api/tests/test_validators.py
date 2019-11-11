from fastapi.exceptions import HTTPException
import pytest
from api.validators import is_valid_input


def test_validator_with_valid_data():

    assert is_valid_input("x", 5, 10) == True


def test_validator_with_invalid_data():
    with pytest.raises(HTTPException):
        is_valid_input("x", "string", 10)

    with pytest.raises(HTTPException):
        is_valid_input("x", -1, 10)

    with pytest.raises(HTTPException):
        is_valid_input("x", 11, 10)
