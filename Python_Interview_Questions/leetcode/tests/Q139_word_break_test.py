import pytest
from leetcode.problem_sets.Q139_word_break import wordBreak

print(wordBreak.__doc__)

def test_wordBreak():
    s = "leetcode"
    wordDict = ["leet","code"]
    assert wordBreak(s, wordDict) == True

    s = "applepenapple"
    wordDict = ["apple","pen"]
    assert wordBreak(s, wordDict) == True

    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    assert wordBreak(s, wordDict) == False