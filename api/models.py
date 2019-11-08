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
        is_valid_input(
            "n", value, config.FIBONACCI_MIN_VALUE, config.FIBONACCI_MAX_VALUE
        )
        return value


class AckermannModel(BaseModel):
    m: int
    n: int

    @validator("m")
    def m_is_valid(cls, value):
        is_valid_input(
            "m",
            value,
            config.ACKERMANN_MIN_VALUE[0],
            config.ACKERMANN_MAX_VALUE[0],
        )
        return value

    @validator("n")
    def n_is_valid(cls, value):
        is_valid_input(
            "n",
            value,
            config.ACKERMANN_MIN_VALUE[1],
            config.ACKERMANN_MAX_VALUE[1],
        )
        return value


class FactorialModel(BaseModel):
    n: int

    @validator("n")
    def n_is_valid(cls, value):
        is_valid_input(
            "n", value, config.FACTORIAL_MIN_VALUE, config.FACTORIAL_MAX_VALUE
        )
        return value
