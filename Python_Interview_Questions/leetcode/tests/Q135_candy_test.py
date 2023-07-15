import pytest
from leetcode.problem_sets.Q135_candy import candy

print(candy.__doc__)

def test_candy():
    ratings = [1,0,2]
    assert candy(ratings) == 5

    ratings = [1,2,2]
    assert candy(ratings) == 4