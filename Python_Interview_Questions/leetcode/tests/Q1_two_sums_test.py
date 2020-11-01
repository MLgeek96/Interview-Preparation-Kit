import pytest 
from leetcode.problem_sets.Q1_two_sums import two_sums

print(two_sums.__doc__)

def test_two_sums():
    nums = [2, 7, 11, 15]
    target = 9
    
    ans = two_sums(nums, target)
    assert ans == [0,1]

    nums = [3,2,4]
    target = 6

    ans = two_sums(nums, target)
    assert ans == [1,2]

    nums = [3,3]
    target = 6

    ans = two_sums(nums, target)
    assert ans == [0,1]

def test_bad_nums():
    nums = [2, 110]
    target = 112

    with pytest.raises(AssertionError):
        two_sums(nums, target)

    