from fastapi import APIRouter
from app.fibonacci import fibonacci
from app.ackermann import ackermann
from app.factorial import factorial
from api.models import Response, FactorialModel, AckermannModel, FibonacciModel

api = APIRouter()


@api.post("/fibonacci/", response_model=Response, status_code=200)
def fibonacci_view(model: FibonacciModel):
    result, time = fibonacci(model.n)
    return {"result": result, "time": time}


@api.post("/akermann/", response_model=Response, status_code=200)
def ackermann_view(model: AckermannModel):
    result, time = ackermann(model.m, model.n)
    return {"result": result, "time": time}


@api.post("/factorial", response_model=Response, status_code=200)
def factorial_view(model: FactorialModel):
    result, time = factorial(model.n)
    return {"result": result, "time": time}
