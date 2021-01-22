import pytest
from leetcode.problem_sets.Q70_climbing_stairs import climbStairs

print(climbStairs.__doc__)

def test_climbing_stairs():
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
    assert climbStairs(1) == 1