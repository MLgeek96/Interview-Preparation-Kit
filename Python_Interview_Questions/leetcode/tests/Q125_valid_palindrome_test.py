import pytest
from leetcode.problem_sets.Q125_valid_palindrome import isPalindrome

def test_isPalindrome():
    s = "A man, a plan, a canal: Panama"
    assert isPalindrome(s) == True

    s = "race a car"
    assert isPalindrome(s) == False

    s = " "
    assert isPalindrome(s) == True