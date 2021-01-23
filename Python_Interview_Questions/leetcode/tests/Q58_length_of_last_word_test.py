import pytest
from leetcode.problem_sets.Q58_length_of_last_word import lengthOfLastWord

def test_length_of_last_word():
    s = "Hello World"
    assert lengthOfLastWord(s) == 5

    s = " "
    assert lengthOfLastWord(s) == 0

    s = "a "
    assert lengthOfLastWord(s) == 1