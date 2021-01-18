import pytest
from leetcode.problem_sets.Q14_longest_common_prefix import longestCommonPrefix

def test_longest_common_prefix():
    strs = ["flower","flow","flight"]
    assert longestCommonPrefix(strs) == "fl"

    strs = ["dog","racecar","car"]
    assert longestCommonPrefix(strs) == ""

    strs = [""]
    assert longestCommonPrefix(strs) == ""

