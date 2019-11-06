from fastapi import HTTPException


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
            detail=f"max factorial number input is ({max_val}), Swagger API is unable to view more than f({max_val})",
        )

    return True


def factorial_valid_input(number):
    return is_valid_input(number, 0, 2000)


def fibonacci_valid_input(number):
    return is_valid_input(number, 0, 20000)

