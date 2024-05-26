from typing import List

def transposeMatrix(matrix: List[List[int]]):
    """
    You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix.

    The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top left to bottom right); it switches the row and column indices of the original matrix.

    You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.

    Smaple Input #1:
    matrix = [
        [1, 2]
    ]

    Sample Output #1:
    [
        [1],
        [2]
    ]

    Sample Input #2:
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    Sample Output #2:
    [
        [1, 3, 5],
        [2, 4, 6]
    ]

    Sample Input #3:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    Sample Output #3:
    [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]

    Hints:
    1. The row and column indices of each enry in the matrix should be flipped. For example, the value at matrix[1][2] will be at matrix[2][1] in the transpose of the matrix.

    2. Each column in the matrix should become a row in the transpose of the matrix. Each row in the matrix should become a column in the transpose of the matrix.

    3. Try iterating one column at a time, and with each column, create a row of the values to add to the transpose of the matrix.


    Optimal Space & Time Complexity:
    O(w*h) time | O(w*h) space - where w is the width of the matrix and h is the height
    """
    # O(w*h) time | O(w*h) space
    transposedMatrix = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transposedMatrix.append(newRow)
    return transposedMatrix

    num_rows, num_cols = len(matrix), len(matrix[0])
    transposedMatrix = [[None for _ in range(num_rows)] for _ in range(num_cols)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transposedMatrix[j][i] = matrix[i][j]
    return transposedMatrix

if __name__ == "__main__":
    matrix = [
        [1]
    ]
    assert transposeMatrix(matrix) == [[1]]

    matrix = [
        [1],
        [-1]
    ]
    assert transposeMatrix(matrix) == [[1, -1]]

    matrix = [
        [1, 2, 3]
    ]
    assert transposeMatrix(matrix) == [[1], [2], [3]]

    matrix = [
        [1],
        [2],
        [3]
    ]
    assert transposeMatrix(matrix) == [[1, 2, 3]]

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert transposeMatrix(matrix) == [[1, 4], [2, 5], [3, 6]]

    matrix = [
        [0, 0, 0],
        [1, 1, 1]
    ]
    assert transposeMatrix(matrix) == [[0, 1], [0, 1], [0, 1]]

    matrix = [
        [0, 1],
        [0, 1],
        [0, 1]
    ]
    assert transposeMatrix(matrix) == [[0, 0, 0], [1, 1, 1]]

    matrix = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert transposeMatrix(matrix) == [[0, 0], [0, 0], [0, 0]]

    matrix = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]
    assert transposeMatrix(matrix) == [[1, 2, 3], [4, 5, 6]]

    matrix = [
        [-7, -7],
        [100, 12],
        [-33, 17]
    ]
    assert transposeMatrix(matrix) == [[-7, 100, -33], [-7, 12, 17]]

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert transposeMatrix(matrix) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    matrix = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    assert transposeMatrix(matrix) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    matrix = [
        [5, 6, 3, -3, 12],
        [-3, 6, 5, 2, -1],
        [0, 0, 3, 12, 3]
    ]
    assert transposeMatrix(matrix) == [[5, -3, 0], [6, 6, 0], [3, 5, 3], [-3, 2, 12], [12, -1, 3]]

    matrix = [
        [0, -1, -2, -3],
        [4, 5, 6, 7],
        [2, 3, -2, -3],
        [42, 100, 30, -42]
    ]
    assert transposeMatrix(matrix) == [[0, 4, 2, 42], [-1, 5, 3, 100], [-2, 6, -2, 30], [-3, 7, -3, -42]]

    matrix = [
        [1234, 6935, 4205],
        [-23459, 314159, 0],
        [100, 3, 987654]
    ]
    assert transposeMatrix(matrix) == [[1234, -23459, 100], [6935, 314159, 3], [4205, 0, 987654]]