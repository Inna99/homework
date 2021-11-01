"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with suppressor(IndexError):
...    [][2]
"""
import logging
from contextlib import contextmanager

logging.basicConfig(level=logging.DEBUG)


@contextmanager
def suppressor(*args, **kwargs):
    """Custom generator context manager that suppresses passed exception"""
    ex = args[0]
    try:
        yield
    except ex:
        pass


class Suppressor:
    """Custom class context manager that suppresses passed exception"""

    def __init__(self, exception):
        self.ex = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            logging.info("The exception was not raised")
            return True
        elif exc_type is self.ex:
            logging.info(f"Exception {exc_type} has been handled")
            return True


if __name__ == "__main__":  # pragma: no cover
    pass
