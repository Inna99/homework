from homework11.task2 import *


def test_orders():
    orders = [
        Order(100, NoDiscount()),
        Order(100, BasicDiscount(.20)),
        Order(100, DayDiscount([i for i in range(0, 32)], .20))
    ]

    assert orders[0].final_price() == 100
    assert orders[1].final_price() == 80.
    assert orders[2].final_price() == 80.
