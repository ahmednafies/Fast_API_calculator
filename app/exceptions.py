class Error(Exception):
    """Base class for other exceptions"""

    pass


class NegativeNumbersNotAllowed(Error):
    """Raised when a negative number is passed to a method"""

    pass

