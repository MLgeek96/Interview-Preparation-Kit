def addBinary(a: str, b: str) -> str:
    """
    Given two binary strings a and b, return their sum as a binary string.

    Example 1:
    Input: a = "11", b = "1"
    Output: "100"

    Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

    Constraints:
    • 1 <= a.length, b.length <= 10 ** 4
    • a and b consist only of '0' or '1' characters.
    • Each string does not contain leading zeros except for the zero itself.
    """
    assert 1 <= len(a) <= 10 ** 4, "Length of a must be between 1 and 10 ** 4"
    assert 1 <= len(b) <= 10 ** 4, "Length of b must be between 1 and 10 ** 4"
    for character in a:
        assert character in ['1', '0'], "a should consist only of '0' or '1' characters"
    for character in b:
        assert character in ['1', '0'], "b should consist only of '0' or '1' characters"

    integer_sum = int(a, 2) + int(b, 2)
    binary_sum = bin(integer_sum)
    return binary_sum[2:]

