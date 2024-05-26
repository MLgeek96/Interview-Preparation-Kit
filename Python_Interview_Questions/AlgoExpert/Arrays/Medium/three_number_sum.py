from typing import List

def threeNumberSum(array: List[int], targetSum: int):
    """
    Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

    If no three numbers sum up to the target sum, the function should return an empty array.

    Sample Input:
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0

    Sample Output:
    [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

    Optimal Space & Time Complexity:
    O(n^2) time | O(n) space - where n is the length of the input array
    """
    # O(n^2) time | O(n) space 
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            else:
                right -= 1
    return triplets

if __name__ == "__main__":
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0
    assert threeNumberSum(array, targetSum) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

    array = [1, 2, 3]
    targetSum = 6
    assert threeNumberSum(array, targetSum) == [[1, 2, 3]]

    array = [1, 2, 3]
    targetSum = 7
    assert threeNumberSum(array, targetSum) == []

    array = [8, 10, -2, 49, 14]
    targetSum = 57
    assert threeNumberSum(array, targetSum) == [[-2, 10, 49]]

    array = [12, 3, 1, 2, -6, 5, 0, -8, -1]
    targetSum = 0
    assert threeNumberSum(array, targetSum) == [[-8, 3, 5], [-6, 1, 5], [-1, 0, 1]]

    array = [12, 3, 1, 2, -6, 5, 0, -8, -1, 6]
    targetSum = 0
    assert threeNumberSum(array, targetSum) == [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-1, 0, 1]]

    array = [12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5]
    targetSum = 0
    assert threeNumberSum(array, targetSum) == [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-5, -1, 6], [-5, 0, 5], [-5, 2, 3], [-1, 0, 1]]

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
    targetSum = 18
    assert threeNumberSum(array, targetSum) == [[1, 2, 15], [1, 8, 9], [2, 7, 9], [3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]]

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
    targetSum = 32
    assert threeNumberSum(array, targetSum) == [[8, 9, 15]]

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
    targetSum = 33
    assert threeNumberSum(array, targetSum) == []

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
    targetSum = 5
    assert threeNumberSum(array, targetSum) == []