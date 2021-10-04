from typing import List


def list_merge(list_lists):
    return [x for lst in list_lists for x in lst]


class Checker:
    def __init__(self):
        self.o_wins = False
        self.x_wins = False
        self.draw = False
        self.unfinished = False


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Given a Tic-Tac-Toe 3x3 board (can be unfinished).
    Write a function that checks if the are some winners.
    If there is "x" winner, function should return "x wins!"
    If there is "o" winner, function should return "o wins!"
    If there is a draw, function should return "draw!"
    If board is unfinished, function should return "unfinished!"
    """
    checker = Checker()
    board_lst = list_merge(board)
    masks = ["012", "345", "678", "036", "147", "258", "048", "246"]
    for mask in masks:
        one, two, three = map(int, list(mask))
        set_ = {board_lst[one], board_lst[two], board_lst[three]}
        if set_ == {"o"}:
            checker.o_wins = True
        elif set_ == {"x"}:
            checker.x_wins = True
        elif {"-"}.issubset(set_) and len(set_) != 3:
            checker.unfinished = True

    if checker.o_wins and checker.x_wins:
        return "draw!"
    elif checker.x_wins:
        return "x wins!"
    elif checker.o_wins:
        return "o wins!"
    elif checker.unfinished:
        return "unfinished!"
    else:
        return "draw!"
