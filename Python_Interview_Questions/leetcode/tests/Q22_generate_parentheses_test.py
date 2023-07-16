import pytest
from leetcode.problem_sets.Q22_generate_parentheses import generateParenthesis

print(generateParenthesis.__doc__)

def test_generateParenthesis():
    n = 3
    assert generateParenthesis(n) == ["((()))","(()())","(())()","()(())","()()()"]

    n = 1
    assert generateParenthesis(n) == ["()"]