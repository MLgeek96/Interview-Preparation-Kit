import pytest
from leetcode.problem_sets.Q162_find_peak_element import findPeakElement

print(findPeakElement.__doc__)

def test_findPeakElement():
    nums = [1,2,3,1]
    assert findPeakElement(nums) == 2

    nums = [1,2,1,3,5,6,4]
    assert findPeakElement(nums) == 5

    nums = [1,2]
    assert findPeakElement(nums) == 1