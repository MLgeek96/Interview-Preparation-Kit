import pytest
from leetcode.problem_sets.Q71_simplify_path import simplifyPath

print(simplifyPath.__doc__)

def test_simplifyPath():
    path = "/home/"
    assert simplifyPath(path) == "/home"

    path = "/../"
    assert simplifyPath(path) == "/"

    path = "/home//foo/"
    assert simplifyPath(path) == "/home/foo"