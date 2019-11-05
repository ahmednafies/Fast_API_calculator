from fastapi import APIRouter
from app.fibonacci import Fibonacci
from app.ackermann import ackermann
from app.factorial import factorial

from api.models import FibonacciResponse
from api.models import AckermannResponse
from api.models import FactorialResponse

api = APIRouter()


@api.get("/")
def root():
    return {"Hello": "World"}


@api.get("/fibonacci/{n}", response_model=FibonacciResponse, status_code=200)
def fibonacci_view(n: int):
    return {"result": Fibonacci(n).get_sequence()}


@api.get(
    "/akermann/{m}&{n}", response_model=AckermannResponse, status_code=200
)
def ackermann_view(m: int, n: int):
    return {"result": ackermann(m, n)}


@api.get("/factorial/{n}", response_model=FactorialResponse, status_code=200)
def factorial_view(n: int):
    return {"result": factorial(n)}
