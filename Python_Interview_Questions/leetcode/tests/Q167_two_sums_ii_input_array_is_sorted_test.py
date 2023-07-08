import pytest
from leetcode.problem_sets.Q167_two_sums_ii_input_array_is_sorted import twoSum

print(twoSum.__doc__)

def test_twoSum():
    numbers = [2,7,11,15]
    target = 9
    assert twoSum(numbers, target) == [1, 2]

    numbers = [2,3,4]
    target = 6
    assert twoSum(numbers, target) == [1, 3]

    numbers = [-1,0]
    target = -1
    assert twoSum(numbers, target) == [1,2]