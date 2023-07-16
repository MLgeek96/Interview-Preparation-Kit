from typing import List

def generateParenthesis(n: int) -> List[str]:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:
    Input: n = 1
    Output: ["()"]
    
    Constraints:
    • 1 <= n <= 8
    """
    assert 1 <= n <= 8

    def backtrack(left, right, s):
        if len(s) == n * 2:
            resultList.append(s)
        
        if left < n:
            backtrack(left + 1, right, s + "(")

        if right < left:
            backtrack(left, right + 1, s + ")")

    resultList = []
    backtrack(0, 0, "")

    return resultList

