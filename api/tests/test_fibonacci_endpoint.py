from starlette.testclient import TestClient
from api.views import api
from fastapi.exceptions import HTTPException, RequestValidationError
import pytest
import config

client = TestClient(api)


def test_fibonacci_with_valid_data():
    response = client.post("/fibonacci/", json={"n": 10})
    assert response.status_code == 200
    assert response.json()["result"] == 55


def test_fibonacci_with_invalid_data():
    with pytest.raises(HTTPException):
        client.post("/fibonacci/", json={"n": -1})

    with pytest.raises(HTTPException):
        client.post("/fibonacci/", json={"n": config.FIBONACCI_MAX_VALUE + 1})

    with pytest.raises(RequestValidationError):
        client.post("/fibonacci/", json={"n": "hello"})
