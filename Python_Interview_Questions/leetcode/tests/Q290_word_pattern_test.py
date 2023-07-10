import pytest
from leetcode.problem_sets.Q290_word_pattern import wordPattern

print(wordPattern.__doc__)

def test_wordPattern():
    pattern = "abba"
    s = "dog cat cat dog"
    assert wordPattern(pattern, s) == True

    pattern = "abba"
    s = "dog cat cat fish"
    assert wordPattern(pattern, s) == False

    pattern = "aaaa"
    s = "dog cat cat dog"
    assert wordPattern(pattern, s) == False