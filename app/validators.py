from app.exceptions import ValidationError


def is_valid_number(num, min_val, max_val):
    if not isinstance(num, int):
        raise TypeError("Only Integer Values are allowed")
    if num < min_val:
        raise ValidationError("Negative numbers are not allowed")
    if num > max_val:
        raise ValidationError("Input exceed maximum allowed limit")
