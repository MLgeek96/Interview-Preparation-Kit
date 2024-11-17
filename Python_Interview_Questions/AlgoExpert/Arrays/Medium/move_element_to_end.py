from typing import List

def moveElementToEnd(array: List[int], toMove: int):
    """
    You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

    The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the orders of the other integers.

    Sample Input:
    ```
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    ```

    Sample Output:
    ```
    [1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently
    ```

    Hints:
    1. You can solve this problem in linear time.
    2. In view of Hint #1, you can solve this problem without sorting the input array. Try setting two pointers at the start and end of the array, respectively, and progressively moving them inwards.
    3. Following Hint #2, set two pointers at the start and end of the array, respectively. Move the right pointer inwards so long as it points to the integer to move, and move the left pointer inwards so long as it doesn't point to the integer to move. When both pointers aren't moving, swap their values in place. Repeat this process until the pointers pass each other.


    Optimal Space & Time Complexity
    O(n) time | O(1) space - where n is the length of the array
    """
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array

if __name__ == "__main__":
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    assert moveElementToEnd(array, toMove) == [4, 1, 3, 2, 2, 2, 2, 2]

    array = []
    toMove = 3
    assert moveElementToEnd(array, toMove) == []

    array = [1, 2, 4, 5, 6]
    toMove = 3
    assert moveElementToEnd(array, toMove) == [1, 2, 4, 5, 6]

    array = [3, 3, 3, 3, 3]
    toMove = 3
    assert moveElementToEnd(array, toMove) == [3, 3, 3, 3, 3]

    array = [3, 1, 2, 4, 5]
    toMove = 3
    assert moveElementToEnd(array, toMove) == [5, 1, 2, 4, 3]

    array = [1, 2, 4, 5, 3]
    toMove = 3
    assert moveElementToEnd(array, toMove) == [1, 2, 4, 5, 3]

    array = [1, 2, 3, 4, 5]
    toMove = 3
    assert moveElementToEnd(array, toMove) == [1, 2, 5, 4, 3]

    array = [2, 4, 2, 5, 6, 2, 2]
    toMove = 2
    assert moveElementToEnd(array, toMove) == [6, 4, 5, 2, 2, 2, 2]

    array = [5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
    toMove = 5
    assert moveElementToEnd(array, toMove) == [12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 6, 5, 5, 5, 5, 5, 5]

    array = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]
    toMove = 5
    assert moveElementToEnd(array, toMove) == [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]

    array = [5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12]
    toMove = 5
    assert moveElementToEnd(array, toMove) == [12, 1, 2, 11, 10, 3, 4, 6, 7, 9, 8, 5, 5, 5, 5, 5, 5]