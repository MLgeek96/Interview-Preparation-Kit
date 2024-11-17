from typing import List

def countInversions(array):
    """
    Write a function that takes in an array of integers and returns the number of inversions in the array. An inversion occurs if for any valid indices i and j, i < j and array[i] > array[j].

    For example, given array = [3, 4, 1, 2], there are 4 inversions. The following pairs of indices represent inversions: [0, 2], [0, 3], [1, 2], [1, 3].

    Intuitively, the number of inversions is a measure of how unsorted the array is.

    Sample Input:
    ```
    array = [2, 3, 3, 1, 9, 5, 6]
    ```

    Sample Output:
    ```
    5
    // The following pairs of indices represent inversions:
    // [0, 3], [1, 3], [2, 3], [4, 5], [4, 6]
    ```

    Hints:
    1. The brute-force approach to solve this problem is to simply compare every pair of indices in the array and to determine how many of them represent inversions. This approach takes O(n^2) time, where n is the length of the array. Can you do better than this?
    2. If the number of inversions is the degree to which the array is unsorted, and it if it takes O(nlog(n)) time to sort an arary using an optimal sorting algorithm, can you determine how unsorted the array is with a solution that runs in that time complexity?
    3. Try thinking about how you would solve this problem if, instead of being given one array, you were given two separate arrays representing the main array's two halves. You would need to determine the number of inversions in the array created by merging the left array and the right array. The number of inversions in this example is actually equal to the number of inversions in the left array, the number of inversions in the right array, and the number of inversions when you merge the sorted left array and the sorted right array. Recall how Merge Sort works for a hint above you can solve this problem.
    4. Once you understand the information stated in Hint #3, you can use an algorithm that is very similar to Merge Sort to determine the number of inversions in any array. You'll recurisvely determine the number of inversions in the left and right halves of an array while sorting both the left and righ thalves, just like you do in Merge Sort. Once your two halves, are sorted, you'll merge them together and count the number of inversions in the merged array. Take the exmaple of these two sorted arrays: a1 = [1, 3, 4] and a2 = [2, 2, 5]. When you merge these two sorted arrays, you insert elements from the left and right array into one larger array. Whenever you insert elements from the right array before inserting an element from the left array, that means an inversion or multiple inversions have occured. This is because elements in the right array are positioned after all elements in the left array (if these two arrays were originally left and right halves of another array). The remaining elements to be inserted from the left array when we insert an element from the right array are all inverted with this right-array element. See the Conceptual Overview section fo this question's video explanation for a more in-depth explanation.

    Optimal Space & Time Complexity
    O(nlog(n)) time | O(n) space - where n is the length of the array
    """
    return countSubArrayInversions(array, 0, len(array))

def countSubArrayInversions(array, start, end):
    if end - start <= 1:
        return 0
    middle = start + (end - start) // 2
    leftInversions = countSubArrayInversions(array, start, middle)
    rightInversions = countSubArrayInversions(array, middle, end)
    mergedArrayInversions = mergeSortAndCountInversions(array, start, middle, end)
    return leftInversions + rightInversions + mergedArrayInversions

def mergeSortAndCountInversions(array, start, middle, end):
    sortedArray = []
    left = start 
    right = middle 
    inversions = 0

    while left < middle and right < end:
        if array[left] <= array[right]:
            sortedArray.append(array[left])
            left += 1
        else:
            inversions += middle - left 
            sortedArray.append(array[right])
            right += 1
    
    sortedArray += array[left: middle] + array[right: end]
    for idx, num in enumerate(sortedArray):
        array[start + idx] = num 
    
    return inversions

if __name__ == "__main__":
    array = [2, 3, 3, 1, 9, 5, 6]
    assert countInversions(array) == 5

    array = []
    assert countInversions(array) == 0

    array = [1, 2, 3, 4, 5, 6, -1]
    assert countInversions(array) == 6

    array = [0, 2, 4, 5, 76]
    assert countInversions(array) == 0

    array = [54, 1, 2, 3, 4]
    assert countInversions(array) == 4

    array = [1, 10, 2, 8, 3, 7, 4, 6, 5]
    assert countInversions(array) == 16

    array = [2, -18]
    assert countInversions(array) == 1

    array = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert countInversions(array) == 105

    array = [5, -1, 2, -4, 3, 4, 19, 87, 762, -8, 0]
    assert countInversions(array) == 23

    array = [1, 1, 1, 1, 1, 1, 1, 1]
    assert countInversions(array) == 0

    array = [1, 1, 1, 1, 0, 1, 1, 1]
    assert countInversions(array) == 4

    array = [2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3]
    assert countInversions(array) == 16

    array = [3, 1, 2]
    assert countInversions(array) == 2

    array = [3, 2, 1, 1]
    assert countInversions(array) == 5

    array = [10, 7, 2, 3, 1, -9, -86, -862, 234, 312, 3421, 23, 0, 2, 1, 2]
    assert countInversions(array) == 62