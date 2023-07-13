import pytest
from leetcode.problem_sets.Q238_product_of_array_except_self import productExceptSelf

def test_productExceptSelf():
    nums = [1,2,3,4]
    assert productExceptSelf(nums) == [24,12,8,6]

    nums = [-1,1,0,-3,3]
    assert productExceptSelf(nums) == [0,0,9,0,0]