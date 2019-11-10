FACTORIAL_MIN_VALUE: int = 0
FACTORIAL_MAX_VALUE: int = 20000
FIBONACCI_MIN_VALUE: int = 0
FIBONACCI_MAX_VALUE: int = 2000
ACKERMANN_LIMITS: dict = {
    "m": {
        0: {"n": {"min": 0, "max": 10000000000}},
        1: {"n": {"min": 0, "max": 10000000000}},
        2: {"n": {"min": 0, "max": 10000000000}},
        3: {"n": {"min": 0, "max": 10000}},
        4: {"n": {"min": 0, "max": 3}},
        5: {"n": {"min": 0, "max": 0}},
    }
}

ACKERMANN_M_MIN: int = list(ACKERMANN_LIMITS["m"].keys())[0]
ACKERMANN_M_MAX: int = list(ACKERMANN_LIMITS["m"].keys())[-1]
