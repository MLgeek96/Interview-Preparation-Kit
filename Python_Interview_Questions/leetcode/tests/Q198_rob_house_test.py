import pytest
from leetcode.problem_sets.Q198_rob_house import rob

print(rob.__doc__)

def test_rob():
    nums = [1,2,3,1]
    assert rob(nums) == 4

    nums = [2,7,9,3,1]
    assert rob(nums) == 12

    nums = [0]
    assert rob(nums) == 0

    nums = [2, 1]
    assert rob(nums) == 2

    nums = [1, 2]
    assert rob(nums) == 2