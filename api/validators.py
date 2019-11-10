# -*- coding: utf-8 -*-
"""API Validators Module

This module contains functionality used to validate request data

"""
from fastapi import HTTPException


def is_valid_input(name: str, val, max_val: int) -> bool:
    """Method validates input value.
    1. Input must be of type "int".
    2. Input must be > 0.
    3. Input must be < max_val.
    
    Args:
        name (str): Name of the input, used for message display.
        val (int): Input to be validated.
        max_val (int): Maximum allowed value for the input.
    
    Raises:
        HTTPException: raised when input is < 0 or > max_val or not of type "int".
    
    Returns:
        bool: True, when all validations are passed
    """
    if not isinstance(val, int):
        raise HTTPException(
            status_code=422,
            detail=f"input must be a positive integer for '{name}'",
        )

    if val < 0:
        raise HTTPException(
            status_code=422,
            detail=f"negative numbers are not allowed for '{name}'",
        )

    if val > max_val:
        raise HTTPException(
            status_code=422,
            detail=f"max number allowed for '{name}' is ({max_val})",
        )

    return True
