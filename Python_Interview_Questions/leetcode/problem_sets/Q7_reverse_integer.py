def reverse(x: int) -> int:
    """
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

    Example 1:
    Input: x = 123
    Output: 321

    Example 2:
    Input: x = -123
    Output: -321

    Example 3:
    Input: x = 120
    Output: 21

    Example 4:
    Input: x = 0
    Output: 0

    Constraints:
    • -2 ** 31 <= x <= 2 ** 31 - 1
    """
    if x >= 0:
        str_x = str(x)
        ans = int(str_x[::-1])
    else:
        str_x = str(x).lstrip("-")
        rev_str_x = str_x[::-1]
        ans = int(rev_str_x) * -1
    if (ans < -2 ** 31) or (ans > 2 ** 31 - 1):
        return 0
    else:
        return ans