import re

def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

    Each letter in magazine can only be used once in `ransomNote`.

    Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

    Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

    Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true
    
    Constraints:
    • 1 <= ransomNote.length, magazine.length <= 10 ** 5
    • ransomNote and magazine consist of lowercase English letters.

    """
    assert 1 <= len(ransomNote) <= 10 ** 5, "ransomNote string must contains between 1 and 10 ** 5 characters"
    assert 1 <= len(magazine) <= 10 ** 5, "magazine string must contains between 1 and 10 ** 5 characters"
    
    assert re.search('[a-z]', ransomNote), "ransomNote should consist of only lowercase English letters"
    assert re.search('[a-z]', magazine), "magazine should consist of only lowercase English letters"

    # ransomNoteDict = {}
    # for char in ransomNote:
    #     ransomNoteDict[char] = ransomNoteDict.get(char, 0) + 1
    
    # magazineDict = {}
    # for char in magazine:
    #     magazineDict[char] = magazineDict.get(char, 0) + 1

    # for key in ransomNoteDict:
    #     if key not in magazineDict.keys(): return False
    #     if ransomNoteDict[key] > magazineDict[key]: return False
    # return True

    for char in set(ransomNote):
        if ransomNote.count(char) > magazine.count(char): return False
    return True