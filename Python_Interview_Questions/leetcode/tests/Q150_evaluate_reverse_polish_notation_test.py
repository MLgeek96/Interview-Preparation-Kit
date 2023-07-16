import pytest
from leetcode.problem_sets.Q150_evaluate_reverse_polish_notation import evalRPN

print(evalRPN.__doc__)

def test_evalRPN():
    tokens = ["2","1","+","3","*"]
    assert evalRPN(tokens) == 9

    tokens = ["4","13","5","/","+"]
    assert evalRPN(tokens) == 6

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    assert evalRPN(tokens) == 22

    tokens = ["18"]
    assert evalRPN(tokens) == 18