from typing import List

def subarraySort(array: List[int]):
    """
    Write a function that takes in an array of at least two integers and that returns an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted (in ascending order).

    If the input array is already sorted, the function should return [-1, -1]

    Sample Input:
    ```
    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    ```

    Sample Output:
    ```
    [3, 9]
    ```

    Hints:
    1. realise that even a single out-of-order number in the input array can call for a large subarray to have to be sorted. This is because, depending on how out-of-place the number is, it might need to be moved very far away from its original position in order to be in its sorted position.
    2. Find the smallest and largest numbers that are out of order in the input array. You should be able to do this in a single pass through the array.
    3. Once you've found the smallest and largest out-of-order numbers mentioned in Hint #2, find their final sorted positions in the array. This should give you the extremities of the smallest subarray that needs to be sorted.

    Optimal Space & Time Complexity
    O(n) time | O(1) space - where n is the length of the input array 
    """

    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if minOutOfOrder == float("inf"):
        return [-1, -1]
    subarrayLeftIdx = 0 
    while minOutOfOrder >= array[subarrayLeftIdx]:
        subarrayLeftIdx += 1
    subarrayRightIdx = len(array) - 1
    while maxOutOfOrder <= array[subarrayRightIdx]:
        subarrayRightIdx -= 1
    return [subarrayLeftIdx, subarrayRightIdx]

def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]

if __name__ == "__main__":
    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    assert subarraySort(array) == [3, 9]

    array = [1, 2]
    assert subarraySort(array) == [-1, -1]

    array = [2, 1]
    assert subarraySort(array) == [0, 1]

    array = [1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]
    assert subarraySort(array) == [4, 9]

    array = [1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]
    assert subarraySort(array) == [4, 6]

    array = [1, 2, 8, 4, 5]
    assert subarraySort(array) == [2, 4]

    array = [4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]
    assert subarraySort(array) == [0, 12]

    array = [4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]
    assert subarraySort(array) == [0, 11]

    array = [-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]
    assert subarraySort(array) == [1, 11]

    array = [-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]
    assert subarraySort(array) == [1, 12]

    array = [1, 2, 3, 4, 5, 6, 8, 7, 9, 10, 11]
    assert subarraySort(array) == [6, 7]

    array = [1, 2, 3, 4, 5, 6, 18, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19]
    assert subarraySort(array) == [6, 16]

    array = [1, 2, 3, 4, 5, 6, 18, 21, 22, 7, 14, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 4, 14, 11, 6, 33, 35, 41, 55]
    assert subarraySort(array) == [4, 24]

    array = [1, 2, 20, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert subarraySort(array) == [2, 19]

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2]
    assert subarraySort(array) == [2, 19]

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert subarraySort(array) == [-1, -1]

    array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert subarraySort(array) == [-1, -1]