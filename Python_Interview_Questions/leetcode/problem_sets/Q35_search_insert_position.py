from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    """
    Given a sorted array of distinct integers and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.

    Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

    Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

    Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

    Example 4:
    Input: nums = [1,3,5,6], target = 0
    Output: 0

    Example 5:
    Input: nums = [1], target = 0
    Output: 0

    Constraints:
    • 1 <= nums.length <= 10 ** 4
    • -10 ** 4 <= nums[i] <= 10 ** 4
    • nums contains distinct values sorted in ascending order.
    • -10 ** 4 <= target <= 10 ** 4
    """
    assert 1 <= len(nums) <= 10 ** 4, "Length of nums must be between 1 and 10 ** 4"
    for num in nums:
        assert -10 ** 4 <= num <= 10 ** 4, "Integer in nums must be between -10 ** 4 and 10 ** 4"
    assert nums == nums.sort() and len(set(nums)) == len(nums), "Nums should contain distinct values sorted in ascending order"
    assert -10 ** 4 <= target <= 10 ** 4, "Target must be between -10 ** 4 and 10 ** 4"

    if target < min(nums):
        return 0
    elif target > max(nums):
        return len(nums)
    else:
        for index, num in enumerate(nums):
            if num == target:
                return index
            elif nums[index] < target < nums[index + 1]:
                return index + 1
