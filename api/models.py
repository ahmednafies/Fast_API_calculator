from pydantic import BaseModel
from typing import List


class FibonacciResponse(BaseModel):
    result: List[int]


class AckermannResponse(BaseModel):
    result: int


class FactorialResponse(BaseModel):
    result: int
