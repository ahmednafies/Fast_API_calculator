from fastapi import HTTPException


def is_valid_input(name, val, min_val, max_val):
    if not isinstance(val, int):
        raise HTTPException(
            status_code=400,
            detail=f"input must be a positive integer for '{name}'",
        )

    if val < min_val:
        raise HTTPException(
            status_code=400,
            detail=f"negative numbers are not allowed for '{name}'",
        )

    if val > max_val:
        raise HTTPException(
            status_code=400,
            detail=f"max number allowed for '{name}' is ({max_val})",
        )

    return True

