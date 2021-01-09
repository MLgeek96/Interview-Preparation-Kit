def isPalindrome(x: int) -> bool:
    """
    Determine whether an integer is a palindrome.
    An integer is a palindrome when it reads the same backward as forward.

    Follow up: Could you solve it without converting the integer to a string?

    Example 1:
    Input: x = 121
    Output: true

    Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121.
    From right to left, it becomes 121-.
    Therefore it is not a palindrome.

    Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Example 4:
    Input: x = -101
    Output: false

    Constraints:
    • -2 ** 31 <= x <= 2 ** 31 - 1

    """

    assert -2 ** 31 <= x <= 2 ** 31 - 1, "Given integer is out of bound"

    if x < 0:
        return False
    int_input = x
    reverse_int = 0
    while int_input != 0:
        reverse_int = reverse_int * 10 + int_input % 10
        int_input = int_input // 10

    return True if reverse_int == x else False
