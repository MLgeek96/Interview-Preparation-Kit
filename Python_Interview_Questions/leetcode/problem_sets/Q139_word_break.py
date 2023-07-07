import re
from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    """
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.

    Example 1:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

    Example 2:
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

    Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false
    
    Constraints:
    • 1 <= s.length <= 300
    • 1 <= wordDict.length <= 1000
    • 1 <= wordDict[i].length <= 20
    • s and wordDict[i] consist of only lowercase English letters.
    • All the strings of wordDict are unique.
    """
    assert 1 <= len(s) <= 300, "Length of s must be between 1 and 300"
    assert 1 <= len(wordDict) <= 1000, "Length of wordDict must be between 1 and 1000"
    assert re.search("[a-z]", s), "s must consist of only lowercase English letters"
    for word in wordDict:
        assert 1 <= len(word) <= 20, "Length of word in wordDict must be between 1 and 20"
        assert re.search("[a-z]", word), "word in wordDict must consist of only lowercase English letters"
    assert len(wordDict) == len(set(wordDict)), "All the strings in wordDict must be unique"

    dp = [False for _ in range(len(s) + 1)]
    dp[-1] = True

    for i in reversed(range(len(s))):
        for word in wordDict:
            if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                dp[i] = dp[i+len(word)]
            if dp[i]:
                break
    return dp[0]
