def longestPalindrome(s: str) -> str:
    """
    Given a string s, return the longest palindromic substring in s.

    Example 1:
    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Example 2:
    Input: s = "cbbd"
    Output: "bb"

    Example 3:
    Input: s = "a"
    Output: "a"

    Example 4:
    Input: s = "ac"
    Output: "a"

    Constraints:
    • 1 <= s.length <= 1000
    • s consist of only digits and English letters (lower-case and/or upper-case),

    """

    def validate_palindrome(left_index: int, right_index: int) -> str:
        while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
            left_index -= 1
            right_index += 1

        return s[left_index+1: right_index]

    longest_palindrome = ""
    for i in range(len(s)):
        # for palindrome with odd length
        palindrome = validate_palindrome(i, i)
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome
        # for palindrome with even length
        palindrome = validate_palindrome(i, i + 1)
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome
    return longest_palindrome


