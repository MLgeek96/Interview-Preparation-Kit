from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    """
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

    Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

    Example 3:
    Input: nums = [1]
    Output: [[1]]
    
    Constraints:
    • 1 <= nums.length <= 6
    • -10 <= nums[i] <= 10
    • All the integers of nums are unique.
    """
    assert 1 <= len(nums) <= 6
    for num in nums:
        assert -10 <= num <= 10
    assert len(nums) == len(set(nums))
    
    resultList = []
    visited = set()

    def backtrack(visitedSet, permutation):
        if len(permutation) == len(nums):
            resultList.append(permutation.copy())
            
        for i in range(len(nums)):
            if i not in visited:
                visitedSet.add(i)
                backtrack(visitedSet, permutation + [nums[i]])
                visitedSet.remove(i)

    backtrack(visited, [])
    return resultList

