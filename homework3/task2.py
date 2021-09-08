import time
import struct
import random
import hashlib
from multiprocessing.pool import ThreadPool
from multiprocessing import Process, Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

# Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
# Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
# You are not allowed to modify slow_calculate function.


def sum_slow_calculate_from0_to500():
    # return sum(Process(target=slow_calculate, args=(i,)) for i in range(500))
    # slow_calculate_result = []
    # pool = ThreadPool(processes=1)
    # for i in range(5):
    #     p = Process(target=slow_calculate, args=(i,))
    #     print(p)
    #     slow_calculate_result.append(p)
    #     p.start()
    #
    # for elem in slow_calculate_result:
    #     print(elem.get())

    #
    # with Pool() as pool:
    #     results = [pool.apply_async(slow_calculate, (i,)) for i in range(5)]
    #     pool.close()
    #     pool.join()
    #
    # results = [result.get() for result in results]
    # print(results)
    with Pool(8) as pool:
        answer = sum(pool.map(slow_calculate, list(range(500))))
    print(answer)


print(sum_slow_calculate_from0_to500())
print(slow_calculate(1))
