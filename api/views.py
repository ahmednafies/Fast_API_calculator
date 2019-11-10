from fastapi import APIRouter

from api.models import AckermannModel, FactorialModel, FibonacciModel, Response
from app.ackermann import ackermann
from app.factorial import factorial
from app.fibonacci import fibonacci

api = APIRouter()


@api.post("/fibonacci/", response_model=Response, status_code=200)
def fibonacci_view(model: FibonacciModel):
    result, time = fibonacci(model.n)
    return {"result": result, "time": time}


@api.post("/ackermann/", response_model=Response, status_code=200)
def ackermann_view(model: AckermannModel):
    result, time = ackermann(model.values.m, model.values.n)
    return {"result": result, "time": time}


@api.post("/factorial/", response_model=Response, status_code=200)
def factorial_view(model: FactorialModel):
    result, time = factorial(model.n)
    return {"result": result, "time": time}
