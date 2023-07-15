import pytest
from leetcode.problem_sets.Q56_merge_intervals import merge

print(merge.__doc__)

def test_merge():
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    assert merge(intervals) == [[1,6],[8,10],[15,18]]

    intervals = [[1,4],[4,5]]
    assert merge(intervals) == [[1,5]]