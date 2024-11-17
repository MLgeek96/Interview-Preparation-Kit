from typing import List

def largestRange(array: List[int]):
    """
    Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of integers contained in that array.

    The first number in the output array should be the first number in the range, while the second number should be the last number in the range.

    A range of numbers is defined as a set of numbers that ocme right after each other in the set of real integers. For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of length 5. Note that the numbers don't need to be sorted or adjacent in the input array in order to form a range.

    You can assume that there will only be one largest range

    Sample Input:
    ```
    array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    ```

    Sample Output:
    ```
    [0, 7]
    ```

    Hints:
    1. How can you use a hash table to solve this problem with an algorithm that runs in linear time?
    2. Iterate through the input array once, storing every unique number in a hash table and mapping every number to a falsy value. This hash table will not only provide for fast access of the numbers in the input array, but it will also allow you to keep track of "visited" and "unvisited" numbers, so as not to unnecessarily repeat work.
    3. Iterate through the input array once more, this time stopping at every number to check if the number is marked as "visited" in the hash table. If it is, skip it; if it isn't, start expanding outwards from the number with a left number and a right number, continuously checking if those left and right numbers are in the hash table (and thus in the input array), and marking them as "visited" in the hash table if they are. This should allow you to quickly find the largest range in which the current number is contained, all the while setting you up not to perform unnecessary work later.

    Optimal Space & Time Complexity
    O(n) time | O(n) space - where n is the length of the input array 
    """
    bestRange = []
    longestLength = 0 
    nums = {}
    for num in array:
        nums[num] = True 
    for num in array:
        if not nums[num]:
            continue 
        nums[num] = False 
        currentLength = 1 
        left = num - 1
        right = num + 1
        while left in nums: 
            nums[left] = False 
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False 
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange

if __name__ == "__main__":
    array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    assert largestRange(array) == [0, 7]

    array = [1]
    assert largestRange(array) == [1, 1]

    array = [1, 2]
    assert largestRange(array) == [1, 2]

    array = [4, 2, 1, 3]
    assert largestRange(array) == [1, 4]

    array = [4, 2, 1, 3, 6]
    assert largestRange(array) == [1, 4]

    array = [8, 4, 2, 10, 3, 6, 7, 9, 1]
    assert largestRange(array) == [6, 10]

    array = [19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]
    assert largestRange(array) == [10, 19]

    array = [0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]
    assert largestRange(array) == [-1, 19]

    array = [0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]
    assert largestRange(array) == [-7, 7]

    array = [-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2]
    assert largestRange(array) == [-8, 19]

    array = [1, 1, 1, 3, 4]
    assert largestRange(array) == [3, 4]

    array = [-1, 0, 1]
    assert largestRange(array) == [-1, 1]

    array = [10, 0, 1]
    assert largestRange(array) == [0, 1]