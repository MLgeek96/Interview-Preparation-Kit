import pytest
from leetcode.problem_sets.Q63_unique_paths_ii import uniquePathsWithObstacles

print(uniquePathsWithObstacles.__doc__)

def test_uniquePathsWithObstacles():
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    assert uniquePathsWithObstacles(obstacleGrid) == 2
    
    obstacleGrid = [[0,1],[0,0]]
    assert uniquePathsWithObstacles(obstacleGrid) == 1