


def longest_substring_without_repeating_characters(s: str) -> int:
    """
    Given a string `s`, find the length of the longest substring without repeating characters.

    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    Example 4:
    Input: s = ""
    Output: 0

    Constraints:
    • 0 <= s.length <= 5 * 104
    • s consists of English letters, digits, symbols and spaces.
    """
    assert 0 <= len(s) <= 5 * 104

    unique_substring = []
    substring = ""
    for character in s:
        if character not in list(substring):
            substring += character 
        else:
            unique_substring.append(substring)
            substring = character

    if unique_substring:
        return max(len(x) for x in unique_substring)
    else:
        return 0

