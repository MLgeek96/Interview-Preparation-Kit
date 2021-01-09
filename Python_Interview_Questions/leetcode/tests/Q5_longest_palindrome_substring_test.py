import pytest
from leetcode.problem_sets.Q5_longest_palindrome_substring import longestPalindrome

def test_longest_palindrome_substring():
    string = "babad"
    ans = longestPalindrome(string)

    assert ans in ['bab', 'aba']

    string = "cbbd"
    ans = longestPalindrome(string)

    assert ans == "bb"

    string = "a"
    ans = longestPalindrome(string)

    assert ans == "a"

    string = "ac"
    ans = longestPalindrome(string)

    assert ans == "a"

