from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string ""

    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

    Constraints:
    • 0 <= strs.length <= 200
    • 0 <= strs[i].length <= 200
    • strs[i] consists of only lower-case English letters.
    """
    assert 0 <= len(strs) <= 200, "Length of string must be between 0 and 200"
    for str in strs:
        assert 0 <= len(str) <= 200, "Length of string in list must be between 0 and 200"
        assert str == str.lower(), "String should consists of only lower-case English letters"

    result = ''
    for tuple_character in zip(*strs):
        if min(tuple_character) == max(tuple_character):
            result += tuple_character[0]
        else:
            break

    return result

