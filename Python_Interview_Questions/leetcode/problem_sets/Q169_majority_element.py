from typing import List

def majorityElement(nums: List[int]) -> int:
    """
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    Example 1:
    Input: nums = [3,2,3]
    Output: 3

    Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
    
    Constraints:
    • n == nums.length
    • 1 <= n <= 5 * 10 ** 4
    • -10 ** 9 <= nums[i] <= 10 ** 9   
    """
    assert 1 <= len(nums) <= 5 * 10 ** 4
    for num in nums:
        assert -10 ** 9 <= num <= 10 ** 9
        
    ## Moore Voting Algorithm
    # count = 0
    # candidate = 0
    
    # for num in nums:
    #     if count == 0:
    #         candidate = num
        
    #     if num == candidate:
    #         count += 1
    #     else:
    #         count -= 1
    
    # return candidate

    numDict = {}
    for num in nums:
        if num not in numDict:
            numDict[num] = 0
        numDict[num] += 1
        if numDict[num] > len(nums) // 2:
            return num