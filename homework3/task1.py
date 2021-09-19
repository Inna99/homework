# In previous homework task 4, you wrote a cache function that remembers other function output value.
# Modify it to be a parametrized decorator, so that the following code:
#
# @cache(times=3)
# def some_function():
#     pass
# Would give out cached value up to times number only. Example:
#
# @cache(times=2)
# def f():
#     return input('? ')   # careful with input() in python2, use raw_input() instead
#
# >>> f()
# ? 1
# '1'
# >>> f()     # will remember previous value
# '1'
# >>> f()     # but use it up to two times only
# '1'
# >>> f()
# ? 2
# '2'
import functools
from typing import Callable, Dict


def cache(times=5):
    def one_more_func(func: Callable) -> Callable:
        """Hash function with the parameter"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = args + tuple(kwargs.items())
            if cache_key not in wrapper_cache:
                wrapper_cache[cache_key] = [func(*args, **kwargs), times]
                print("?")
                return wrapper_cache[cache_key]
            else:
                wrapper_cache[cache_key][1] -= 1
                if wrapper_cache[cache_key][1] == 0:
                    return wrapper_cache.pop(cache_key)
                return wrapper_cache[cache_key]

        wrapper_cache: Dict[int, int] = dict()
        return wrapper

    return one_more_func
