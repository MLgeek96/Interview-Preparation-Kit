from cgitb import small
from typing import List

def smallestDifference(arrayOne: List[int], arrayTwo: List[int]):
    """
    Write a function that takes in two non-empty arrays of integers, find the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

    Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

    You can assume that there will only be one pair of numbers with the smallest difference.

    Sample Input:
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]

    Sample Output:
    [28, 26]

    Optimal Space & Time Complexity:
    O(nlog(n) + mlog(m)) time | O(1) space - where n is the length of the first input array and m is the length of the second input array
    """
    # O(nlog(n) + mlog(m) time) | O(1) space
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair

    # arrayOne.sort()
    # arrayTwo.sort()

    # arrayOnePointer = 0
    # arrayTwoPointer = 0
    # minDifference = float('inf')

    # while arrayOnePointer < len(arrayOne) and arrayTwoPointer < len(arrayTwo):
    #     difference = abs(arrayOne[arrayOnePointer] - arrayTwo[arrayTwoPointer])
    #     if difference == 0:
    #         return [arrayOne[arrayOnePointer], arrayTwo[arrayTwoPointer]]
    #     elif difference < minDifference:
    #         minDifference = difference
    #         minDifferencePair = [arrayOne[arrayOnePointer], arrayTwo[arrayTwoPointer]]
        
    #     if arrayOne[arrayOnePointer] < arrayTwo[arrayTwoPointer]:
    #         arrayOnePointer += 1
    #     else:
    #         arrayTwoPointer += 1
    # return minDifferencePair

if __name__ == "__main__":
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]
    assert smallestDifference(arrayOne, arrayTwo) == [28, 26]

    arrayOne = [-1, 5, 10, 20, 3]
    arrayTwo = [26, 134, 135, 15, 17]
    assert smallestDifference(arrayOne, arrayTwo) == [20, 17]

    arrayOne = [10, 0, 20, 25]
    arrayTwo = [1005, 1006, 1014, 1032, 1031]
    assert smallestDifference(arrayOne, arrayTwo) == [25, 1005]

    arrayOne = [10, 0, 20, 25, 2200]
    arrayTwo = [1005, 1006, 1014, 1032, 1031]
    assert smallestDifference(arrayOne, arrayTwo) == [25, 1005]

    arrayOne = [10, 0, 20, 25, 2000]
    arrayTwo = [1005, 1006, 1014, 1032, 1031]
    assert smallestDifference(arrayOne, arrayTwo) == [2000, 1032]

    arrayOne = [240, 124, 86, 111, 2, 84, 954, 27, 89]
    arrayTwo = [1, 3, 954, 19, 8]
    assert smallestDifference(arrayOne, arrayTwo) == [954, 954]

    arrayOne = [0, 20]
    arrayTwo = [21, -2]
    assert smallestDifference(arrayOne, arrayTwo) == [20, 21]

    arrayOne = [10, 1000]
    arrayTwo = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
    assert smallestDifference(arrayOne, arrayTwo) == [1000, 1014]

    arrayOne = [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123]
    arrayTwo = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
    assert smallestDifference(arrayOne, arrayTwo) == [-123, -124]

    arrayOne = [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530]
    arrayTwo = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
    assert smallestDifference(arrayOne, arrayTwo) == [530, 530]

