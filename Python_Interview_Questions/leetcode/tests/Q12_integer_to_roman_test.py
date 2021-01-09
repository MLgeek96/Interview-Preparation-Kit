import pytest
from leetcode.problem_sets.Q12_integer_to_roman import intToRoman

def test_integer_to_roman():
    num = 3
    assert intToRoman(num) == "III"

    num = 4
    assert intToRoman(num) == "IV"

    num = 9
    assert intToRoman(num) == "IX"

    num = 58
    assert intToRoman(num) == "LVIII"

    num = 1994
    assert intToRoman(num) == "MCMXCIV"
