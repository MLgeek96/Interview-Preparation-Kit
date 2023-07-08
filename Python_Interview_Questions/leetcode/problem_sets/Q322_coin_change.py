from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.

    Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

    Example 2:
    Input: coins = [2], amount = 3
    Output: -1

    Example 3:
    Input: coins = [1], amount = 0
    Output: 0
    
    Constraints:
    • 1 <= coins.length <= 12
    • 1 <= coins[i] <= 2 ** 31 - 1
    • 0 <= amount <= 10 ** 4
    """
    assert 1 <= len(coins) <= 12, "Length of coins must be between 1 and 12"
    for coin in coins:
        assert 1 <= coin <= 2 ** 31 - 1, "Coin must be between 1 and 2 ** 31 - 1"
    assert 0 <= amount <= 10 ** 4, "Amount must be between 0 and 10 ** 4" 

    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[-1] if dp[-1] != float('inf') else -1