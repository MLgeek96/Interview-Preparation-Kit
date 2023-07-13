import pytest
from leetcode.problem_sets.Q151_reverse_words_in_a_string import reverseWords

print(reverseWords.__doc__)

def test_reverseWords():
    s = "the sky is blue"
    assert reverseWords(s) == "blue is sky the"

    s = "  hello world  "
    assert reverseWords(s) == "world hello"

    s = "a good   example"
    assert reverseWords(s) == "example good a"