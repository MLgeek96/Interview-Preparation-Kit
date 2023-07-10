import re

def isAnagram(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:
    Input: s = "rat", t = "car"
    Output: false
    
    Constraints:
    • 1 <= s.length, t.length <= 5 * 10 ** 4
    • s and t consist of lowercase English letters.

    Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
    """
    assert 1 <= len(s) <= 5 * 10 ** 4, "Length of s must be between 1 and 5 * 10 ** 4"
    assert 1 <= len(t) <= 5 * 10 ** 4, "Length of t must be between 1 and 5 * 10 ** 4"
    assert re.search('[a-z]', s), "s must consist of lowercase English letters"
    assert re.search('[a-z]', t), "t must consist of lowercase English letters"

    sDict = {}
    for sChar in s:
        if sChar not in sDict:
            sDict[sChar] = 1
        else:
            sDict[sChar] += 1

    for tChar in t:
        if tChar not in sDict:
            return False
        else:
            sDict[tChar] -= 1

    return list(set(sDict.values())) == [0] and len(s) == len(t)
