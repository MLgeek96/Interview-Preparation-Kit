from typing import List

def rob(nums: List[int]) -> int:
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

    Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

    Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.
    

    Constraints:
    • 1 <= nums.length <= 100
    • 0 <= nums[i] <= 400
    """
    assert 1 <= len(nums) <= 100, "Length of nums must be between 1 and 100"
    for num in nums:
        assert 0 <= num <= 400, "Number in nums must be between 0 and 400"

    for i in range(1, len(nums)):
        if i == 1:
            nums[i] = max(nums[i], nums[i-1])
        else:
            nums[i] = max(nums[i-1], nums[i]+nums[i-2])

    return nums[-1]