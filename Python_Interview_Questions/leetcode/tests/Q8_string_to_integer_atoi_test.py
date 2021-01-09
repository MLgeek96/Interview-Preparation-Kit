import pytest
from leetcode.problem_sets.Q8_string_to_integer_atoi import myAtoi

def test_string_to_integer_atoi():
    string_input = "42"
    ans = myAtoi(string_input)

    assert ans == 42

    string_input = "   -42"
    ans = myAtoi(string_input)

    assert ans == -42

    string_input = "4193 with words"
    ans = myAtoi(string_input)

    assert ans == 4193

    string_input = "words and 987"
    ans = myAtoi(string_input)

    assert ans == 987

    string_input = "-91283472332"
    ans = myAtoi(string_input)

    assert ans == -2147483648

    string_input = "+-12"
    ans = myAtoi(string_input)

    assert ans == 0

    string_input = "3.1415"
    ans = myAtoi(string_input)

    assert ans == 3





