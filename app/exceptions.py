class Error(Exception):
    """Base class for other exceptions"""

    pass


class NegativeNumbersNotAllowed(Error):
    """Raised when a negative number is passed to a method"""

    pass


class NumberExceedsTheMaximumLimit(Error):
    """Raised when a number exceeds max allowed limit"""

    pass
