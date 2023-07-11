import pytest
from leetcode.problem_sets.Q128_longest_consecutive_sequence import longestConsecutive

print(longestConsecutive.__doc__)

def test_longestConsecutive():
    nums = [100,4,200,1,3,2]
    assert longestConsecutive(nums) == 4

    nums = [0,3,7,2,5,8,4,6,0,1]
    assert longestConsecutive(nums) == 9