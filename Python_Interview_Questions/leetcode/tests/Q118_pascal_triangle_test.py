import pytest
from leetcode.problem_sets.Q118_pascal_triangle import generate

print(generate.__doc__)

def test_pascal_triangle():
    assert generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]