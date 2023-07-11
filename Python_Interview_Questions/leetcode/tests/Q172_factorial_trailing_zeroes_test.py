import pytest
from leetcode.problem_sets.Q172_factorial_trailing_zeroes import trailingZeroes

print(trailingZeroes.__doc__)

def test_trailingZeroes():
    n = 3
    assert trailingZeroes(n) == 0

    n = 5
    assert trailingZeroes(n) == 1

    n = 0
    assert trailingZeroes(n) == 0