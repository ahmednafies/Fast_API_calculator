# -*- coding: utf-8 -*-
"""Ackermann Endpoint Tests Module.
"""

from starlette.testclient import TestClient
from api.views import api
from fastapi.exceptions import HTTPException, RequestValidationError
import pytest

client = TestClient(api)

endpoint = "/ackermann/"


def test_ackermann_with_valid_data():
    """Function tests Ackermann(m,n) with valid data"""

    response = client.post(endpoint, json={"values": {"m": 4, "n": 0}})
    assert response.status_code == 200
    assert response.json()["result"] == 13


def test_ackermann_with_invalid_data():
    """Function tests Ackermann with invalid data
        1. Non-integer value
        2. Ackermann(m,n) where m is a negative number
        3. Ackermann(m,n) where n is a negative number
        4. Ackermann(m,n) where m exceeds the max allowed value
        5. Ackermann(m,n) where n exceeds the max allowed value for its corresponding m value
    """

    with pytest.raises(RequestValidationError):
        client.post(endpoint, json={"values": {"m": "string", "n": "string"}})

    with pytest.raises(HTTPException):
        client.post(endpoint, json={"values": {"m": -1, "n": 5}})

    with pytest.raises(HTTPException):
        client.post(endpoint, json={"values": {"m": 2, "n": -1}})

    with pytest.raises(HTTPException):
        client.post(endpoint, json={"values": {"m": 6, "n": 0}})

    with pytest.raises(HTTPException):
        client.post(endpoint, json={"values": {"m": 4, "n": 4}})
