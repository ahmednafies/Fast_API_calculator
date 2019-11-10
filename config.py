FACTORIAL_MAX_VALUE: int = 20000
FIBONACCI_MAX_VALUE: int = 2000
ACKERMANN_LIMITS: dict = {
    "m": {
        0: {"n": {"max": 10000000000}},
        1: {"n": {"max": 10000000000}},
        2: {"n": {"max": 10000000000}},
        3: {"n": {"max": 10000}},
        4: {"n": {"max": 3}},
        5: {"n": {"max": 0}},
    }
}

ACKERMANN_M_MAX: int = list(ACKERMANN_LIMITS["m"].keys())[-1]
