from functools import lru_cache


class Fibonacci:

    previous_results = {}

    def __init__(self, n):
        self.n = n

    def compute(self, n, m) -> int:
        if n <= 1:
            return n
        return self.compute(n - 1) + self.compute(n - 2)

    @lru_cache(100)
    def get_sequence(self) -> list:
        # TODO: raise negative numbers exceptions
        # TODO: add maximum number validation
        # TODO: save last computation

        return [self.compute(i) for i in range(self.n)]
