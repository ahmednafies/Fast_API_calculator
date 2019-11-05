from fastapi import APIRouter
from app.fibonacci import Fibonacci
from app.ackermann import ackermann
from app.factorial import factorial

api = APIRouter()


@api.get("/")
def root():
    return {"Hello": "World"}


@api.get("/fibonacci/{n}")
def fibonacci_view(n: int):
    return {"result": Fibonacci(n).get_sequence()}


@api.get("/akermann/{m}&{n}")
def ackermann_view(m: int, n: int):
    return {"result": ackermann(m, n)}


@api.get("/factorial/{n}")
def factorial_view(n: int):
    return {"result": factorial(n)}
