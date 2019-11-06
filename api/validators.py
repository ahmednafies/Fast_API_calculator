from fastapi import HTTPException


def factorial_valid_input(n):
    if n < 0:
        raise HTTPException(
            status_code=400, detail="negative numbers are not allowed"
        )

    if n > 170:
        raise HTTPException(
            status_code=400,
            detail="max factorial number input is 170, Swagger API is unable to view more than f(170)",
        )

    return True
