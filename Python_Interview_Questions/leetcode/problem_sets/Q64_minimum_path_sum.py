from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    """
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.

    Example 1:
    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7
    Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

    Example 2:
    Input: grid = [[1,2,3],[4,5,6]]
    Output: 12
    
    Constraints:
    • m == grid.length
    • n == grid[i].length
    • 1 <= m, n <= 200
    • 0 <= grid[i][j] <= 200
    """
    m = len(grid)
    n = len(grid[0])
    assert 1 <= m <= 200, "Length of grid must be between 1 and 200"
    assert 1 <= n <= 200, "Length of grid must be between 1 and 200"

    for i in range(m):
        for j in range(n):
            assert 0 <= grid[i][j] <= 200, "Number in grid must be between 0 and 200"

    result = grid
    for rowIdx in range(len(grid)):
        for colIdx in range(len(grid[rowIdx])):
            if rowIdx == 0 and colIdx == 0:
                continue
            elif rowIdx == 0 and colIdx > 0:
                result[rowIdx][colIdx] += result[rowIdx][colIdx - 1]
            elif rowIdx != 0 and colIdx == 0:
                result[rowIdx][colIdx] += result[rowIdx - 1][colIdx]
            else:
                result[rowIdx][colIdx] += min(result[rowIdx - 1][colIdx], result[rowIdx][colIdx - 1])
    return result[-1][-1]