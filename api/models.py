from pydantic import BaseModel, validator
from api.validators import is_valid_input
import config


class Response(BaseModel):
    result: int
    time: str


class FibonacciModel(BaseModel):
    n: int

    @validator("n")
    def n_is_valid(cls, value):
        is_valid_input("n", value, config.FIBONACCI_MAX_VALUE)
        return value


class AckermannValues(BaseModel):
    m: int
    n: int


class AckermannModel(BaseModel):
    values: AckermannValues

    @validator("values")
    def is_valid(cls, values):
        m, n = values.m, values.n
        is_valid_input("m", m, config.ACKERMANN_M_MAX)
        n_max_val = config.ACKERMANN_LIMITS["m"][m]["n"]["max"]
        is_valid_input("n", n, n_max_val)
        return values


class FactorialModel(BaseModel):
    n: int

    @validator("n")
    def is_valid(cls, value):
        is_valid_input("n", value, config.FACTORIAL_MAX_VALUE)
        return value
