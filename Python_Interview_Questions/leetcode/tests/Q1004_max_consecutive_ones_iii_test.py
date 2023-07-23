import pytest
from leetcode.problem_sets.Q1004_max_consecutive_ones_iii import longestOnes

print(longestOnes.__doc__)

def test_longestOnes():
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2

    assert longestOnes(nums, k) == 6

    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3

    assert longestOnes(nums, k) == 10