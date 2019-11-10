from starlette.testclient import TestClient
from api.views import api
from fastapi.exceptions import HTTPException, RequestValidationError
import pytest
import config

client = TestClient(api)

endpoint = "/factorial/"


def test_factorial_with_valid_data():
    response = client.post(endpoint, json={"n": 5})
    assert response.status_code == 200
    assert response.json()["result"] == 120


def test_factorial_with_invalid_data():
    with pytest.raises(HTTPException):
        client.post(endpoint, json={"n": -1})

    with pytest.raises(HTTPException):
        client.post(endpoint, json={"n": config.FACTORIAL_MAX_VALUE + 1})

    with pytest.raises(RequestValidationError):
        client.post(endpoint, json={"n": "hello"})
