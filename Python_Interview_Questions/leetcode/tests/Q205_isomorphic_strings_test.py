import pytest
from leetcode.problem_sets.Q205_isomorphic_strings import isIsomorphic

print(isIsomorphic.__doc__)

def test_isIsomorphic():
    s = "egg"
    t = "add"
    assert isIsomorphic(s, t) == True

    s = "foo"
    t = "bar"
    assert isIsomorphic(s, t) == False

    s = "paper"
    t = "title"
    assert isIsomorphic(s, t) == True