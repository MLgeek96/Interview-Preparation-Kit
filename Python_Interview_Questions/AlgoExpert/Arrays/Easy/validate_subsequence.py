from typing import List

def isValidSubsequence(array: List[int], sequence: List[int]):
    """
    Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

    A subsequence of an array si a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

    Sample Input:
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]

    Sample Output: 
    true

    Hints:
    1. You can solve this question by iterating through the main input array once.
    
    2. Iterate through the main array, and look for the first integer in the potential subsequence. If you find that integer, keep on iterating through the main array, but now look for the second integer in the potential subsequence. Continue this process until you either find every integer in the potential subsequence or you reach the end of the main array.

    3. To actually implement what Hint #2 describes, you'll have to declare a variable holding your position in the potential subsequence. At first, this position will be the 0th index in the sequence; as you find the sequence's integers in the main array, you'll increment the position variable until you reach the end of the sequence.

    Optimal Space & Time Complexity:
    O(n) time | O(1) space - where n is the length of the array
    """

    # O(n) time | O(1) space
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

    # O(n) time | O(1) space
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    assert isValidSubsequence(array, sequence) is True

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 1, 22, 25, 6, -1, 8, 10]
    assert isValidSubsequence(array, sequence) is True

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 1, 22, 6, -1, 8, 10]
    assert isValidSubsequence(array, sequence) is True

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [22, 25, 6]
    assert isValidSubsequence(array, sequence) is True

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, 10]
    assert isValidSubsequence(array, sequence) is True

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 1, 22, 10]
    assert isValidSubsequence(array, sequence) is True

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, -1, 8, 10]
    assert isValidSubsequence(array, sequence) is True

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [25]
    assert isValidSubsequence(array, sequence) is True

    array = [1, 1, 1, 1, 1]
    sequence = [1, 1, 1]
    assert isValidSubsequence(array, sequence) is True

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 1, 22, 25, 6, -1, 8, 10, 12]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [4, 5, 1, 22, 25, 6, -1, 8, 10]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 1, 22, 23, 6, -1, 8, 10]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 1, 22, 22, 25, 6, -1, 8, 10]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 1, 22, 22, 6, -1, 8, 10]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, -1]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, -1, 10]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, -2]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [26]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 1, 25, 22, 6, -1, 8, 10]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 26, 22, 8]
    assert isValidSubsequence(array, sequence) is False

    array = [1, 1, 6, 1]
    sequence = [1, 1, 1, 6]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10, 11, 11, 11, 11]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 1, 22, 25, 6, -1, 8, 10, 10]
    assert isValidSubsequence(array, sequence) is False

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 5]
    assert isValidSubsequence(array, sequence) is False