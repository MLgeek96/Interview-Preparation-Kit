from typing import List

def findPeakElement(nums: List[int]) -> int:
    """
    A peak element is an element that is strictly greater than its neighbors.

    Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

    You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

    You must write an algorithm that runs in O(log n) time.

    Example 1:
    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.

    Example 2:
    Input: nums = [1,2,1,3,5,6,4]
    Output: 5
    Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

    Constraints:
    • 1 <= nums.length <= 1000
    • -2 ** 31 <= nums[i] <= 2 ** 31 - 1
    • nums[i] != nums[i + 1] for all valid i.
    """
    assert 1 <= len(nums) <= 1000
    for num in nums:
        assert -2 ** 31 <= num <= 2 ** 31 - 1
    for i in range(1, len(nums)):
        assert nums[i] != nums[i + 1]

    leftPointer = 0
    rightPointer = len(nums) - 1

    while leftPointer <= rightPointer:
        midPointer = (leftPointer + rightPointer) // 2

        if (midPointer == 0 or nums[midPointer - 1] <= nums[midPointer]) and (midPointer == len(nums) - 1 or nums[midPointer] > nums[midPointer + 1]):
            return midPointer
        elif (midPointer > 0 and nums[midPointer - 1] > nums[midPointer]):
            rightPointer = midPointer - 1
        else:
            leftPointer = midPointer + 1