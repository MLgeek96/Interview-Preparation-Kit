from typing import List

def binarySearch(array: List[int], target: int):
    """
    Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.

    If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.

    Sample Input:
    ```
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    ```

    Sample Output:
    ```
    3
    ```

    Hints:
    1. The Binary Search algorithm works by finding the number in the middle of the input array and comparing it to the target number. Given that the array is sorted, if this middle number is smaller than the target number, and the entire left part of the array si no longer worth exploring since the target number can no longer be in it; similarly, if the middle number is greater than the target number, then the entire right part of the array is no longer worth exploring. Applying this logic recursively eliminates half of the array until the number is found or until the array runs out of numbers.
    2. Write a helper function that takes in two additional arguments: a left pointer and a right pointer representing the indices at the extremities of the array (or subarray) that you are applying Binary Search on. The first time this helper function is called, the left pointer should be zero and the right pointer should be the final index of the input array. To find the index of the middle number mentioned in Hint #1, simply round down the number obtained from: (left + right) / 2. Apply this logic recursively until you find the target number or until the left pointer becomes greater than the right pointer.
    3. Can you implement this algorithm iteratively? Are there any advantages to doing so?

    Optimal Space & Time Complexity
    O(log(n)) time | O(1) space - where n is the length of the input array
    """
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1 
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)

# O(log(n)) time | O(1) space - where n is the length of the input array
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle 
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1 
    return -1

if __name__ == "__main__":
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    assert binarySearch(array, target) == 3
    
    array = [1, 5, 23, 111]
    target = 111
    assert binarySearch(array, target) == 3

    array = [1, 5, 23, 111]
    target = 5
    assert binarySearch(array, target) == 1

    array = [1, 5, 23, 111]
    target = 35
    assert binarySearch(array, target) == -1
    
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 0
    assert binarySearch(array, target) == 0

    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 1
    assert binarySearch(array, target) == 1

    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 21
    assert binarySearch(array, target) == 2
    
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 45
    assert binarySearch(array, target) == 4

    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 61
    assert binarySearch(array, target) == 6

    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 71
    assert binarySearch(array, target) == 7
    
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 72 
    assert binarySearch(array, target) == 8

    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 73
    assert binarySearch(array, target) == 9

    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 70
    assert binarySearch(array, target) == -1
    
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355]
    target = 355
    assert binarySearch(array, target) == 10

    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355]
    target = 354
    assert binarySearch(array, target) == -1

    array = [1, 5, 23, 111]
    target = 120
    assert binarySearch(array, target) == -1

    array = [5, 23, 111]
    target = 3
    assert binarySearch(array, target) == -1