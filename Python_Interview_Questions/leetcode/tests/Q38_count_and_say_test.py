import pytest
from leetcode.problem_sets.Q38_count_and_say import countAndSay

def test_count_and_say():
    assert countAndSay(1) == "1"
    assert countAndSay(4) == "1211"