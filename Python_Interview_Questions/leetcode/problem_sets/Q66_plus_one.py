from re import A
from typing import List

def plusOne(digits: List[int]) -> List[int]:
    """
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

    Example 1:
    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4].

    Example 2:
    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
    Incrementing by one gives 4321 + 1 = 4322.
    Thus, the result should be [4,3,2,2].

    Example 3:
    Input: digits = [9]
    Output: [1,0]
    Explanation: The array represents the integer 9.
    Incrementing by one gives 9 + 1 = 10.
    Thus, the result should be [1,0].

    Constraints:
    • 1 <= digits.length <= 100
    • 0 <= digits[i] <= 9
    • digits does not contain any leading 0's.
    """
    assert 1 <= len(digits) <= 100, "Length of input array must be between 1 and 100"
    for digit in digits:
        assert 0 <= digit <= 9, "Digit must be between 0 and 9"
    
    pointer = 0
    while pointer <= len(digits):
        if digits[pointer] != 0:
            break
        assert digits[pointer] != 0, "Digits does not contain any leading 0's"
        pointer += 1

    # num_str = "".join(map(str, digits))
    # num = int(num_str) + 1
    # return list(map(int, str(num)))

    for i in reversed(range(len(digits))):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    digits.insert(0, 1)

    return digits