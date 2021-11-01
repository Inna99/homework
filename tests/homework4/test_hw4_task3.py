from homework4.task3 import my_precious_logger


def test_my_precious_logger_error(capsys):
    """Check when string starts with error"""
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found\n"


def test_my_precious_logger_ok(capsys):
    """Check when string not starts with error"""
    my_precious_logger("file not error:  found")
    captured = capsys.readouterr()
    assert captured.out == "OK\n"
