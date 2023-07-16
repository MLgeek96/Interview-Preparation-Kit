import pytest
from leetcode.problem_sets.Q77_combinations import combine

print(combine.__doc__)

def test_combine():
    n = 4
    k = 2
    assert combine(n, k) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    n = 1
    k = 1
    assert combine(n, k) == [[1]]