from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    """
    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

    Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

    Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1
    
    Constraints:
    • 1 <= nums.length <= 2500
    • -10 ** 4 <= nums[i] <= 10 ** 4
    """
    assert 1 <= len(nums) <= 2500, "Length of nums must be between 1 and 2500"
    for num in nums:
        assert -10 ** 4 <= num <= 10 ** 4, "Number in nums must be between -10 ** 4 and 10 ** 4"
    
    # dp = [1]* len(nums)
    # for i in range(1, len(nums)):
    #     for j in range(0,i):
    #         if nums[i] > nums[j]:
    #             dp[i] = max(dp[i], 1 + dp[j])
    # return max(dp)

    dp = [1 for _ in range(len(nums))]
    for i in reversed(range(len(nums))):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)