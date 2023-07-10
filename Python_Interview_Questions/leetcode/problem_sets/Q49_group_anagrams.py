from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Example 2:
    Input: strs = [""]
    Output: [[""]]

    Example 3:
    Input: strs = ["a"]
    Output: [["a"]]
    
    Constraints:
    • 1 <= strs.length <= 10 ** 4
    • 0 <= strs[i].length <= 100
    • strs[i] consists of lowercase English letters.
    
    """
    assert 1 <= len(strs) <= 10 ** 4, "Length of strs must be between 1 and 10 ** 4"
    for string in strs:
        assert 0 <= len(string) <= 100, "Length of str in strs must be between 0 and 100"

    resultDict = {}

    for string in strs:
        charDict = {}
        for char in string:
            if char in charDict:
                charDict[char] += 1
            else:
                charDict[char] = 1

        resStr = ""
        for char in sorted(charDict):
            resStr += char + str(charDict[char])

        if resStr not in resultDict:
            resultDict[resStr] = [string]
        else:
            resultDict[resStr].append(string) 

    return sorted(list(resultDict.values()), key=len)