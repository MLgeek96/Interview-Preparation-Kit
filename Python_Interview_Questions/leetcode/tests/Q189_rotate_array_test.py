import pytest
from leetcode.problem_sets.Q189_rotate_array import rotate

print(rotate.__doc__)

def test_rotate():
    nums = [1,2,3,4,5,6,7]
    k = 3
    assert rotate(nums, k) == [5,6,7,1,2,3,4]

    nums = [-1,-100,3,99]
    k = 2
    assert rotate(nums, k) == [3,99,-1,-100]