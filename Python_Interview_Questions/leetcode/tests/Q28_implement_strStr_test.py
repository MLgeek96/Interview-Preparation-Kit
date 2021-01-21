import pytest
from leetcode.problem_sets.Q28_implement_strStr import strStr

def test_implement_strStr():
    haystack = "hello"
    needle = "ll"
    assert strStr(haystack, needle) == 2

    haystack = "aaaaa"
    needle = "bba"
    assert strStr(haystack, needle) == -1

    haystack = ""
    needle = ""
    assert strStr(haystack, needle) == 0

    haystack = "a"
    needle = "a"
    assert strStr(haystack, needle) == 0

    haystack = ""
    needle = "a"
    assert strStr(haystack, needle) == -1

