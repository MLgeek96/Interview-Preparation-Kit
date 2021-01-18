import pytest
from leetcode.problem_sets.Q7_reverse_integer import reverse

def test_reverse():
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(120) == 21
    assert reverse(0) == 0

