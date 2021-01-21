import pytest
from leetcode.problem_sets.Q202_happy_number import isHappy

def test_happy_number():
    assert isHappy(19) == True
    assert isHappy(2) == False
    assert isHappy(7) == True