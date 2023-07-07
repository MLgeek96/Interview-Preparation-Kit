import re

def isPalindrome(s: str) -> bool:
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

    Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

    Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
    

    Constraints:
    • 1 <= s.length <= 2 * 10 ** 5
    • s consists only of printable ASCII characters.

    """
    assert 1 <= len(s) <= 2 * 10 ** 5, "Length of s must be between 1 and 2 * 10 ** 5"
    assert all(ord(char) < 128 for char in s), "s must consist only of printable ASCII characters"
    
    new_str = re.sub(r'[^a-zA-Z0-9]', '', s)
    new_str = new_str.lower()

    leftPointer, rightPointer = 0, len(new_str) - 1
    while leftPointer < rightPointer:
        if new_str[leftPointer] != new_str[rightPointer]:
            return False
        leftPointer += 1
        rightPointer -= 1

    return True