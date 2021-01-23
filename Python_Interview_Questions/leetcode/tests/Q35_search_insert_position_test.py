import pytest
from leetcode.problem_sets.Q35_search_insert_position import searchInsert

def test_search_insert_position():
    nums = [1,3,5,6]
    target = 5
    assert searchInsert(nums, target) == 2

    nums = [1, 3, 5, 6]
    target = 2
    assert searchInsert(nums, target) == 1

    nums = [1, 3, 5, 6]
    target = 7
    assert searchInsert(nums, target) == 4

    nums = [1, 3, 5, 6]
    target = 0
    assert searchInsert(nums, target) == 0

    nums = [1]
    target = 0
    assert searchInsert(nums, target) == 0