from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

    Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

    Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation: 
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
    
    Constraints:
    • 1 <= nums.length <= 10 ** 5
    • -2 ** 31 <= nums[i] <= 2 ** 31 - 1
    • 0 <= k <= 10 ** 5

    Follow up:
    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?    
    """
    assert 1 <= len(nums) <= 10 ** 5
    for num in nums:
        assert -2 ** 31 <= num <= 2 ** 31 - 1
    assert 0 <= k <= 10 ** 5

    # while k > 0:
    #     temp = nums.pop()
    #     nums.insert(0, temp)
    #     k -= 1
    # if len(nums) <= 1:
    #     return nums
    # k = k % len(nums)
    # if k == 0:
    #     return nums
    # nums[:k], nums[k:] = nums[-k:], nums[:-k]
    # return nums
    n = len(nums)
    k = k % n
    nums[:n-k] = nums[:n-k][::-1]
    nums[n-k:] = nums[n-k:][::-1]
    nums[:] = nums[::-1]
    return nums
    