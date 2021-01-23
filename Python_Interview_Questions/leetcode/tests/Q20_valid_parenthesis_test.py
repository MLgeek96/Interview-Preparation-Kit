import pytest
from leetcode.problem_sets.Q20_valid_parenthesis import isValid

def test_valid_parenthesis():
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("(]") == False
    assert isValid("([)]") == False
    assert isValid("{[]}") == True