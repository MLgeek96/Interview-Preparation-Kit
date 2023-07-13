import pytest
from leetcode.problem_sets.Q121_best_time_to_buy_and_sell_stock import maxProfit

print(maxProfit.__doc__)

def test_maxProfit():
    prices = [7,1,5,3,6,4]
    assert maxProfit(prices) == 5

    prices = [7,6,4,3,1]
    assert maxProfit(prices) == 0