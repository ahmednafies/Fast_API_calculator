from functools import lru_cache


class Fibonacci:

    previous_results = {}

    def __init__(self, n):
        self.n = n

    def _compute(self, n) -> int:
        if n <= 1:
            return n
        return self._compute(n - 1) + self._compute(n - 2)

    @lru_cache(100)
    def get_sequence(self) -> list:
        # TODO: raise negative numbers exceptions
        # TODO: add maximum number validation
        # TODO: save last computation

        return [self._compute(i) for i in range(self.n)]
