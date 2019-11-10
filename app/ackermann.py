from functools import lru_cache
from app.utils import eval_time
import config
from app.utils import validate
from app.validators import is_valid_number


def knuth_to_power(n):
    result = 2
    while n >= 0:
        result = result ** 2
        n -= 1
    return result


def compute(m, n):
    if m == 0:
        return n + 1

    if m == 1:
        return n + 2

    if m == 2:
        return 2 * n + 3

    if m == 3:
        return 2 ** (n + 3) - 3

    if m == 4:
        return (2 ** knuth_to_power(n)) - 3

    if m == 5:
        return (2 ** knuth_to_power(1)) - 3


@eval_time
@lru_cache(100)
@validate(config.ACKERMANN_M_MIN, config.ACKERMANN_M_MAX)
def ackermann(m, n):
    n_min_val = config.ACKERMANN_LIMITS["m"][m]["n"]["min"]
    n_max_val = config.ACKERMANN_LIMITS["m"][m]["n"]["max"]
    is_valid_number(n, n_min_val, n_max_val)
    result = compute(m, n)
    return result
