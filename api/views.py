from fastapi import APIRouter
from app.fibonacci import fibonacci
from app.ackermann import ackermann
from app.factorial import factorial
from api.validators import factorial_valid_input
from api.models import Int

api = APIRouter()


@api.get("/")
def root():
    return {"Hello": "Klarna"}


@api.get("/fibonacci/{n}", response_model=Int, status_code=200)
def fibonacci_view(n: int):
    return {"result": fibonacci(n)}


@api.get("/akermann/{m}&{n}", response_model=Int, status_code=200)
def ackermann_view(m: int, n: int):
    return {"result": ackermann(m, n)}


@api.get("/factorial/{n}", response_model=Int, status_code=200)
def factorial_view(n: int):
    if factorial_valid_input(n):
        return {"result": factorial(n)}
