def trailingZeroes(n: int) -> int:
    """
    Given an integer n, return the number of trailing zeroes in n!.

    Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

    Example 1:
    Input: n = 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.

    Example 2:
    Input: n = 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.

    Example 3:
    Input: n = 0
    Output: 0
    
    Constraints:
    • 0 <= n <= 10 ** 4
    """
    assert 0 <= n <= 10 ** 4, "n must be between 0 and 10 ** 4"

    numFactorFive = 0
    for num in range(1, n + 1):
        while num % 5 == 0:
            numFactorFive += 1
            num //=  5
    return numFactorFive