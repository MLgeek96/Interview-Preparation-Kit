import pytest 
import sys

from Leetcode_Problem_Set.Problem_Sets.Q1_two_sums import two_sums

def test_two_sums():
    nums = [3,2,4]
    target = 6

    ans = two_sums(nums, target)
    assert ans == [0, 1]