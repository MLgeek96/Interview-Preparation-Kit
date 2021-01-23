import pytest
from leetcode.problem_sets.Q53_maximum_subarray import maxSubArray

print(maxSubArray.__doc__)

def test_maximum_subarray():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    assert maxSubArray(nums) == 6

    nums = [1]
    assert maxSubArray(nums) == 1

    nums = [0]
    assert maxSubArray(nums) == 0

    nums = [-1]
    assert maxSubArray(nums) == -1

    nums = [-100000]
    assert maxSubArray(nums) == -100000