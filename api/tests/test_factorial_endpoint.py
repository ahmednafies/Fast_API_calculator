# -*- coding: utf-8 -*-
"""Factorial Endpoint Tests Module.
"""
from starlette.testclient import TestClient
from api.views import api
from fastapi.exceptions import HTTPException, RequestValidationError
import pytest
import config

client = TestClient(api)

endpoint = "/factorial/"


def test_factorial_with_valid_data():
    """Function tests Factorial with valid data"""
    response = client.post(endpoint, json={"n": 5})
    assert response.status_code == 200
    assert response.json()["result"] == 120


def test_factorial_with_invalid_data():
    """Function tests Factorial with invalid data
        1. Non-integer value
        2. Factorial(n) where n is a negative number
        3. Factorial(n) where n exceeds the max allowed value.
    """
    with pytest.raises(RequestValidationError):
        client.post(endpoint, json={"n": "hello"})

    with pytest.raises(HTTPException):
        client.post(endpoint, json={"n": -1})

    with pytest.raises(HTTPException):
        client.post(endpoint, json={"n": config.FACTORIAL_MAX_VALUE + 1})

