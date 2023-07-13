import pytest
from leetcode.problem_sets.Q122_best_time_to_buy_and_sell_stock_ii import maxProfit

print(maxProfit.__doc__)

def test_maxProfit():
    prices = [7,1,5,3,6,4]
    assert maxProfit(prices) == 7

    prices = [1,2,3,4,5]
    assert maxProfit(prices) == 4

    prices = [7,6,4,3,1]
    assert maxProfit(prices) == 0