import pytest
from leetcode.problem_sets.Q15_3Sum import threeSum

print(threeSum.__doc__)

def test_3Sum():
    nums = [-1, 0, 1, 2, -1, -4]
    assert threeSum(nums) == [[-1,-1,2],[-1,0,1]]

    nums = []
    assert threeSum(nums) == []

    nums = [0]
    assert threeSum(nums) == []

    nums = [0, 0, 0, 0]
    assert threeSum(nums) == [[0, 0, 0]]

    nums = [-1,0,1,2,-1,-4]
    assert threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]

    nums = [-2,0,1,1,2]
    assert threeSum(nums) == [[-2,0,2],[-2,1,1]]