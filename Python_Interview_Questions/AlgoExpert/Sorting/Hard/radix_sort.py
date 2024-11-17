from typing import List

def radixSort(array: List[int]):
    """
    Write a function that takes in an array of non-negative integers and returns a sorted version of that array. Use the Radix Sort algorithm to sort the array. 

    If you are unfamiliar with Heap Sort, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.

    Sample Input:
    ```
    array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
    ```

    Sample Output:
    ```
    [2, 12, 65, 87, 237, 345, 654, 3008, 8762]
    ```

    Hints:
    1. Radix Sort sorts numbers by looking only at one of their digits at a time. It first sorts all of the given numbers by their ones'column, then by their tens'column, then by their hundred's'column, and so on and so forth until they're fully sorted.
    2. Radix Sort uses an intermediary sorting algorithm to sort numbers one digits' column at a time. The goal of Radix Sort is to perform a more efficient sort than popular sorting algorithms like Merge Sort or Quick Sort for inputs that are well suited to be sorted by their individual digits' columns. With this in mind, what intermediary sorting algorithm should we use with Radix Sort? Keep in mind that this sorting algorithm will run multiple times, sorting one digits' column at a time.
    3. The most popular sorting algorithm to use with Radix Sort is Counting Sort. Counting Sort takes advantage of the fact that we know the range of possible values that we need to sort. When sorting numbers, we know that we only need to sort digits, which will always be in the range 0-9. Therefore, we can count how many times these digits occur and use those counts to populate a new sorted array. We'll perform counting sort multiple times, once for each digits' column that we're sorting, starting with the ones' column. We need to ensure that our counting sort performs a stable sort, so that we don't lose information from previous iterations of sorting. Counting sort runs in O(n) time, which means that we might have a much more efficient sorting algorithm if the largest number in our input contains few digits. See the Conceptual Overview section of this question's video explanation for a more in-depth explanation.

    Optimal Space & Time Complexity
    O(d * (n + b)) times | O(n + b) space - where n is the length of the input array, d is the max number of digits, and b is the base of the numbering system used
    """
    if len(array) == 0:
        return array 

    maxNumber = max(array)
    digit = 0 
    while maxNumber / 10 ** digit > 0:
        countingSort(array, digit)
        digit += 1
    
    return array 

def countingSort(array, digit):
    sortedArray = [0] * len(array)
    countArray = [0] * 10 

    digitColumn = 10 ** digit 
    for num in array:
        countIndex = (num // digitColumn) % 10 
        countArray[countIndex] += 1

    for idx in range(1, 10):
        countArray[idx] += countArray[idx - 1]

    for idx in range(len(array) - 1, -1, -1):
        countIndex = (array[idx] // digitColumn) % 10
        countArray[countIndex] -= 1
        sortedIndex = countArray[countIndex]
        sortedArray[sortedIndex] = array[idx]

    for idx in range(len(array)):
        array[idx] = sortedArray[idx]

if __name__ == "__main__":
    array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
    assert radixSort(array) == [2, 12, 65, 87, 234, 345, 654, 3008, 8762]

    array = [2, 12, 65, 87, 234, 345, 654, 3008, 8762]
    assert radixSort(array) == [2, 12, 65, 87, 234, 345, 654, 3008, 8762]

    array = [111, 11, 11, 1, 0]
    assert radixSort(array) == [0, 1, 11, 11, 111]

    array = [12, 123, 456, 986, 2, 3, 34, 543, 97654, 34200]
    assert radixSort(array) == [2, 3, 12, 34, 123, 456, 543, 986, 34200, 97654]

    array = [4, 44, 444, 888, 88, 33, 3, 22, 2222, 1111, 1234]
    assert radixSort(array) == [3, 4, 22, 33, 44, 88, 444, 888, 1111, 1234, 2222]

    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert radixSort(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    array = []
    assert radixSort(array) == []

    array = [100]
    assert radixSort(array) == [100]

    array = [10000, 100001, 10001, 10101, 101, 11, 100, 10, 1, 0]
    assert radixSort(array) == [0, 1, 10, 11, 100, 101, 10000, 10001, 10101, 100001]

    array = [34, 56, 7373, 2321, 3421, 8272, 232, 23892831, 230983, 2312, 7878, 87, 234, 23, 332, 4556]
    assert radixSort(array) == [23, 34, 56, 87, 232, 234, 332, 2312, 2321, 3421, 4556, 7373, 7878, 8272, 230983, 23892831]

    array = [10, 87, 2321, 3221, 2312, 7632, 6542, 3223, 231, 2342, 321, 9, 1, 323, 421, 325, 65, 789, 4002]
    assert radixSort(array) == [1, 9, 10, 65, 87, 231, 321, 323, 325, 421, 789, 2312, 2321, 2342, 3221, 3223, 4002, 6542, 7632]

    array = [0, 1, 2, 22, 11, 3, 33, 0, 0, 0, 21, 21, 21, 1, 11, 111]
    assert radixSort(array) == [0, 0, 0, 0, 1, 1, 2, 3, 11, 11, 21, 21, 21, 22, 33, 111]

    array = [8, 4, 5, 34, 234, 987, 444, 23, 21, 8, 1, 0]
    assert radixSort(array) == [0, 1, 4, 5, 8, 8, 21, 23, 34, 234, 444, 987]

    array = [1, 11]
    assert radixSort(array) == [1, 11]

    array = [1, 11, 1, 11, 101, 9, 99, 432, 441]
    assert radixSort(array) == [1, 1, 9, 11, 11, 99, 101, 432, 441]

    array = [1000, 100, 10, 1, 10, 100, 1000, 10001, 10201, 1001, 0, 1, 1]
    assert radixSort(array) == [0, 1, 1, 1, 10, 10, 100, 100, 1000, 1000, 1001, 10001, 10201]

    array = [9, 109, 908, 876, 1099, 190, 290, 999, 9999]
    assert radixSort(array) == [9, 109, 190, 290, 876, 908, 999, 1099, 9999]

    array = [0, 999999, 234892, 10000009, 89892, 782731, 891932, 92012, 1892193, 181730, 785239, 2314451, 1231421, 812723]
    assert radixSort(array) == [0, 89892, 92012, 181730, 234892, 782731, 785239, 812723, 891932, 999999, 1231421, 1892193, 2314451, 10000009]