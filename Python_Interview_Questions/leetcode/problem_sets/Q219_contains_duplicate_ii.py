from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

    Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

    Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

    Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
    
    Constraints:
    • 1 <= nums.length <= 10 ** 5
    • -10 ** 9 <= nums[i] <= 10 ** 9
    • 0 <= k <= 10 ** 5
    """
    assert 1 <= len(nums) <= 10 ** 5, "Length of nums must be between 1 and 10 ** 5"
    for num in nums:
        assert -10 ** 9 <= num <= 10 ** 9, "Number in nums must be between -10 ** 9 and 10 ** 9"
    assert 0 <= k <= 10 ** 5, "k must be between 0 and 10 ** 5"
    
    numsIdx = {}
    for idx, num in enumerate(nums):
        if num in numsIdx and abs(idx - numsIdx[num]) <= k:
            return True
        numsIdx[num] = idx
    return False