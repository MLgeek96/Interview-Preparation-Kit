from typing import List


def firstDuplicateValue(array):
    """
    Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that returns the first integer that appears more than once (when the array is read from left to right).

    In other words, out of all the integers that might occur more than once in the input array, your function should return the one whose first duplicate value has the minimum index. 

    If no integer appears more than once, your function should return -1.

    Note that you're allowed to mutate the input array.

    Sample Input #1:
    ```
    array = [2, 1, 5, 2, 3, 3, 4]
    ```

    Sample Output #1:
    ```
    2 // 2 is the first integer that appears more than once.
    // 3 also appears more than once, but the second 3 appears after the second 2.
    ```

    Sample Input #2:
    ```
    array = [2, 1, 5, 3, 3, 2, 4]
    ```

    Sample Output #2:
    ```
    3 // 3 is the first integer that appears more than once.
    // 2 also appears more than once, but the second two appears after the second 3.
    ```

    Hints:
    1. The brute-force solution can be done in O(n^2) time. Think about how you can determine if a value appears twice in an array.
    2. You can use a data structure that has constant-time lookups to keep track of integers that you've seen already. This leads the way to a linear-time solution.
    3. You should always pay close attention to the details of a question's prompt. In this question, the integers in the array are between 1 and n, inclusive, where n is the length of the input array. The prompt also explicitly allows us to mutate the array. How can these details help us find a better solution, either time-complexity wise or space-complexity wise?
    4. Since the integers are between 1 and length of the input array, you can map them to indices in the array itself by substracting 1 from them. Once you've mapped an integer to an index in the array, you can mutate the value in the array at that index and make it negative (by multiplying it by -1). Since the integers normally aren't negative, the first time that you encounter a negative value at the index that an integer maps to, you'll know that you'll have already seen that integer.

    Optimal Space & Time Complexity
    O(n) time | O(1) space - where n is the length of the input array 
    """
    # O(n^2) time | O(1) space - where n is the length of the input array 
    minimumSecondIndex = len(array)
    for i in range(len(array)):
        value = array[i]
        for j in range(i + 1, len(array)):
            valueToCompare = array[j]
            if value == valueToCompare:
                minimumSecondIndex = min(minimumSecondIndex, j)
    
    if minimumSecondIndex == len(array):
        return -1 
    return array[minimumSecondIndex]

    # O(n) time | O(n) space - where n is the length of the input array 
    seen = set() 
    for value in array:
        if value in seen:
            return value 
        seen.add(value)
    return -1

    # O(n) time | O(1) space - where n is the length of the input array 
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue 
        array[absValue - 1] *= -1
    return -1

if __name__ == "__main__":
    array = [2, 1, 5, 2, 3, 3, 4]
    assert firstDuplicateValue(array) == 2

    array = [2, 1, 5, 3, 3, 2, 4]
    assert firstDuplicateValue(array) == 3

    array = [1, 1, 2, 3, 3, 2, 2]
    assert firstDuplicateValue(array) == 1

    array = [3, 1, 3, 1, 1, 4, 4]
    assert firstDuplicateValue(array) == 3

    array = []
    assert firstDuplicateValue(array) == -1

    array = [1]
    assert firstDuplicateValue(array) == -1

    array = [1, 1]
    assert firstDuplicateValue(array) == 1

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
    assert firstDuplicateValue(array) == 10

    array = [2, 1, 1]
    assert firstDuplicateValue(array) == 1

    array = [2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert firstDuplicateValue(array) == 2

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert firstDuplicateValue(array) == -1

    array = [7, 6, 5, 3, 6, 4, 3, 5, 2]
    assert firstDuplicateValue(array) == 6

    array = [9, 13, 6, 2, 3, 5, 5, 5, 3, 2, 2, 2, 2, 4, 3]
    assert firstDuplicateValue(array) == 5

    array = [23, 21, 22, 5, 3, 13, 11, 16, 5, 11, 9, 14, 23, 3, 2, 2, 5, 11, 6, 11, 23, 8, 1]
    assert firstDuplicateValue(array) == 5

    array = [8, 20, 4, 12, 14, 9, 19, 17, 14, 20, 22, 9, 6, 15, 1, 15, 10, 9, 17, 7, 22, 17]
    assert firstDuplicateValue(array) == 14

    array = [3, 3, 2]
    assert firstDuplicateValue(array) == 3

    array = [6, 6, 5, 1, 3, 7, 7, 8]
    assert firstDuplicateValue(array) == 6

    array = [23, 25, 9, 26, 2, 19, 24, 18, 25, 17, 13, 3, 14, 17, 9, 20, 26, 15, 21, 2, 6, 11, 2, 12, 23, 5, 4, 20]
    assert firstDuplicateValue(array) == 25

    array = [12, 22, 6, 18, 5, 17, 18, 22, 22, 4, 6, 14, 12, 8, 5, 6, 10, 7, 13, 22, 17, 18]
    assert firstDuplicateValue(array) == 18

    array = [16, 6, 6, 18, 6, 13, 28, 9, 3, 26, 10, 2, 23, 5, 20, 21, 11, 20, 6, 11, 26, 20, 26, 25, 13, 3, 12, 4]
    assert firstDuplicateValue(array) == 6

    array = [15, 2, 6, 3, 3, 22, 14, 16, 6, 21, 4, 16, 2, 17, 9, 13, 1, 3, 5, 6, 1, 2, 23, 16, 16]
    assert firstDuplicateValue(array) == 3

    array = [4, 7, 9, 7, 1, 3, 2, 3, 1, 12, 12, 5]
    assert firstDuplicateValue(array) == 7

    array = [9, 21, 9, 22, 3, 23, 4, 26, 7, 11, 25, 25, 19, 13, 23, 28, 5, 23, 19, 13, 10, 26, 28, 9, 28, 16, 7, 13, 22]
    assert firstDuplicateValue(array) == 9

    array = [29, 3, 23, 16, 1, 22, 21, 14, 15, 21, 12, 27, 9, 12, 11, 3, 22, 5, 21, 24, 14, 26, 11, 5, 21, 25, 15, 19, 13, 4]
    assert firstDuplicateValue(array) == 21

    array = [13, 2, 8, 8, 10, 11, 13, 11, 9, 13, 4, 5, 7]
    assert firstDuplicateValue(array) == 8

    array = [4, 7, 7, 14, 14, 10, 15, 14, 14, 16, 14, 11, 5, 12, 17, 7, 1, 6, 13]
    assert firstDuplicateValue(array) == 7

    array = [2, 5, 1, 4, 1]
    assert firstDuplicateValue(array) == 1

    array = [11, 10, 5, 3, 1, 7, 10, 6, 10, 11, 7]
    assert firstDuplicateValue(array) == 10

    array = [2, 13, 3, 9, 1, 9, 1, 11, 11, 5, 3, 1, 9, 12]
    assert firstDuplicateValue(array) == 9

    array = [3, 3, 1, 1]
    assert firstDuplicateValue(array) == 3

    array = [26, 18, 21, 26, 26, 16, 16, 3, 19, 9, 10, 24, 21, 9, 8, 11, 17, 21, 18, 22, 17, 27, 6, 7, 6, 10, 4]
    assert firstDuplicateValue(array) == 26

    array = [27, 16, 15, 21, 10, 21, 3, 21, 5, 12, 27, 24, 20, 26, 5, 13, 26, 22, 26, 8, 23, 10, 14, 17, 7, 5, 3]
    assert firstDuplicateValue(array) == 21

    array = [11, 6, 1, 1, 4, 19, 10, 12, 19, 8, 12, 15, 26, 9, 6, 20, 17, 12, 26, 15, 25, 18, 26, 5, 3, 5, 16, 5]
    assert firstDuplicateValue(array) == 1

    array = [16, 22, 20, 22, 26, 19, 8, 17, 18, 24, 17, 19, 19, 11, 18, 13, 10, 20, 6, 23, 20, 19, 21, 6, 17, 7]
    assert firstDuplicateValue(array) == 22

    array = [11, 13, 6, 12, 4, 15, 4, 9, 3, 10, 5, 8, 15, 5, 8]
    assert firstDuplicateValue(array) == 4

    array = [7, 9, 5, 6, 4, 11, 2, 8, 2, 5, 1]
    assert firstDuplicateValue(array) == 2

    array = [8, 1, 5, 2, 9, 12, 9, 6, 9, 9, 5, 13, 5, 9]
    assert firstDuplicateValue(array) == 9

    array = [11, 5, 2, 7, 11, 11, 3, 11, 4, 2, 9]
    assert firstDuplicateValue(array) == 11

    array = [2, 22, 3, 20, 18, 8, 29, 25, 7, 12, 12, 17, 1, 28, 3, 6, 11, 2, 28, 16, 23, 27, 8, 28, 4, 29, 24, 12, 29]
    assert firstDuplicateValue(array) == 12

    array = [5, 1, 3, 5, 1]
    assert firstDuplicateValue(array) == 5

    array = [20, 12, 3, 18, 9, 16, 4, 18, 6, 19, 14, 23, 10, 13, 6, 1, 22, 11, 11, 16, 13, 15, 17, 19, 14, 12, 20]
    assert firstDuplicateValue(array) == 18

    array = [23, 15, 11, 5, 13, 11, 9, 9, 13, 8, 22, 12, 2, 24, 6, 2, 15, 24, 12, 9, 13, 13, 22, 18]
    assert firstDuplicateValue(array) == 11

    array = [4, 1, 5, 1, 4]
    assert firstDuplicateValue(array) == 1

    array = [7, 14, 4, 6, 17, 17, 3, 14, 1, 16, 18, 4, 12, 13, 8, 19, 1, 2, 4, 14]
    assert firstDuplicateValue(array) == 17

    array = [5, 6, 6, 4, 3, 5]
    assert firstDuplicateValue(array) == 6

    array = [3, 2, 3, 1]
    assert firstDuplicateValue(array) == 3

    array = [9, 12, 14, 6, 14, 2, 4, 9, 13, 2, 10, 5, 7, 1]
    assert firstDuplicateValue(array) == 14

    array = [9, 2, 11, 5, 6, 8, 10, 15, 5, 7, 11, 6, 19, 19, 14, 15, 3, 9, 16]
    assert firstDuplicateValue(array) == 5

    array = [2, 6, 1, 7, 1, 6, 6]
    assert firstDuplicateValue(array) == 1

    array = [6, 3, 1, 8, 2, 2, 1, 7, 10, 8, 6, 4]
    assert firstDuplicateValue(array) == 2

    array = [21, 17, 1, 8, 22, 8, 22, 8, 23, 3, 21, 5, 18, 2, 8, 21, 21, 22, 10, 24, 13, 4, 20, 24]
    assert firstDuplicateValue(array) == 8

    array = [16, 9, 13, 10, 18, 17, 11, 5, 11, 4, 2, 16, 15, 6, 3, 7, 15, 10, 1]
    assert firstDuplicateValue(array) == 11

    array = [5, 5, 5, 4, 6, 6, 2]
    assert firstDuplicateValue(array) == 5

    array = [5, 3, 8, 2, 9, 6, 8, 1, 6]
    assert firstDuplicateValue(array) == 8

    array = [5, 5, 1, 5, 3, 7, 4, 4]
    assert firstDuplicateValue(array) == 5

    array = [19, 4, 1, 6, 2, 5, 20, 13, 8, 6, 11, 12, 12, 12, 11, 18, 7, 13, 6, 10]
    assert firstDuplicateValue(array) == 6

    array = [3, 11, 11, 10, 11, 8, 8, 11, 10, 11, 10, 8, 10]
    assert firstDuplicateValue(array) == 11

    array = [15, 3, 15, 6, 13, 3, 12, 10, 17, 8, 13, 1, 12, 9, 14, 7, 16]
    assert firstDuplicateValue(array) == 15

    array = [2, 2, 2]
    assert firstDuplicateValue(array) == 2

    array = [11, 6, 8, 8, 8, 9, 10, 6, 4, 1, 10, 1, 6]
    assert firstDuplicateValue(array) == 8

    array = [2, 3, 16, 9, 11, 14, 13, 1, 10, 12, 5, 17, 4, 16, 10, 5, 4]
    assert firstDuplicateValue(array) == 16

    array = [13, 4, 10, 10, 8, 13, 13, 7, 11, 6, 3, 2, 11]
    assert firstDuplicateValue(array) == 10

    array = [6, 15, 7, 10, 9, 14, 10, 1, 10, 1, 2, 11, 1, 6, 8]
    assert firstDuplicateValue(array) == 10