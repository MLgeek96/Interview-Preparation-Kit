import pytest
from leetcode.problem_sets.Q66_plus_one import plusOne

def test_plusOne():
    digits = [1,2,3]
    assert plusOne(digits) == [1, 2, 4]

    digits = [4,3,2,1]
    assert plusOne(digits) == [4, 3, 2, 2]

    digits = [9]
    assert plusOne(digits) == [1, 0]