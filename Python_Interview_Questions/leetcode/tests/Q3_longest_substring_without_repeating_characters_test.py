import pytest 
from leetcode.problem_sets.Q3_longest_substring_without_repeating_characters import longest_substring_without_repeating_characters

def test_longest_substring_without_repeating_characters():
    string = "abcabcbb"
    ans = longest_substring_without_repeating_characters(string)

    assert ans == 3

    string = "bbbbb"
    ans = longest_substring_without_repeating_characters(string)

    assert ans == 1

    string = "pwwkew"
    ans = longest_substring_without_repeating_characters(string)

    assert ans == 3

    string = ""
    ans = longest_substring_without_repeating_characters(string)

    assert ans == 0



    
