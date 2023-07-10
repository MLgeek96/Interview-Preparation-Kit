import re

def wordPattern(pattern: str, s: str) -> bool:
    """
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

    Example 1:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true

    Example 2:
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false

    Example 3:
    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false

    Constraints:
    • 1 <= pattern.length <= 300
    • pattern contains only lower-case English letters.
    • 1 <= s.length <= 3000
    • s contains only lowercase English letters and spaces ' '.
    • s does not contain any leading or trailing spaces.
    • All the words in s are separated by a single space.
    """
    assert 1 <= len(pattern) <= 300, "Length of pattern must be between 1 and 300"
    assert re.search('[a-z]', pattern), "pattern contains only lower-case English letters"
    assert 1 <= len(s) <= 3000, "Length of s must be between 1 and 3000"
    assert re.search('[a-z ]', s), "s contains only lowercase English letters and spaces ' '"
    assert s == s.lstrip() == s.rstrip(), "s does not contain any leading or trailing spaces"

    s = s.split(' ')
    return len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s))) and len(pattern) == len(s)