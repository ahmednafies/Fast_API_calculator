from fastapi import APIRouter
from app.fibonacci import fibonacci
from app.ackermann import ackermann
from app.factorial import factorial
from api.validators import factorial_valid_input, fibonacci_valid_input
from api.models import Int

api = APIRouter()


@api.get("/fibonacci/{n}", response_model=Int, status_code=200)
def fibonacci_view(n: int):
    if fibonacci_valid_input(n):
        result, time = fibonacci(n)
        return {"result": result, "time": time}


@api.get("/akermann/{m}&{n}", response_model=Int, status_code=200)
def ackermann_view(m: int, n: int):
    return {"result": ackermann(m, n)}


@api.get("/factorial/{n}", response_model=Int, status_code=200)
def factorial_view(n: int):
    if factorial_valid_input(n):
        result, time = factorial(n)
        return {"result": result, "time": time}
