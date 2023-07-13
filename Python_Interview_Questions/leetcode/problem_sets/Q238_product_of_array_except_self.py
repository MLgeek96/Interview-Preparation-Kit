from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
    
    Constraints:
    • 2 <= nums.length <= 10 ** 5
    • -30 <= nums[i] <= 30
    • The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    """
    assert 2 <= len(nums) <= 10 ** 5
    for num in nums:
        assert -30 <= num <= 30
        
    leftArray = [1] * len(nums)
    rightArray = [1] * len(nums)

    for i in range(1, len(nums)):
        leftArray[i] = leftArray[i - 1] * nums[i - 1]
        j = len(nums) - i - 1
        rightArray[j] = rightArray[j + 1] * nums[j + 1]            

    return [x*y for x, y in zip(leftArray, rightArray)]