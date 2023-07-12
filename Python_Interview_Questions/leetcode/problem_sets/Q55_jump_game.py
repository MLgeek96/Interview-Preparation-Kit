from typing import List

def canJump(nums: List[int]) -> bool:
    """
    You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.

    Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

    Constraints:
    • 1 <= nums.length <= 10 ** 4
    • 0 <= nums[i] <= 10 ** 5
    """
    assert 1 <= len(nums) <= 10 ** 4
    for num in nums:
        assert 0 <= num <= 10 ** 5

    # goal = len(nums) - 1
    # for i in reversed(range(len(nums))):
    #     if i + nums[i] >= goal:
    #         goal = i
    # return not goal

    # dp = [False] * len(nums)
    # dp[-1] = True

    # for i in reversed(range(0, len(nums) - 1)):
    #     dp[i] = any(dp[i:i + nums[i] + 1])
    # return dp[0] == True

    curr = nums[0]
    for i in range(1, len(nums)):
        if curr == 0:
            return False
        curr -= 1
        curr = max(curr, nums[i])
    return True

