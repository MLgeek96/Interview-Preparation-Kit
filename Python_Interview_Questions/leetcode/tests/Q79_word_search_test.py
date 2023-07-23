import pytest
from leetcode.problem_sets.Q79_word_search import exist

print(exist.__doc__)

def test_exist():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    assert exist(board, word) is True

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    assert exist(board, word) is True

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    assert exist(board, word) is False
    