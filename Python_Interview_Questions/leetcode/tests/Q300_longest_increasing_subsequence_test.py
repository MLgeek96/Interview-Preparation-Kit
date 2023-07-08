import pytest
from leetcode.problem_sets.Q300_longest_increasing_subsequence import lengthOfLIS

print(lengthOfLIS.__doc__)

def test_lengthOfLIS():
    nums = [10,9,2,5,3,7,101,18]
    assert lengthOfLIS(nums) == 4
    
    nums = [0,1,0,3,2,3]
    assert lengthOfLIS(nums) == 4

    nums = [7,7,7,7,7,7,7]
    assert lengthOfLIS(nums) == 1