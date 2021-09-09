import time
import struct
import random
import hashlib
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def sum_slow_calculate_from_0_to_500():
    """Summa 500 calls slow_calculate"""
    with Pool(32) as pool:
        answer = sum(pool.map(slow_calculate, list(range(500))))
    return answer
