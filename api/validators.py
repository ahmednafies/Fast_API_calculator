from fastapi import HTTPException
import config


def is_valid_input(number, min_val, max_val):
    if not isinstance(number, int):
        raise HTTPException(
            status_code=400, detail="Input must be a positive integer"
        )

    if number < min_val:
        raise HTTPException(
            status_code=400, detail="negative numbers are not allowed"
        )

    if number > max_val:
        raise HTTPException(
            status_code=400,
            detail=f"max factorial number input is ({max_val})",
        )

    return True


def factorial_valid_input(number):
    return is_valid_input(
        number, config.FACTORIAL_MIN_VALUE, config.FACTORIAL_MAX_VALUE
    )


def fibonacci_valid_input(number):
    return is_valid_input(
        number, config.FIBONACCI_MIN_VALUE, config.FIBONACCI_MAX_VALUE
    )

