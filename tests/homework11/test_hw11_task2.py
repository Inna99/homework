from homework11.strategy import NoDiscount, BasicDiscount, DayDiscount, Order


def test_orders():
    orders = [
        Order(100, NoDiscount()),
        Order(100, BasicDiscount(0.20)),
        Order(100, DayDiscount([i for i in range(0, 32)], 0.20)),
    ]

    assert orders[0].final_price() == 100
    assert orders[1].final_price() == 80.0
    assert orders[2].final_price() == 80.0
