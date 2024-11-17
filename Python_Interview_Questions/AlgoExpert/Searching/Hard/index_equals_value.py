from typing import List

def indexEqualsValue(array: List[int]):
    """
    Write a function that takes in a sorted array of distinct integers and returns the first index in the array that is equal to the value at that index. In other words, your function should return the minimum index where index == array[index].

    If there is no such index, your function should return -1.

    Sample Input:
    ```
    array = [-5, -3, 0, 3, 4, 5, 9]
    ```

    Sample Output:
    ```
    3 // 3 == array[3]
    ```

    Hints:
    1. First think about a simple brute-force approach to solve this problem. What is the time complexity of this apprach and what improvements could be made to this time complexity?
    2. If the brute force solution runs in linear time complexity, then a better solution would have to run in O(log(n)) time. Which algorithm has an O(log(n)) time complexity?
    3. Implement a variation of binary search to solve this problem. Think about what conditions or checks must be added to search for the desired index-value pair.
    4. As you perform a variation of binary search on the input array, if the value that you're looking at is smaller than its index, cut the left half of the array from the search space, because all values to the left will be smaller than their corresponding indices; this is guaranteed to be true, since left indices will naturally decrement by 1 each and left valeus will decrement by at least 1 each due to the array being sorted. Similar logic applies to the right side of the array when the value that you're looking at is greater than its index.
    5. When you encounter a value that's equal to its index, you'll have to perform some additional logic to make sure that you're not potentially missing other values in the array that are equal to their index and that come before the value that you're looking at.

    Optimal Space & Time Complexity
    O(log(n)) time | O(1) space - where n is the length of the input array
    """
    # O(n) time | O(1) space - where n is the length of the input array 
    for index in range(len(array)):
        value = array[index]
        if index == value:
            return index 
    return -1 

    # O(log(n)) time | O(log(n)) space - where n is the length of the input array
    return indexEqualsValueHelper(array, 0, len(array) - 1)

    def indexEqualsValueHelper(array, leftIndex, rightIndex):
        if leftIndex > rightIndex:
            return -1 
            
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2
        middleValue = array[middleIndex]

        if middleValue < middleIndex:
            return indexEqualsValueHelper(array, middleIndex + 1, rightIndex)
        elif middleValue == middleIndex and middleIndex == 0:
            return middleIndex 
        elif middleValue == middleIndex and array[middleIndex - 1] < middleIndex - 1:
            return middleIndex 
        else:
            return indexEqualsValueHelper(array, leftIndex, middleIndex - 1)


    # O(log(n)) time | O(1) space - where n is the length of the input array
    leftIndex = 0 
    rightIndex = len(array) - 1

    while leftIndex <= rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2
        middleValue = array[middleIndex]

        if middleValue < middleIndex:
            leftIndex = middleIndex + 1
        elif middleValue == middleIndex and middleIndex == 0:
            return middleIndex
        elif middleValue == middleIndex and array[middleIndex - 1] < middleIndex - 1:
            return middleIndex
        else:
            rightIndex = middleIndex - 1

    return -1

if __name__ == "__main__":
    array = [-5, -3, 0, 3, 4, 5, 9]
    assert indexEqualsValue(array) == 3

    array = [-12, 1, 2, 3, 12]
    assert indexEqualsValue(array) == 1

    array = [-5, -4, -3, -2, -1, 0, 1, 3, 5, 6, 7, 11, 12, 14, 19, 20]
    assert indexEqualsValue(array) == 11

    array = [-3, -1, 1, 3, 5, 7, 9]
    assert indexEqualsValue(array) == 3

    array = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert indexEqualsValue(array) == -1

    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert indexEqualsValue(array) == 0

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert indexEqualsValue(array) == -1

    array = [0]
    assert indexEqualsValue(array) == 0

    array = [0, 1]
    assert indexEqualsValue(array) == 0

    array = [1, 2]
    assert indexEqualsValue(array) == -1

    array = [-50, 1, 2, 3, 4]
    assert indexEqualsValue(array) == 1

    array = [-40, -20, 0, 2, 4, 6, 8, 10]
    assert indexEqualsValue(array) == 4

    array = [-1000, 0, 1, 5000, 5001, 5002, 5005]
    assert indexEqualsValue(array) == -1

    array = [-1000, 0, 1, 2, 3, 4, 6, 5000, 5001, 5002, 5005]
    assert indexEqualsValue(array) == 6

    array = [-999, 0, 2, 500, 1000, 1500, 2000, 2500, 3000, 3500]
    assert indexEqualsValue(array) == 2

    array = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 18]
    assert indexEqualsValue(array) == 18

    array = []
    assert indexEqualsValue(array) == -1