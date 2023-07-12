from tkinter import N
import pytest
from leetcode.problem_sets.Q55_jump_game import canJump

print(canJump.__doc__)

def test_canJump():
    nums = [2,3,1,1,4]
    assert canJump(nums) == True

    nums = [3,2,1,0,4]
    assert canJump(nums) == False