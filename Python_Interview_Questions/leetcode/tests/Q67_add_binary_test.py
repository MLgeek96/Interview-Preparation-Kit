import pytest
from leetcode.problem_sets.Q67_add_binary import addBinary

def test_add_binary():
    a = "11"
    b = "1"
    assert addBinary(a, b) == "100"

    a = "1010"
    b = "1011"
    assert addBinary(a, b) == "10101"