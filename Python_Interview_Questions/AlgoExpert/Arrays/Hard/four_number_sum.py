from typing import List

def fourNumberSum(array: List[int], targetSum: int):
    """
    Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
    The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these quadruplets in no particular order.

    If no four numbers sum up to the target sum, the function should return an empty array.

    Sample Input:
    ```
    array = [7, 6, 4, -1, 1, 2]
    targetSum = 16
    ```

    Sample Output:
    ```
    [[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently
    ```

    Hints:
    1. Using four four loops to calculate the sums of all possible quadruplets in the array would generate an algorithm that runs in O(n^4) time, where n is the length of the input array. Can you come up with something faster using fewer for loops?
    2. You can calculate the sums of every pair of numbers in the array in O(n^2) time using just two four loops. Then, assuming that you've stored all of these sums in a hash table, you can fairly easility find which two sums can be paired to add up to the target sum: the numbers summing up to these two sums constitute candidates for valid quadruplets; you just have to make sure that no number was used to generate both of the two sums.
    3. You can do everything described in Hint #2 with just two sibling for loops nested inside a third for loop. Your goal is to create a hash table mapping the sums of every pair of numbers in the array to an array of arrays, with each subarray representing the indices of each pair summing up to that number. Loop through the input array with a simple for loop. Inside this loop, loop through the input array again, starting at the index of the first loop. At each iteration, calculate the difference between the target sum and the sum of the two numbers represented by the indices of the four loops. If that difference is in the hash table that you're building, then valid quadruplets can be formed by combining the current pair of numbers with each pair stored in the hash table at the difference just calculated. Following this nested for loop, loop through the array again, this time starting at index 0 all the way to the index of the first for loop. At each iteration, calculate the sum of the two numbers represented by indices of teh for loops and add it to the ahsh table if it isn't already there; then add the pair of indices to the array that the sum in the hash table maps to.

    Optimal Space & Time Complexity
    Average: O(n^2) time | O(n^2) space - where n is the length of the input array 
    Worst: O(n^3) time | O(n^2) soace - where n is the length of the input array 
    """
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum 
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets

if __name__ == "__main__":
    array = [7, 6, 4, -1, 1, 2]
    targetSum = 16
    assert fourNumberSum(array, targetSum) == [[7, 6, 4, -1], [7, 6, 1, 2]]

    array = [1, 2, 3, 4, 5, 6, 7]
    targetSum = 10
    assert fourNumberSum(array, targetSum) == [[1, 2, 3, 4]]

    array = [5, -5, -2, 2, 3, -3]
    targetSum = 0
    assert fourNumberSum(array, targetSum) == [[5, -5, -2, 2], [5, -5, 3, -3], [-2, 2, 3, -3]]

    array = [-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    targetSum = 4
    assert fourNumberSum(array, targetSum) == [[-2, -1, 1, 6],  [-2, 1, 2, 3],  [-2, -1, 2, 5],  [-2, -1, 3, 4]]

    array = [-1, 22, 18, 4, 7, 11, 2, -5, -3]
    targetSum = 30
    assert fourNumberSum(array, targetSum) == [[-1, 22, 7, 2],  [22, 4, 7, -3],  [-1, 18, 11, 2],  [18, 4, 11, -3],  [22, 11, 2, -5]]

    array = [-10, -3, -5, 2, 15, -7, 28, -6, 12, 8, 11, 5]
    targetSum = 20
    assert fourNumberSum(array, targetSum) == [[-5, 2, 15, 8],  [-3, 2, -7, 28],  [-10, -3, 28, 5],  [-10, 28, -6, 8],  [-7, 28, -6, 5],  [-5, 2, 12, 11],  [-5, 12, 8, 5]]

    array = [1, 2, 3, 4, 5]
    targetSum = 100
    assert fourNumberSum(array, targetSum) ==[]

    array = [1, 2, 3, 4, 5, -5, 6, -6]
    targetSum = 5
    assert fourNumberSum(array, targetSum) == [[2, 3, 5, -5],  [1, 4, 5, -5],  [2, 4, 5, -6],  [1, 3, -5, 6],  [2, 3, 6, -6],  [1, 4, 6, -6]]