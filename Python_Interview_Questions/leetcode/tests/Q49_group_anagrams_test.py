import pytest
from leetcode.problem_sets.Q49_group_anagrams import groupAnagrams

print(groupAnagrams.__doc__)

def test_groupAnagrams():
    strs = ["eat","tea","tan","ate","nat","bat"]
    assert groupAnagrams(strs) == [["bat"],["tan","nat"],["eat","tea","ate"]]

    strs = [""]
    assert groupAnagrams(strs) == [[""]]

    strs = ["a"]
    assert groupAnagrams(strs) == [["a"]]

    strs = ["",""]
    assert groupAnagrams(strs) == [["",""]]
    
    strs = ["tea","","eat","","tea",""]
    assert groupAnagrams(strs) == [['tea', 'eat', 'tea'], ['', '', '']]