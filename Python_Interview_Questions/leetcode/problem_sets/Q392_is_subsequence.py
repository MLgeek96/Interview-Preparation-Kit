import re

def isSubsequence(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
        
    Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

    Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false
    
    Constraints:
    • 0 <= s.length <= 100
    • 0 <= t.length <= 10 ** 4
    • s and t consist only of lowercase English letters.

    Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

    """

    assert 0 <= len(s) <= 100, "Length of string s must be between 0 and 100"
    assert 0 <= len(t) <= 10 ** 4, "Length of string t must be between 0 and 10 ** 4"
    assert re.search('[a-z]', s), "String s must consist only of lowercase English letters"
    assert re.search('[a-z]', t), "String t must consist only of lowercase English letters"

    sPointer = tPointer = 0
    while sPointer < len(s) and tPointer < len(t):
        if s[sPointer] == t[tPointer]:
            sPointer += 1
        tPointer += 1

    return sPointer == len(s)