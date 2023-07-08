import pytest
from leetcode.problem_sets.Q120_triangle import minimumTotal

print(minimumTotal.__doc__)

def test_minimumTotal():
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    assert minimumTotal(triangle) == 11

    triangle = [[-10]]
    assert minimumTotal(triangle) == -10

    triangle = [[-10], [-2, 6]]
    assert minimumTotal(triangle) == -12