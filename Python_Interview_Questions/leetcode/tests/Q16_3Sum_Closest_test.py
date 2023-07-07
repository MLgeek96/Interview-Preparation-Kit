import pytest
from leetcode.problem_sets.Q16_3Sum_Closest import threeSumClosest

print(threeSumClosest.__doc__)

def test_3Sum_Closest():
    nums = [-1,2,1,-4]
    target = 1
    assert threeSumClosest(nums, target) == 2

    nums = [0, 2, 1, -3]
    target = 1
    assert threeSumClosest(nums, target) == 0

    nums = [1, 2, 4, 8, 16, 32, 64, 128]
    target = 82
    assert threeSumClosest(nums, target) == 82