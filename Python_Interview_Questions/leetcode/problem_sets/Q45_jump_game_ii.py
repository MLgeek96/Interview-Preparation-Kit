from typing import List

def jump(nums: List[int]) -> int:
    """
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

    Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    • 0 <= j <= nums[i] and
    • i + j < n

    Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

    Example 1:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Example 2:
    Input: nums = [2,3,0,1,4]
    Output: 2

    Constraints:
    • 1 <= nums.length <= 10 ** 4
    • 0 <= nums[i] <= 1000
    • It's guaranteed that you can reach nums[n - 1].
    """
    assert 1 <= len(nums) <= 10 ** 4
    for num in nums:
        assert 0 <= num <= 1000

    # start, end, count = 0, 0, 0
    # for i in range(len(nums) - 1):
    #     start = max(start, i + nums[i])
    #     if end == i:
    #         end = start
    #         count += 1
    # return count

    dp = [float('inf')] * len(nums)
    dp[-1] = 0

    for i in reversed(range(len(nums))):
        target = dp[i + 1: i + nums[i] + 1]
        if len(target) > 0:
            dp[i] = min(dp[i], 1 + min(target))
    
    return dp[0]
