from os import remove
import pytest
from leetcode.problem_sets.Q80_remove_duplicates_from_sorted_array_ii import removeDuplicates

print(removeDuplicates.__doc__)

def test_removeDuplicates():
    nums = [1,1,1,2,2,3]
    assert removeDuplicates(nums) == 5 

    nums = [0,0,1,1,1,1,2,3,3]
    assert removeDuplicates(nums) == 7