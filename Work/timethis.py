# ruff: noqa: ANN201,ANN202,ANN001,

# timethis.py
#
# Exercise 7.10

import time


def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__module__}.{func.__name__}: {end - start:.2f}s")
        return result

    return wrapper
