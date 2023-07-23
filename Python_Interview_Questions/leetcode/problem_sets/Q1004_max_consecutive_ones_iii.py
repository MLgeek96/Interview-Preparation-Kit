from typing import List

def longestOnes(nums: List[int], k: int) -> int:
    """
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

    Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

    Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    
    Constraints:
    • 1 <= nums.length <= 10 ** 5
    • nums[i] is either 0 or 1.
    • 0 <= k <= nums.length
    """
    assert 1 <= len(nums) <= 10 ** 5
    for num in nums:
        assert num == 0 or num == 1
    assert 0 <= k <= len(nums)

    leftPointer = 0
    maxLength = 0

    for idx, num in enumerate(nums):
        k -= 1 - num
        if k < 0:
            k += 1 - nums[leftPointer]
            leftPointer += 1
        maxLength = max(maxLength, idx - leftPointer + 1)
    
    return maxLength