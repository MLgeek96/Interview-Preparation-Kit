import pytest
from leetcode.problem_sets.Q46_permutations import permute

print(permute.__doc__)

def test_permute():
    nums = [1,2,3]
    assert permute(nums) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    nums = [0,1]
    assert permute(nums) == [[0,1],[1,0]]

    nums = [1]
    assert permute(nums) == [[1]]