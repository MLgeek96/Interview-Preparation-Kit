import pytest
from leetcode.problem_sets.Q39_combination_sum import combinationSum

print(combinationSum.__doc__)

def test_combinationSum():
    candidates = [2,3,6,7]
    target = 7
    assert combinationSum(candidates, target) == [[2,2,3],[7]]

    candidates = [2,3,5]
    target = 8
    assert combinationSum(candidates, target) == [[2,2,2,2],[2,3,3],[3,5]]

    candidates = [2]
    target = 1
    assert combinationSum(candidates, target) == []