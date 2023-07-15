import pytest
from leetcode.problem_sets.Q57_insert_intervals import insert

print(insert.__doc__)

def test_insert():
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    assert insert(intervals, newInterval) == [[1,5],[6,9]]

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    assert insert(intervals, newInterval) == [[1,2],[3,10],[12,16]]

    intervals = []
    newInterval = [5,7]
    assert insert(intervals, newInterval) == [[5,7]]

    intervals = [[1,5]]
    newInterval = [0,3]
    assert insert(intervals, newInterval) == [[0,5]]

    intervals = [[1,5]]
    newInterval = [0,0]
    assert insert(intervals, newInterval) == [[0,0], [1,5]]

    intervals = [[3,5],[12,15]]
    newInterval = [6,6]
    assert insert(intervals, newInterval) == [[3,5],[6,6],[12,15]]

    intervals = [[0,2],[3,9]]
    newInterval = [6,8]
    assert insert(intervals, newInterval) == [[0,2],[3,9]]