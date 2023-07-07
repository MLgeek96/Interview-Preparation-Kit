import pytest
from leetcode.problem_sets.Q209_minimum_size_subarray_sum import minSubArrayLen

print(minSubArrayLen.__doc__)

def test_minSubArrayLen():
    target = 7
    nums = [2,3,1,2,4,3]

    assert minSubArrayLen(target, nums) == 2

    target = 4
    nums = [1,4,4]

    assert minSubArrayLen(target, nums) == 1

    target = 11 
    nums = [1,1,1,1,1,1,1,1]

    assert minSubArrayLen(target, nums) == 0
