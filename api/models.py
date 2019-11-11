# -*- coding: utf-8 -*-
"""API Models Module

This Module contains the models used for serializing data
and populating Open API documentation for all of the endpoints.
Moreover payload validations happen in this module

"""

from pydantic import BaseModel, validator
from api.validators import is_valid_input
import config


class Response(BaseModel):
    """Class handles the response models for all endpoints
    """

    result: int
    time: str


class FibonacciModel(BaseModel):
    """Class represents the payload model of the Fibonacci endpoint
    """

    n: int

    @validator("n")
    def n_is_valid(cls, value):
        """Method validates the input value 'n' for Fibonacci
        s
        Args:
            value (int): Positive integer value.
        
        Returns:
            int: if value is valid otherwise raises an exception.
        """
        is_valid_input("n", value, config.FIBONACCI_MAX_VALUE)
        return value


class AckermannValues(BaseModel):
    """Class represents the payload model of the Ackermann
    """

    m: int
    n: int


class AckermannModel(BaseModel):
    """Class represents the payload model of the Ackermann.

    The reason that values are handeld in 'AckermannValues'
    is that pydantic can only validate one value at a time.

    However, both values need to be validated together
    for example, if 'm = 4' then 'n' can be '0 < n < 4'
    yet for 'm = 5', 'n' can only be equal to '0'

    """

    values: AckermannValues

    @validator("values")
    def is_valid(cls, values):
        """Method validates the input values 'm' and 'n' for Ackermann
        Args:
            value (AckermannValues):  object of type AckermannValues
        
        Returns:
            AckermannValues: if both values are valid otherwise raises an exception.
        """
        m, n = values.m, values.n
        is_valid_input("m", m, config.ACKERMANN_M_MAX)
        n_max_val = config.ACKERMANN_LIMITS["m"][m]["n"]["max"]
        is_valid_input("n", n, n_max_val)
        return values


class FactorialModel(BaseModel):
    """Class represents the payload model of the Factorial endpoint
    """

    n: int

    @validator("n")
    def is_valid(cls, value):
        """Method validates the input value 'n' for Factorial
    Args:
        value (int): Positive integer value.
    
    Returns:
        int: if value is valid otherwise raises an exception.
    """
        is_valid_input("n", value, config.FACTORIAL_MAX_VALUE)
        return value
