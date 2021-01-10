from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

    Notice that the solution set must not contain duplicate triplets.

    Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Example 2:
    Input: nums = []
    Output: []

    Example 3:
    Input: nums = [0]
    Output: []

    Constraints:
    • 0 <= nums.length <= 3000
    • -105 <= nums[i] <= 105

    """

    assert 0 <= len(nums) <= 3000, "Length of integer list must be strictly between 0 and 3000"
    for i in nums:
        assert -105 <= i <= 105, "All integers in the list must be between -105 and 105"

    if len(nums) < 3:
        return []

    nums.sort()
    nums_length = len(nums)
    ans = []

    for i in range(nums_length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left_pointer = i + 1
        right_pointer = nums_length - 1
        while left_pointer < right_pointer:
            sum = nums[i] + nums[left_pointer] + nums[right_pointer]
            if sum == 0:
                ans.append([nums[i], nums[left_pointer], nums[right_pointer]])
                left_pointer += 1
                right_pointer -= 1
                while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                    left_pointer += 1
                while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer + 1]:
                    right_pointer -= 1
            elif sum > 0:
                right_pointer -= 1
            else:
                left_pointer += 1

    return ans

