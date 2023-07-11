import pytest
from leetcode.problem_sets.Q169_majority_element import majorityElement

print(majorityElement.__doc__)

def test_majorityElement():
    nums = [3,2,3]
    assert majorityElement(nums) == 3

    nums = [2,2,1,1,1,2,2]
    assert majorityElement(nums) == 2