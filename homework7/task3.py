from typing import List


def list_merge(list_lists):
    return [x for lst in list_lists for x in lst]


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Given a Tic-Tac-Toe 3x3 board (can be unfinished).
    Write a function that checks if the are some winners.
    If there is "x" winner, function should return "x wins!"
    If there is "o" winner, function should return "o wins!"
    If there is a draw, function should return "draw!"
    If board is unfinished, function should return "unfinished!"
    """
    board_lst = list_merge(board)
    masks = ["012", "345", "678", "036", "147", "258", "048", "246"]
    unfinished = False
    for mask in masks:
        one, two, three = map(int, list(mask))
        set_ = {board_lst[one], board_lst[two], board_lst[three]}
        if set_.union({"o"}) == {"o"}:
            return "o wins!"
        elif set_.union({"x"}) == {"x"}:
            return "x wins!"
        elif set_.intersection({"-"}) == {"-"} and len(set_) < 3:
            unfinished = True

    if unfinished is True:
        return "unfinished"
    else:
        return "draw!"
