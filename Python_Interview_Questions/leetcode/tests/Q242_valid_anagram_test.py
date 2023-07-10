import pytest
from leetcode.problem_sets.Q242_valid_anagram import isAnagram

print(isAnagram.__doc__)

def test_isAnagram():
    s = "anagram"
    t = "nagaram"
    assert isAnagram(s, t) == True
    
    s = "rat"
    t = "car"
    assert isAnagram(s, t) == False