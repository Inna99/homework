from datetime import datetime

from homework3.task2 import sum_slow_calculate_from_0_to_500


def test_how_fast():
    start_time = datetime.now()
    sum_slow_calculate_from_0_to_500()
    assert (datetime.now() - start_time).seconds < 60
