# -*- coding: utf-8 -*-
"""Fibonacci Endpoint Tests Module.
"""
from starlette.testclient import TestClient
from api.views import api
from fastapi.exceptions import HTTPException, RequestValidationError
import pytest
import config

client = TestClient(api)


def test_fibonacci_with_valid_data():
    """Function tests Fibonacci with valid data"""

    response = client.post("/fibonacci/", json={"n": 10})
    assert response.status_code == 200
    assert response.json()["result"] == 55


def test_fibonacci_with_invalid_data():
    """Function tests Fibonacci with invalid data
        1. Non-integer value
        2. Fibonacci(n) where n is a negative number
        3. Fibonacci(n) where n exceeds the max allowed value.
    """
    with pytest.raises(RequestValidationError):
        client.post("/fibonacci/", json={"n": "hello"})

    with pytest.raises(HTTPException):
        client.post("/fibonacci/", json={"n": -1})

    with pytest.raises(HTTPException):
        client.post("/fibonacci/", json={"n": config.FIBONACCI_MAX_VALUE + 1})

