from typing import List

def quickSelect(array, k):
    """
    Write a function that takes in an array of distinct integers as well as an integer k and that returns the kth smallest integer in that array. 

    The function should do this in linear time, on average.

    Sample Input:
    ```
    array = [8, 5, 2, 9, 7, 6, 3]
    k = 3
    ```

    Sample Output:
    ```
    5
    ```

    Hints:
    1. The Quick Sort sorting algorithm works by picking a "pivot" number form an array, positioning every other number in the array in sorted order with respect to the pivot (all smaller numbers to the pivot's left; all bigger numbers to the pivot's right), and then repeating the same two steps on both sides of the pivot until the entire array is sorted. Apply the technique used in Quick Sort until the pivot elements gets positioned in the kth place in the array, at which point you'll have found the answer to the problem.
    2. Pick a random number from the input array (the first number, for instance) and let that number be the pivot. Iterate through the rest of the array using two pointers, one starting at the left extremity of the array and progressively moving to the right, and the other one starting at the right extremity of the array and progressively moving to the left. As you iterate through the array, compare the left and right pointer numbers to the pivot. If the left number is greater than the pivot and the right number is less than the pivot, swap them; this will effectively sort these numbers with respect to the pivot at the end of the iteration. If the left number is ever less than or equal to the pivot, increment the left pointer; similarly, if the right number is ever greater than or equal to teh pivot, decrement the right pointer. Do this until the pointers pass each other, at which point swapping the pivot with the right number should position the pivot in its final, sorted position, where every number to its left is smaller and every number to its right is greater. If the pivot is in the kth position, you're done; if it isn't, figure out if the kth smallest number is located to the left or to the right of the pivot.
    3. Repeat the process mentioned in Hint #2 on the side of the kth smallest number, and keep on repeating the process thereafter until you find the answer. What is the time complexity of the algorithm?

    Optimal Space & Time Complexity
    Best: O(n) time | O(1) space - where n is the length of the input array 
    Average: O(n) time | O(1) space - where n is the length of the input array 
    Worst: O(n^2) time | O(1) space - where n is the length of the input array 
    """
    position = k - 1
    return quickSelectHelper(array, 0, len(array) - 1, position)

def quickSelectHelper(array, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            raise Exception("Your algorithm should never arrive here!")
        pivotIdx = startIdx 
        leftIdx = startIdx + 1
        rightIdx = endIdx 
        while leftIdx <= rightIdx:
            if array[leftIdx] > array[rightIdx] and array[rightIdx] < array[pivotIdx]:
                swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
        swap(pivotIdx, rightIdx, array)
        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1

def swap(one, two, array):
    array[one], array[two] = array[two], array[one]

if __name__ == "__main__":
    array = [8, 5, 2, 9, 7, 6, 3]
    k = 3
    assert quickSelect(array, k) == 5

    array = [1]
    k = 1
    assert quickSelect(array, k) == 1

    array = [43, 24, 37]
    k = 1
    assert quickSelect(array, k) == 24

    array = [43, 24, 37]
    k = 2
    assert quickSelect(array, k) == 37

    array = [43, 24, 37]
    k = 3
    assert quickSelect(array, k) == 43

    array = [8, 3, 2, 5, 1, 7, 4, 6]
    k = 1
    assert quickSelect(array, k) == 1

    array = [8, 3, 2, 5, 1, 7, 4, 6]
    k = 2
    assert quickSelect(array, k) == 2

    array = [8, 3, 2, 5, 1, 7, 4, 6]
    k = 3
    assert quickSelect(array, k) == 3

    array = [8, 3, 2, 5, 1, 7, 4, 6]
    k = 4
    assert quickSelect(array, k) == 4

    array = [8, 3, 2, 5, 1, 7, 4, 6]
    k = 5
    assert quickSelect(array, k) == 5

    array = [8, 3, 2, 5, 1, 7, 4, 6]
    k = 6
    assert quickSelect(array, k) == 6

    array = [8, 3, 2, 5, 1, 7, 4, 6]
    k = 7
    assert quickSelect(array, k) == 7

    array = [8, 3, 2, 5, 1, 7, 4, 6]
    k = 8
    assert quickSelect(array, k) == 8

    array = [102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15]
    k = 5
    assert quickSelect(array, k) == 25

    array = [102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15]
    k = 4
    assert quickSelect(array, k) == 15

    array = [102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15]
    k = 9
    assert quickSelect(array, k) == 102

    array = [1, 3, 71, 123, 124, 156, 814, 1294, 10024, 110000, 985181, 55516151]
    k = 12
    assert quickSelect(array, k) == 55516151

    array = [1, 3, 71, 123, 124, 156, 814, 1294, 10024, 110000, 985181, 55516151]
    k = 4
    assert quickSelect(array, k) == 123