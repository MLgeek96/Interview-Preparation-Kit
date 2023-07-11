def myPow(x: float, n: int) -> float:
    """
    Implement pow(x, n), which calculates x raised to the power n (i.e., x ^ n).

    Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000

    Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100

    Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2 ^(-2) = 1/2^2 = 1/4 = 0.25
    
    Constraints:
    • -100.0 < x < 100.0
    • -2 ** 31 <= n <= 2 ** 31 - 1
    • n is an integer.
    • Either x is not zero or n > 0.
    """
    assert -100.0 < x < 100.0, "x must be between -100.0 and 100.0"
    assert -2 ** 31 <= n <= 2 ** 31 - 1, "n must be between -2 ** 31 and 2 ** 31 - 1"
    assert n == int(n), "n must be an integer"
    assert x != 0 or n > 0, "Either x is not zero or n > 0"

    def helper(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        res = helper(x * x, n // 2)
        return res * x if n % 2 != 0 else res
    
    ans = helper(x, abs(n))
    return ans if n >= 0 else 1 / ans