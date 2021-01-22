def mySqrt(x: int) -> int:
    """
    Given a non-negative integer x, compute and return the square root of x.

    Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

    Example 1:
    Input: x = 4
    Output: 2

    Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

    Constraints:
    • 0 <= x <= 2 ** 31 - 1
    """
    assert 0 <= x <= 2 ** 31 - 1, "Input integer must be between 0 and 2 ** 31 - 1"

    if x < 2:
        return x

    left_pointer = 0
    right_pointer = x

    while left_pointer < right_pointer:
        mid_pointer = left_pointer + (right_pointer - left_pointer) // 2

        if x == mid_pointer ** 2:
            return mid_pointer
        elif x < mid_pointer ** 2:
            right_pointer = mid_pointer
        elif x > mid_pointer ** 2:
            left_pointer = mid_pointer + 1

    return left_pointer - 1
