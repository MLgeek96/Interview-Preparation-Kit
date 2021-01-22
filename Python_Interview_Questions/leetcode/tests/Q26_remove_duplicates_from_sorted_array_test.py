import pytest
from leetcode.problem_sets.Q26_remove_duplicates_from_sorted_array import removeDuplicates

def test_remove_duplicates_from_sorted_array():
    assert removeDuplicates([1,1,2]) == 2
    assert removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
    assert removeDuplicates([1,1]) == 1