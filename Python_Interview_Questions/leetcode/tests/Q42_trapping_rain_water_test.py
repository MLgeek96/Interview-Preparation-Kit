import pytest
from leetcode.problem_sets.Q42_trapping_rain_water import trap

def test_trapping_rain_water():
    height = [4, 2, 0, 3, 2, 5]
    assert trap(height) == 9

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert trap(height) == 6

    height = []
    assert trap(height) == 0

