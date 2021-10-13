from homework7.task3 import tic_tac_toe_checker


def test_tic_tac_toe_checker_draw():
    """Check "draw!" endpoint"""
    z = [["o", "o", "o"], ["-", "x", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(z) == "draw!"


def test_tic_tac_toe_checker_unfinished():
    """Check "unfinished" endpoint"""
    z = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(z) == "unfinished!"


def test_tic_tac_toe_checker_unfinished_wins():
    """Check "x wins!" endpoint"""
    z = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(z) == "x wins!"

    z = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(z) == "o wins!"
