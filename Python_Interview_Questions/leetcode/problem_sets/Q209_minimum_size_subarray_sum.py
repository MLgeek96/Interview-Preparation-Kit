from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    """
    Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.

    Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1

    Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0

    Constraints:
    • 1 <= target <= 10 ** 9
    • 1 <= nums.length <= 105
    • 1 <= nums[i] <= 10 ** 4
    """
    assert 1 <= target <= 10 ** 9, "Target sum must be between 1 and 10 ** 9"
    assert 1 <= len(nums) <= 105, "Length of nums must be between 1 and 105"
    for num in nums:
        assert 1 <= num <= 10 ** 4, "Number in nums must be between 1 and 10 ** 4"

    minLength = float('inf')
    leftPointer = 0
    sums = 0
    for index in range(len(nums)):
        sums += nums[index]

        while sums >= target:
            minLength = min(minLength, index - leftPointer + 1)
            sums -= nums[leftPointer]
            leftPointer += 1

    return minLength if minLength != float('inf') else 0