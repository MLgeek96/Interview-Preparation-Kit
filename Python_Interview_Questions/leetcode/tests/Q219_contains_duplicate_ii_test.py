import pytest
from leetcode.problem_sets.Q219_contains_duplicate_ii import containsNearbyDuplicate

print(containsNearbyDuplicate.__doc__)

def test_containsNearbyDuplicate():
    nums = [1,2,3,1]
    k = 3
    assert containsNearbyDuplicate(nums, k) == True

    nums = [1,0,1,1]
    k = 1
    assert containsNearbyDuplicate(nums, k) == True

    nums = [1,2,3,1,2,3]
    k = 2
    assert containsNearbyDuplicate(nums, k) == False