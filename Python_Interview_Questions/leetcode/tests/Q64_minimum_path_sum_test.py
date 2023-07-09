import pytest
from leetcode.problem_sets.Q64_minimum_path_sum import minPathSum

print(minPathSum.__doc__)

def test_minPathSum():
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    assert minPathSum(grid) == 7

    grid = [[1,2,3],[4,5,6]]
    assert minPathSum(grid) == 12