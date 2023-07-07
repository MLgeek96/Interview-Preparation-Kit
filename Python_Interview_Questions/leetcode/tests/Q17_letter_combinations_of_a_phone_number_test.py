import pytest
from leetcode.problem_sets.Q17_letter_combinations_of_a_phone_number import letterCombinations

def test_letter_combinations_of_a_phone_number():
    digits = "23"
    assert letterCombinations(digits) == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    digits = ""
    assert letterCombinations(digits) == []

    digits = "2"
    assert letterCombinations(digits) == ["a", "b", "c"]