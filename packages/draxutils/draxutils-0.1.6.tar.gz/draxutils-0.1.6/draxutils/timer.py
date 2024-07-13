# simple_timer.py

import time
from contextlib import ContextDecorator

class Timer(ContextDecorator):
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, *exc):
        self.end_time = time.time()
        return False

    def __str__(self):
        return f"Elapsed time: {self.elapsed:.6f} seconds"

    @property
    def elapsed(self):
        if self.end_time is None:
            return time.time() - self.start_time
        return self.end_time - self.start_time

"""timer = Timer()  # Create a global timer instance for easy import

# Usage as context manager
def time_this():
    with timer:
        yield

# Usage as decorator
def timed(func):
    @Timer()
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper"""