from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    """
    Two strings are considered close if you can attain one from the other using the following operations:

    • Operation 1: Swap any two existing characters.
        • For example, abcde -> aecdb
    • Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        • For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
    You can use the operations on either string as many times as necessary.

    Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

    Example 1:
    Input: word1 = "abc", word2 = "bca"
    Output: true
    Explanation: You can attain word2 from word1 in 2 operations.
    Apply Operation 1: "abc" -> "acb"
    Apply Operation 1: "acb" -> "bca"

    Example 2:
    Input: word1 = "a", word2 = "aa"
    Output: false
    Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

    Example 3:
    Input: word1 = "cabbba", word2 = "abbccc"
    Output: true
    Explanation: You can attain word2 from word1 in 3 operations.
    Apply Operation 1: "cabbba" -> "caabbb"
    Apply Operation 2: "caabbb" -> "baaccc"
    Apply Operation 2: "baaccc" -> "abbccc"

    Example 4:
    Input: word1 = "cabbba", word2 = "aabbss"
    Output: false
    Explanation: It is impossible to attain word2 from word1, or vice versa, in any amount of operations.

    Constraints:
    • 1 <= word1.length, word2.length <= 10 ** 5
    • word1 and word2 contain only lowercase English letters.

    """
    assert 1 <= len(word1) <= 10 ** 5, "Length of word1 must be between 1 and 10 ** 5"
    assert 1 <= len(word2) <= 10 ** 5, "Length of word2 must be between 1 and 10 ** 5"
    assert word1 == word1.lower(), "word1 must contain only lowercase English letters"
    assert word2 == word2.lower(), "word2 must contain only lowercase English letters"

    word1_counter = Counter(word1)
    word2_counter = Counter(word2)

    if word1_counter == word2_counter:
        return True
    elif sorted(list(word1_counter.values())) == sorted(list(word2_counter.values())) and set(word1_counter.keys()) == set(word2_counter.keys()):
        return True
    return False


