import pytest
from leetcode.problem_sets.Q452_minimum_number_of_arrows_to_burst_ballon import findMinArrowShots

print(findMinArrowShots.__doc__)

def test_findMinArrowShots():
    points = [[10,16],[2,8],[1,6],[7,12]]
    assert findMinArrowShots(points) == 2

    points = [[1,2],[3,4],[5,6],[7,8]]
    assert findMinArrowShots(points) == 4

    points = [[1,2],[2,3],[3,4],[4,5]]
    assert findMinArrowShots(points) == 2

    points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    assert findMinArrowShots(points) == 2
    
    points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
    assert findMinArrowShots(points) == 2