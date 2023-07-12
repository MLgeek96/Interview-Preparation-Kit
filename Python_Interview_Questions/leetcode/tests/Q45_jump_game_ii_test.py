import pytest
from leetcode.problem_sets.Q45_jump_game_ii import jump

print(jump.__doc__)

def test_jump():
    nums = [2,3,1,1,4]
    assert jump(nums) == 2

    nums = [2,3,0,1,4]
    assert jump(nums) == 2