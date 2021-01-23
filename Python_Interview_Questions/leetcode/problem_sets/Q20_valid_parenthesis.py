def isValid(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

    Example 1:
    Input: s = "()"
    Output: true

    Example 2:
    Input: s = "()[]{}"
    Output: true

    Example 3:
    Input: s = "(]"
    Output: false

    Example 4:
    Input: s = "([)]"
    Output: false

    Example 5:
    Input: s = "{[]}"
    Output: true

    Constraints:
    • 1 <= s.length <= 10 ** 4
    • s consists of parentheses only '()[]{}'.
    """
    assert 1 <= len(s) <= 10 ** 4, "Length of string must be between 1 and 10 ** 4"
    for character in s:
        assert character in ['(', ')', '[', ']', '{', '}']

    track_left_bracket = []
    bracket_dict = {'(': ')', '[': ']', '{': '}'}

    for bracket in s:
        if bracket in bracket_dict.keys():
            track_left_bracket.append(bracket)
        elif len(track_left_bracket) == 0 or bracket_dict[track_left_bracket.pop()] != bracket:
            return False
    return True if len(track_left_bracket) == 0 else False
