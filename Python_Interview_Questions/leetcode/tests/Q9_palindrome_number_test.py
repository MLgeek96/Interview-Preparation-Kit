import pytest
from leetcode.problem_sets.Q9_palindrome_number import isPalindrome

print(isPalindrome.__doc__)

def test_palindrome_number():
    x = 121
    assert isPalindrome(x) == True

    x = -121
    assert isPalindrome(x) == False

    x = 10
    assert isPalindrome(x) == False

    x = -101
    assert isPalindrome(x) == False