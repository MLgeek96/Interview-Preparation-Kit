import pytest
from leetcode.problem_sets.Q6_zigzag_conversion import convert

def test_zigzag_conversion():
    s = "PAYPALISHIRING"
    numRows = 3
    ans = convert(s, numRows)

    assert ans == "PAHNAPLSIIGYIR"

    s = "PAYPALISHIRING"
    numRows = 4
    ans = convert(s, numRows)

    assert ans == "PINALSIGYAHRPI"

    s = "A"
    numRows = 1
    ans = convert(s, numRows)

    assert ans == "A"

