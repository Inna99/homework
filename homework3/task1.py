import functools
from typing import Callable, Dict


def cache(times: int = 5):
    def one_more_func(func: Callable) -> Callable:

        """Hash function with the parameter"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = args + tuple(kwargs.items())
            if cache_key not in wrapper_cache:
                result = func(*args, **kwargs)
                wrapper_cache[cache_key] = [id(func), times, result]
                return wrapper_cache[cache_key][2]
            else:
                wrapper_cache[cache_key][1] -= 1
                result = wrapper_cache[cache_key][2]

                if wrapper_cache[cache_key][1] == 0:
                    wrapper_cache.pop(cache_key)
                return result

        wrapper_cache: Dict = dict()
        return wrapper

    return one_more_func
