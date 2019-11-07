import time


def eval_time(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()
        total_time = f"{(end - start) * 1000} ms"
        return result, total_time

    return timed
