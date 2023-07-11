import pytest
from leetcode.problem_sets.Q50_power_x_n import myPow

print(myPow.__doc__)

def test_myPow():
    x = 2.00000
    n = 10
    assert myPow(x, n) == 1024.00000

    # x = 2.10000
    # n = 3
    # assert myPow(x, n) == 9.26100

    x = 2.00000
    n = -2
    assert myPow(x, n) == 0.25