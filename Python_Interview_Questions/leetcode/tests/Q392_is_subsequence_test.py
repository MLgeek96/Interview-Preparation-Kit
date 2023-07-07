import pytest
from leetcode.problem_sets.Q392_is_subsequence import isSubsequence

print(isSubsequence.__doc__)

def test_isSubsequence():
    s = "abc"
    t = "ahbgdc"
    assert isSubsequence(s, t) == True

    s = "axc"
    t = "ahbgdc"
    assert isSubsequence(s, t) == False