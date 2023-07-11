import pytest
from leetcode.problem_sets.Q149_max_points_on_a_line import maxPoints

print(maxPoints.__doc__)

def test_maxPoints():
    points = [[1,1],[2,2],[3,3]]
    assert maxPoints(points) == 3

    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    assert maxPoints(points) == 4