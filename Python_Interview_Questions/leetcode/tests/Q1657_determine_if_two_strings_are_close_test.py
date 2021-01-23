import pytest
from leetcode.problem_sets.Q1657_determine_if_two_strings_are_close import closeStrings


print(closeStrings.__doc__)

def test_determine_if_two_strings_are_close():
    word1 = "abc"
    word2 = "bca"
    assert closeStrings(word1, word2) == True

    word1 = "a"
    word2 = "aa"
    assert closeStrings(word1, word2) == False

    word1 = "cabbba"
    word2 = "abbccc"
    assert closeStrings(word1, word2) == True

    word1 = "cabbba"
    word2 = "aabbss"
    assert closeStrings(word1, word2) == False



