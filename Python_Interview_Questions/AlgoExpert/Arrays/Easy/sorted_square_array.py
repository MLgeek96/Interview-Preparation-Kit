from typing import List

def sortedSquaredArrays(array: List[int]):
    """
    Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new
    array of the same length with the squares of the original integers also sorted in ascending order.

    Sample Input:
    array = [1, 2, 3, 5, 6, 8, 9]

    Sample Output:
    [1, 4, 9, 25, 36, 64, 81]

    Hints:
    1. While the integers in the input array are sorted in increasing order, their squares won't necessarily be as well,
    because of the possible presence of negative numbers.

    2. Traverse the array value by value, square each value, and insert the squares into the output array. Then, sort the
    output array before returning it. Is this the optimal solution?

    3. To reduce the time complexity of the algorithm mentioned in Hint #2, you need to avoid sorting the output array.
    To do this, as you squares the values of the input array, try to directly insert them into their correct position in
    the output array.

    4. Use two pointers to keep track of the smallest and largest values in the input array. Compare the absolute values
    of these smallest and largest values, square the larger absolute value, and place the square at the end of the output
    array, filling it up from right to left. Move the pointers accordingly, and repeat this process until the output
    array is filled.

    Optimal Space & Time Complexity:
    O(n) time | O(n) space, where n is the length of the input array
    """
    # O(nlogn) time | O(n) space
    sortedSquares = [0 for _ in array]
    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value
    sortedSquares.sort()
    return sortedSquares

    # O(n) time | O(n) space
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx += 1
    return sortedSquares

    # O(n) time | O(n) space
    # res = []
    # left_pointer, right_pointer = 0, len(array) - 1
    # while left_pointer <= right_pointer:
    #     smallest_value, largest_value = array[left_pointer], array[right_pointer]
    #     if abs(smallest_value) < abs(largest_value):
    #         res.append(largest_value ** 2)
    #         right_pointer -= 1
    #     else:
    #         res.append(smallest_value ** 2)
    #         left_pointer += 1
    # return res[::-1]

if __name__ == "__main__":
    array = [1, 2, 3, 5, 6, 8, 9]
    assert sortedSquaredArrays(array) == [1, 4, 9, 25, 36, 64, 81]

    array = [1]
    assert sortedSquaredArrays(array) == [1]

    array = [1, 2]
    assert sortedSquaredArrays(array) == [1, 4]

    array = [1, 2, 3, 4, 5]
    assert sortedSquaredArrays(array) == [1, 4, 9, 16, 25]

    array = [0]
    assert sortedSquaredArrays(array) == [0]

    array = [10]
    assert sortedSquaredArrays(array) == [100]

    array = [-1]
    assert sortedSquaredArrays(array) == [1]

    array = [-2, -1]
    assert sortedSquaredArrays(array) == [1, 4]

    array = [-5, -4, -3, -2, -1]
    assert sortedSquaredArrays(array) == [1, 4, 9, 16, 25]

    array = [-10]
    assert sortedSquaredArrays(array) == [100]

    array = [-10, -5, 0, 5, 10]
    assert sortedSquaredArrays(array) == [0, 25, 25, 100, 100]

    array =  [-7, -3, 1, 9, 22, 30]
    assert sortedSquaredArrays(array) == [1, 9, 49, 81, 484, 900]

    array = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]
    assert sortedSquaredArrays(array) == [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]

    array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert sortedSquaredArrays(array) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    array = [-1, -1, 2, 3, 3, 3, 4]
    assert sortedSquaredArrays(array) == [1, 1, 4, 9, 9, 9, 16]

    array = [-3, -2, -1]
    assert sortedSquaredArrays(array) == [1, 4, 9]

    array = [-3, -2, -1]
    assert sortedSquaredArrays(array) == [1, 4, 9]

