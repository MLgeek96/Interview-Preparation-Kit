from typing import List

def maxSubArray(nums: List[int]) -> int:
    """
    Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

    Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

    Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

    Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

    Constraints:
    • 1 <= nums.length <= 10 ** 5
    • -10 ** 4 <= nums[i] <= 10 ** 4

    Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
    """
    assert 1 <= len(nums) <= 10 ** 5
    for num in nums:
        assert -10 ** 4 <= num <= 10 ** 4

    # largestSum = -1e8
    # for i in range(len(nums)):
    #     currentSum = 0
    #     for j in range(i, len(nums)):
    #         currentSum += nums[j]
    #         largestSum = max(largestSum, currentSum)
    # return largestSum

    largestSum = nums[0]
    currentSum = nums[0]

    for num in nums[1:]:
        currentSum = max(num, currentSum + num)
        largestSum = max(largestSum, currentSum)

    return largestSum
