from typing import List

def spiralTraverse(array: List[List[int]]):
    """
    Write a function that takes in an n x m two-dimensional array ( that can be square-shaped where n == m ) and returns a one-dimensional array of all the array's elements in spiral order.

    Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in spiral pattern all the way until every element has been visited.

    Sample Input:
    ```
    array = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ]
    ```

    Sample Output:
    ```
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    ```

    Hints:
    1. You can think of the spiral that you have to traverse as a set of rectangle perimeters that progressively get smaller (i.e., that progressively move inwards in the two-dimensional array).
    2. Going off of Hint #1, declare four variables; a starting row, a starting column, an ending row, and an ending column. These four variables represent the bounds of the first rectangle perimeter in the spiral that you have to traverse. Traverse that perimeter using those bounds, and then move the bounds inwards. End your algorithm once the starting row passes the ending row or the starting column passes the ending column.
    3. You can solve this problem both iteratively and recursively following very similar logic.

    Optimal Space & Time Complexity
    O(n) time | O(n) space - where n is the total number of elements in the array
    """
    # O(n) time | O(n) space - where n is the total number of elements in the array
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
        
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break 
            result.append(array[endRow][col])
        
        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break 
            result.append(array[row][startCol])
        
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result 

    # O(n) time | O(n) space - where n is the total number of elements in the array
    result = []
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result 

    def spiralFill(array, startRow, endRow, startCol, endCol, result):
        if startRow > endRow or startCol > endCol:
            return 

        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
            
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break 
            result.append(array[endRow][col])
        
        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break 
            result.append(array[row][startCol])
        
        spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)

if __name__ == "__main__":
    array = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ]
    assert spiralTraverse(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    array = [
        [1]
    ]
    assert spiralTraverse(array) == [1]

    array = [
        [1, 2],
        [4, 3]
    ]
    assert spiralTraverse(array) == [1, 2, 3, 4]

    array = [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ]
    assert spiralTraverse(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    array = [
        [19, 32, 33, 34, 25, 8],
        [16, 15, 14, 13, 12, 11],
        [18, 31, 36, 35, 26, 9],
        [1, 2, 3, 4, 5, 6],
        [20, 21, 22, 23, 24, 7],
        [17, 30, 29, 28, 27, 10]
    ]
    assert spiralTraverse(array) == [19, 32, 33, 34, 25, 8, 11, 9, 6, 7, 10, 27, 28, 29, 30, 17, 20, 1, 18, 16, 15, 14, 13, 12, 26, 5, 24, 23, 22, 21, 2, 31, 36, 35, 4, 3]

    array = [
        [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
        [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]
    ]
    assert spiralTraverse(array) == [4, 2, 3, 6, 7, 8, 1, 9, 5, 10, 14, 11, 17, 13, 18, 20, 16, 15, 19, 12]

    array = [
        [27, 12, 35, 26],
        [25, 21, 94, 11],
        [19, 96, 43, 56],
        [55, 36, 10, 18],
        [96, 83, 31, 94],
        [93, 11, 90, 16]
    ]
    assert spiralTraverse(array) == [27, 12, 35, 26, 11, 56, 18, 94, 16, 90, 11, 93, 96, 55, 19, 25, 21, 94, 43, 10, 31, 83, 36, 96]

    array = [
        [1, 2, 3, 4],
        [10, 11, 12, 5],
        [9, 8, 7, 6]
    ]
    assert spiralTraverse(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    array = [
        [1, 2, 3],
        [12, 13, 4],
        [11, 14, 5],
        [10, 15, 6],
        [9, 8, 7]
    ]
    assert spiralTraverse(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    array = [
        [1, 11],
        [2, 12],
        [3, 13],
        [4, 14],
        [5, 15],
        [6, 16],
        [7, 17],
        [8, 18],
        [9, 19],
        [10, 20]
    ]
    assert spiralTraverse(array) == [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    array = [
        [1, 3, 2, 5, 4, 7, 6]
    ]
    assert spiralTraverse(array) == [1, 3, 2, 5, 4, 7, 6]

    array = [
        [1],
        [3],
        [2],
        [5],
        [4],
        [7],
        [6]
    ]
    assert spiralTraverse(array) == [1, 3, 2, 5, 4, 7, 6]