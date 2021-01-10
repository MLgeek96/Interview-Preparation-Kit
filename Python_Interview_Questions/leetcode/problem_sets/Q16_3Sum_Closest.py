from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    """
    Given an array nums of n integers and an integer target,
    find three integers in nums such that the sum is closest to target.
    Return the sum of the three integers.
    You may assume that each input would have exactly one solution.

    Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

    Constraints:
    • 3 <= nums.length <= 10^3
    • -10^3 <= nums[i] <= 10^3
    • -10^4 <= target <= 10^4

    """
    assert 3 <= len(nums) <= 10 ** 3, "Length of list must be strictly between 3 and 1, 000"
    for i in nums:
        assert -10 ** 3 <= i <= 10 ** 3, "All integers must be between -1,000 and 1,000"
    assert -10 ** 4 <= target <= 10 ** 4, "Target must be between -1,000 and 1000"

    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left_pointer = i + 1
        right_pointer = len(nums) - 1
        while left_pointer < right_pointer:
            total = nums[i] + nums[left_pointer] + nums[right_pointer]
            if total == target:
                return total
            elif total > target:
                right_pointer -= 1
            else:
                left_pointer += 1
            difference_from_target = abs(target - total)
            if difference_from_target < closest_sum:
                closest_sum = difference_from_target
                ans = total

    return ans
