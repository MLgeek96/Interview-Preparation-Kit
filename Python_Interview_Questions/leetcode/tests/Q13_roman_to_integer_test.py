import pytest
from leetcode.problem_sets.Q13_roman_to_integer import romanToInt

def test_roman_to_integer():
    s = "III"
    assert romanToInt(s) == 3

    s = "IV"
    assert romanToInt(s) == 4

    s = "IX"
    assert romanToInt(s) == 9

    s = "LVIII"
    assert romanToInt(s) == 58

    s = "MCMXCIV"
    assert romanToInt(s) == 1994

