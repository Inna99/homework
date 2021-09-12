from homework4.task3 import my_precious_logger

from sys import stderr, stdin


def test_my_precious_logger():
    """Check when string starts with error"""
    assert my_precious_logger("error: file not found") == stdin.read()


def test_myoutput(capsys): # or use "capfd" for fd-level
    print ("hello")
    sys.stderr.write("world\n")
    out, err = capsys.readouterr()
    assert out == "hello\n"
    assert err == "world\n"
    print "next"
    out, err = capsys.readouterr()
    assert out == "next\n"