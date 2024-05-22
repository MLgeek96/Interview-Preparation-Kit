from typing import List
def twoNumberSum(array: List[int], targetSum: int):
    """
    Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If
    any two numbers in the input array sum up to the target sum, the function should return them in an array, in any
    order. If no two numbers sum up to the target sum, the function should return an empty array.

    Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single
    integer to itself n order to obtain the target sum.

    You can assume that there will be at most one pair of numbers summing up to the target sum.

    Sample Input:
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10

    Sample Output:
    [-1, 11]

    Hints:
    1. Try using two for loops to sum all possible pairs of numbers in the input array. What are the time and space
    implications of this approach?

    2. Realize that for every number X in the input array, you are essentially trying to find a corresponding number Y
    such that X + Y = targetSum. With two variables in this equation known to you, it shouldn't be hard to solve for Y.

    3. Try storing every number in a hash table, solving the equation mentioned in Hint #2 for every number, and checking
    if the Y that you find is stored in the hash table. What are the time and space implications of this approach?

    Optimal Space & Time Complexity:
    O(n) time | O(n) space - where n is the length of the input array.
    """
    # O(n^2) time | O(n) space
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

    # O(n) time | O(n) space
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

    # O(nlogn) time | O(1) space
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1
    return []