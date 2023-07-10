
def isIsomorphic(s: str, t: str) -> bool:
    """
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

    Example 1:
    Input: s = "egg", t = "add"
    Output: true

    Example 2:
    Input: s = "foo", t = "bar"
    Output: false

    Example 3:
    Input: s = "paper", t = "title"
    Output: true
    
    Constraints:
    • 1 <= s.length <= 5 * 10 ** 4
    • s and t consist of any valid ascii character.
    • t.length == s.length
    """
    assert 1 <= len(s) <= 5 * 10 ** 4, "Length of s must be between 1 and 5 * 10 ** 4"
    assert len(t) == len(s), "Length of t and s must be the same"
    
    sDict = {}
    tDict = {}
    for sChar, tChar in zip(s, t):
        if (sChar in sDict and sDict[sChar] != tChar) or (tChar in tDict and tDict[tChar] != sChar):
            return False
        sDict[sChar] = tChar
        tDict[tChar] = sChar
    return True
