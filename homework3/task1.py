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
# 3-1 странный тест как по мне.. проверяет последовательность принтов а не логику функции.
# я думаю стоит завернуть функцию которая делает return list() или еще какойто объект и
# проверять ссылки через is. на первом вызове запомнила ссылку, следующие 4 возвращало ее же на 5ом она сменилась.
# ну и с другим параметром потом. и собственно потому что ты возвращаемый результат не проверяла ты пропустила что у
# тебя возвращается список результат функции + количество повторений а не сам результат.
# да и в примере там знак вопроса это в оборачиваемой функции запрос инпута.
# чтоб наглядно показать что инпут то вызывается то не вызывается, а не отладочная информация кеша)
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


@cache(times=2)
def func(a, b):
    return (a + b) ** 2
