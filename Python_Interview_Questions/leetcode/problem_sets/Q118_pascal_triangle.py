from typing import List

def generate(numRows: int) -> List[List[int]]:
    """
    Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

    Example 1:
    Input: 5
    Output:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
    """

    result = [[] for _ in range(numRows)]
    for i in range(numRows):
        for j in range(i + 1):
            if j == 0 or j == i:
                result[i].append(1)
            else:
                result[i].append(result[i-1][j-1] + result[i-1][j])

    return result
