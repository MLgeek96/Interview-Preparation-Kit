import pytest
from leetcode.problem_sets.Q322_coin_change import coinChange

print(coinChange.__doc__)

def test_coinChange():
    coins = [1,2,5]
    amount = 11
    assert coinChange(coins, amount) == 3

    coins = [2]
    amount = 3
    assert coinChange(coins, amount) == -1
    
    
    coins = [1]
    amount = 0
    assert coinChange(coins, amount) == 0