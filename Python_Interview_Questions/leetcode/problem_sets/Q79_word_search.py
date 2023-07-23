from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    """
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

    Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

    Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true

    Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false
    
    Constraints:
    • m == board.length
    • n = board[i].length
    • 1 <= m, n <= 6
    • 1 <= word.length <= 15
    • board and word consists of only lowercase and uppercase English letters.
    """
    assert 1 <= len(board) <= 6
    for i in range(len(board)):
        assert 1 <= len(board[i]) <= 6
    assert 1 <= len(word) <= 15
    
    seen = set()
    def backtrack(rowIdx, colIdx, i):
        if i == len(word):
            return True
        if rowIdx < 0 or colIdx < 0 or rowIdx >= len(board) or colIdx >= len(board[0]) or word[i] != board[rowIdx][colIdx] or (rowIdx, colIdx) in seen:
            return False
        
        seen.add((rowIdx, colIdx))
        res = (backtrack(rowIdx + 1, colIdx, i + 1) or backtrack(rowIdx - 1, colIdx, i + 1) or backtrack(rowIdx, colIdx + 1, i + 1) or backtrack(rowIdx, colIdx - 1, i + 1))
        seen.remove((rowIdx, colIdx))
        return res

    for i in range(len(board)):
        for j in range(len(board[i])):
            if backtrack(i, j, 0):
                return True
    return False