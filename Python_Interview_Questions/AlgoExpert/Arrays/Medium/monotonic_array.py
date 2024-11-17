from typing import List

def isMonotonic(array: List[int]):
    """
    Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

    An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

    Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

    Note that empty arrays and arrays of one element are monotonic.

    Sample Input:
    ```
    array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    ```

    Sample Output:
    ```
    true
    ```

    Hints:
    1. You can solve this question by iterating through the input array from left to right once.
    2. Try iterating through the input array from left to right, in search of two adjacent integers that can indicate whether the array is trending upward or downward. Once you've found the tentative trend of the array, at each element thereafter, compare the element to the previous one; if this comparison breaks the previously identivied trend, the array isn't monotonic.
    3. Alternatively, you can start by assuming that the array is both entirely non-decreasing and entirely non-increasing. As you iterate through each element, perform a check to see if you can invalidate one or both of your assumptions.

    Optimal Space & Time Complexity
    O(n) time | O(1) space - where n is the length of the array
    """
    # O(n) time | O(1) space - where n is the length of the array
    if len(array) <= 2:
        return True 
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue 
        if breaksDirection(direction, array[i - 1], array[i]):
            return False 
    return True 

    def breaksDirection(direction, previousInt, currentInt):
        difference = currentInt - previousInt
        if direction > 0:
            return difference < 0
        return difference > 0

    # O(n) time | O(1) space - where n is the length of the array
    isNonDecreasing = isNonIncreasing = True 
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False 
        if array[i] > array[i - 1]:
            isNonIncreasing = False 
    return isNonDecreasing or isNonIncreasing

if __name__ == "__main__":
    array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    assert isMonotonic(array) is True

    array = []
    assert isMonotonic(array) is True

    array = [1]
    assert isMonotonic(array) is True

    array = [1, 2]
    assert isMonotonic(array) is True

    array = [2, 1]
    assert isMonotonic(array) is True

    array = [1, 5, 10, 1100, 1101, 1102, 9001]
    assert isMonotonic(array) is True

    array = [-1, -5, -10, -1100, -1101, -1102, -9001]
    assert isMonotonic(array) is True

    array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
    assert isMonotonic(array) is False

    array = [1, 2, 0]
    assert isMonotonic(array) is False

    array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]
    assert isMonotonic(array) is False

    array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
    assert isMonotonic(array) is True

    array = [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11]
    assert isMonotonic(array) is False

    array = [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]
    assert isMonotonic(array) is True

    array = [-1, -1, -1, -1, -1, -1, -1, -1]
    assert isMonotonic(array) is True

    array = [1, 2, -1, -2, -5]
    assert isMonotonic(array) is False

    array = [-1, -5, 10]
    assert isMonotonic(array) is False

    array = [2, 2, 2, 1, 4, 5]
    assert isMonotonic(array) is False

    array = [1, 1, 1, 2, 3, 4, 1]
    assert isMonotonic(array) is False

    array = [1, 2, 3, 3, 2, 1]
    assert isMonotonic(array) is False