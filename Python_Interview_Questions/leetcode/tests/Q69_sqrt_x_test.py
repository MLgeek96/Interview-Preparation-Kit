import pytest
from leetcode.problem_sets.Q69_sqrt_x import mySqrt

def test_sqrt_x():
    assert mySqrt(4) == 2
    assert mySqrt(8) == 2
    assert mySqrt(0) == 0
    assert mySqrt(1) == 1