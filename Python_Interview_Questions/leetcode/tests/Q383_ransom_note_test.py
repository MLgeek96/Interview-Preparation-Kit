import pytest
from leetcode.problem_sets.Q383_ransom_note import canConstruct

print(canConstruct.__doc__)

def test_canConstruct():
    ransomNote = "a"
    magazine = "b"

    assert canConstruct(ransomNote, magazine) == False

    ransomNote = "aa"
    magazine = "ab"

    assert canConstruct(ransomNote, magazine) == False

    ransomNote = "aa"
    magazine = "aab"

    assert canConstruct(ransomNote, magazine) == True