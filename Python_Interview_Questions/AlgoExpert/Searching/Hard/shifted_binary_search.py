from typing import List

def shiftedBinarySearch(array, target):
    """
    Write a function that takes in a sorted array of distinct integers as well as a target integer. The caveat is that the integers in the array have ben shifted by some amount; in other words, they've been moved to the left or to the right by one or more positions. For example, [1, 2, 3, 4] might have turned into [3, 4, 1, 2].

    The function should use a variation of the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.

    If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of the Binary Search question's video explanation before starting to code.

    Sample Input:
    ```
    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 33
    ```

    Sample Output:
    ```
    8
    ```

    Hints:
    1. The Binary Search algorithm involves a left pointer and a right pointer and using those pointers to find the middle number in an array. Unlike with a normal sorted array however, you cannot simply find the middle number of the array and compare it to the target here, because the shift could lead you in the wrong direction. Instead, realize that whenever you find the middle number in the array, the following two scenarios are possible (assuming the middle number is not equal to the target number, in which case you're done); either the left-pointer number is smaller than or equal to the middle number, or it is bigger. Figure out a way to eliminate half of the array depending on the scenario.
    2. In the scenario where the left-pointer number is smaller thatn or equal to the middle number, two other scenarios can arise: either the target number is smaller than the middle number and greater than or equal to the left-pointer number, or it's not. In the first scenario, the right half of the array can be eliminated; in the second scenario, the left half can be eliminated. Figure out the scenarios that can arise if the left-pointer number is greater than the middle number and apply whatever logic you come up with recursively until you find the target number or until you run out of numbers in the array.
    3. Can you implement this algorithm iteratively? Are there any disadvantages to doing so?

    Optimal Space & Time Complexity
    O(log(n)) time | O(1) space - where n is the length of the input array
    """
    # O(log(n)) time | O(1) space - where n is the length of the input array
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

    def shiftedBinarySearchHelper(array, target, left, right):
        if left > right:
            return -1 
        middle = (left + right) // 2
        potentialMatch = array[middle]
        leftNum = array[left]
        rightNum = array[right]

        if target == potentialMatch:
            return middle 
        elif leftNum <= potentialMatch:
            if target < potentialMatch and target >= leftNum:
                return shiftedBinarySearchHelper(array, target, left, middle - 1)
            else:
                return shiftedBinarySearchHelper(array, target, middle + 1, right)
        else:
            if target > potentialMatch and target <= rightNum:
                return shiftedBinarySearchHelper(array, target, middle + 1, right)
            else:
                return shiftedBinarySearchHelper(array, target, left, middle - 1)

    # O(log(n)) time | O(1) space - where n is the length of the input array
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

    def shiftedBinarySearchHelper(array, target, left, right):
        while left <= right:
            middle = (left + right) // 2
            potentialMatch = array[middle]
            leftNum = array[left]
            rightNum = array[right]
            if target == potentialMatch:
                return middle 
            elif leftNum <= potentialMatch:
                if target < potentialMatch and target >= leftNum:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if target > potentialMatch and target <= rightNum:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1

if __name__ == "__main__":
    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 33
    assert shiftedBinarySearch(array, target) == 8

    array = [5, 23, 111, 1]
    target = 111
    assert shiftedBinarySearch(array, target) == 2

    array = [111, 1, 5, 23]
    target = 5
    assert shiftedBinarySearch(array, target) == 2

    array = [23, 111, 1, 5]
    target = 35
    assert shiftedBinarySearch(array, target) == -1

    array = [61, 71, 72, 73, 0, 1, 21, 33, 37, 45]
    target = 33
    assert shiftedBinarySearch(array, target) == 7

    array = [72, 73, 0, 1, 21, 33, 37, 45, 61, 71]
    target = 72
    assert shiftedBinarySearch(array, target) == 0

    array = [71, 72, 73, 0, 1, 21, 33, 37, 45, 61]
    target = 73
    assert shiftedBinarySearch(array, target) == 2

    array = [73, 0, 1, 21, 33, 37, 45, 61, 71, 72]
    target = 70
    assert shiftedBinarySearch(array, target) == -1

    array = [33, 37, 45, 61, 71, 72, 73, 355, 0, 1, 21]
    target = 355
    assert shiftedBinarySearch(array, target) == 7

    array = [33, 37, 45, 61, 71, 72, 73, 355, 0, 1, 21]
    target = 354
    assert shiftedBinarySearch(array, target) == -1

    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 45
    assert shiftedBinarySearch(array, target) == 0

    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 61
    assert shiftedBinarySearch(array, target) == 1

    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 71
    assert shiftedBinarySearch(array, target) == 2

    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 72
    assert shiftedBinarySearch(array, target) == 3

    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 73
    assert shiftedBinarySearch(array, target) == 4

    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 0
    assert shiftedBinarySearch(array, target) == 5

    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 1
    assert shiftedBinarySearch(array, target) == 6

    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 21
    assert shiftedBinarySearch(array, target) == 7

    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 37
    assert shiftedBinarySearch(array, target) == 9

    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 38
    assert shiftedBinarySearch(array, target) == -1

    array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 0
    assert shiftedBinarySearch(array, target) == 0

    array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 1
    assert shiftedBinarySearch(array, target) == 1

    array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 21
    assert shiftedBinarySearch(array, target) == 2

    array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 33
    assert shiftedBinarySearch(array, target) == 3

    array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 37
    assert shiftedBinarySearch(array, target) == 4

    array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 45
    assert shiftedBinarySearch(array, target) == 5

    array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 61
    assert shiftedBinarySearch(array, target) == 6

    array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 71
    assert shiftedBinarySearch(array, target) == 7

    array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 72
    assert shiftedBinarySearch(array, target) == 8

    array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 73
    assert shiftedBinarySearch(array, target) == 9

    array = [0, 1, 21, 33, 37, 45, 61, 71, 72, 73]
    target = 38
    assert shiftedBinarySearch(array, target) == -1