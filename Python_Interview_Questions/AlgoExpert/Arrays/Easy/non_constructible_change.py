from typing import List

def nonConstructibleChange(coins: List[int]):
    """
    Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minumum sum of money) that you cannot create. The given coins can have any positive integer value and aren't necessarily unique (i.e. you can have multiple coins of the same value).

    For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4. If you're given no coins, the minimum amount of change that you can't create is 1.

    Sample Input:
    coins = [5, 7, 1, 1, 2, 3, 22]

    Smaple Output:
    20

    Hints:
    1. One approach to solve this problem is to attempt to create every single amount of change, starting at 1 and going up until you eventually can't create an amount. While this approach works, there is a better one.

    2. Start by sorting the input array. SInce you're trying to find the minimum amount of change that you can't create, it makes sense to consider the smallest coins first.

    3. To understand the trick to this problem, consider the following example: coins = [1, 2, 4]. With this set of coins, we can create create 1, 2, 3, 4, 5, 6, 7 cents worth of change. Now, if we were to add a coin of value 9 to this set, we would not be able to create 8 cents. However, if we were to add a coin of value 7, we would be able to create 8 cents, and we would also be able to create all values of change from 1 to 15. Why is this the case?

    4. Create a variable to store the amount of change that you can currently create up to. Sort all your coins, and loop through them in ascending order. At every iteration, compare the current coin to the amount of change that you can currently create up to. Here are the two scenarios that you'll encounter. 
        * The coin value is greater than the amount of change that you can currently create plus 1
        * The coin value is smaller than or equal to the amount of change that you can currently create plus 1
       In the first scenario, you can simply return the current amount of change that you can create plus 1, because you can't create that amount of change. In the second scenario, you add the value of the coin to the amount of change that you can currently create up to, and you continue iterating through coins. The reason for that is that, if you're in the second scenario, you can create all of the values of change that you can currently create plus the value of the coin that you just considered. If you're given coins [1, 2], then you can make 1, 2,3 cents. So if you add a coin of value 4, then you can make 4 + 1 cents, 4 + 2 cents, and 4 + 3 cents. Thus, you can make up to 7 cents

    Optimal Space & Time Complexity:
    O(nlogn) time | O(1) space - where n is the number of coins
    """
    coins.sort()

    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    return currentChangeCreated + 1

if __name__ == "__main__":
    coins = [5, 7, 1, 1, 2, 3, 22]
    assert nonConstructibleChange(coins) == 20
    
    coins = [1, 1, 1, 1, 1]
    assert nonConstructibleChange(coins) == 6

    coins = [1, 5, 1, 1, 1, 10, 15, 20, 100]
    assert nonConstructibleChange(coins) == 55

    coins = [6, 4, 5, 1, 1, 8, 9]
    assert nonConstructibleChange(coins) == 3

    coins = []
    assert nonConstructibleChange(coins) == 1

    coins = [87]
    assert nonConstructibleChange(coins) == 1

    coins = [5, 6, 1, 1, 2, 3, 4, 9]
    assert nonConstructibleChange(coins) == 32

    coins = [5, 6, 1, 1, 2, 3, 43]
    assert nonConstructibleChange(coins) == 19

    coins = [1, 1]
    assert nonConstructibleChange(coins) == 3

    coins = [2]
    assert nonConstructibleChange(coins) == 1

    coins =  [1]
    assert nonConstructibleChange(coins) == 2

    coins = [109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]
    assert nonConstructibleChange(coins) == 87

    coins = [1, 2, 3, 4, 5, 6, 7]
    assert nonConstructibleChange(coins) == 29