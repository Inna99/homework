from homework4.task5 import fizzbuzz


def test_fizzbuzz():
    """checks the type of the returned object"""
    assert str(type(fizzbuzz(5))) == "<class 'generator'>"


def test_fizzbuzz_list():
    """checks that returned FizzBuzz numbers"""
    assert list(fizzbuzz(5)) == ["1", "2", "fizz", "4", "buzz"]
