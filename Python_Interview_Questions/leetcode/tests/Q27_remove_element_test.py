import pytest
from leetcode.problem_sets.Q27_remove_element import removeElement

def test_remove_element():
    nums = [3,2,2,3]
    val = 3
    assert removeElement(nums, val) == 2

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    assert removeElement(nums, val) == 5