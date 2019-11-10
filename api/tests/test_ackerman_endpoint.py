from starlette.testclient import TestClient
from api.views import api
from fastapi.exceptions import HTTPException, RequestValidationError
import pytest

client = TestClient(api)

endpoint = "/ackermann/"


def test_ackermann_with_valid_data():
    response = client.post(endpoint, json={"values": {"m": 4, "n": 0}})
    assert response.status_code == 200
    assert response.json()["result"] == 13


def test_ackermann_with_invalid_data():
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
