import pytest
from leetcode.problem_sets.Q274_h_index import hIndex

print(hIndex.__doc__)

def test_hIndex():
    citations = [3,0,6,1,5]
    assert hIndex(citations) == 3

    citations = [1,3,1]
    assert hIndex(citations) == 1

    citations = [0]
    assert hIndex(citations) == 0

    citations = [100]
    assert hIndex(citations) == 1