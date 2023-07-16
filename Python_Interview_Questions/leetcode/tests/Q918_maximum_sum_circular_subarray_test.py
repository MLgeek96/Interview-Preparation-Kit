import pytest
from leetcode.problem_sets.Q918_maximum_sum_circular_subarray import maxSubarraySumCircular

print(maxSubarraySumCircular.__doc__)

def test_maxSubarraySumCircular():
    nums = [1,-2,3,-2]
    assert maxSubarraySumCircular(nums) == 3

    nums = [5,-3,5]
    assert maxSubarraySumCircular(nums) == 10

    nums = [-3,-2,-3]
    assert maxSubarraySumCircular(nums) == -2

    nums = [3,1,3,2,6]
    assert maxSubarraySumCircular(nums) == 15