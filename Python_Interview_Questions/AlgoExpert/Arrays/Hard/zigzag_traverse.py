from typing import List

def zigzagTraverse(array: List[List[int]]):
    """
    Write a function that takes in an n x m two-dimensional array (that can be square-shaped where n == m), and returns a one-dimensional array of all the array's elements in zigzag order.

    Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element, and proceeds in a zigzag pattern all the way to the bottom right corner.

    Sample Input:
    ```
    array = [
        [1, 3, 4, 10], 
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16]
    ]
    ```

    Sample Output:
    ```
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    ```

    Hints:
    1. Don't overthink this question by trying to come up with a clever way of getting the zigzag order. Think about the simplest checks that need to be made to decide when and how to change direction throughout the zigzag traversal.
    2. Starting at the top left corner, iterate through the two-dimensional array by keeping track of the direction that you're moving in (up or down). If you're moving up, you know that you need to move in an up-right pattern and that you need to handle the case where you hit the otp or the right borders of the array. If you're moving down, you know that you need to move in a down-left pattern and that you need to handle the case where you hit the left or the bottom borders of the array.
    3. When going up, if you hit the right border, you'll have to go down one element; if you hit the top border, you'll have to go right one element. Similarly, when going down, if you hit the left border, you'll have to go down one element; if you hit the bottom border, you'll have to go right one element.

    Optimal Space & Time Complexity
    O(n) time | O(n) space - where n is the total number of elements in the two-dimensional array
    """
    def isOutOfBounds(row, col, height, width):
        return row < 0 or row > height or col < 0 or col > width

    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row = col = 0 
    goingDown = True 
    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False 
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True 
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result 

if __name__ == "__main__":
    array = [
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16]
    ]
    assert zigzagTraverse(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    array = [
        [1]
    ]
    assert zigzagTraverse(array) == [1]

    array = [
        [1, 2, 3, 4, 5]
    ]
    assert zigzagTraverse(array) == [1, 2, 3, 4, 5]

    array = [
        [1],
        [2],
        [3],
        [4],
        [5]
    ]
    assert zigzagTraverse(array) == [1, 2, 3, 4, 5]

    array = [
        [1, 3],
        [2, 4],
        [5, 7],
        [6, 8],
        [9, 10]
    ]
    assert zigzagTraverse(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    array = [
        [1, 3, 4, 7, 8],
        [2, 5, 6, 9, 10]
    ]
    assert zigzagTraverse(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    array = [
        [1, 3, 4, 10, 11],
        [2, 5, 9, 12, 19],
        [6, 8, 13, 18, 20],
        [7, 14, 17, 21, 24],
        [15, 16, 22, 23, 25]
    ]
    assert zigzagTraverse(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    array = [
        [1, 3, 4, 10, 11, 20],
        [2, 5, 9, 12, 19, 21],
        [6, 8, 13, 18, 22, 27],
        [7, 14, 17, 23, 26, 28],
        [15, 16, 24, 25, 29, 30]
    ]
    assert zigzagTraverse(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    array = [
        [1, 3, 4, 10, 11],
        [2, 5, 9, 12, 20],
        [6, 8, 13, 19, 21],
        [7, 14, 18, 22, 27],
        [15, 17, 23, 26, 28],
        [16, 24, 25, 29, 30]
    ]
    assert zigzagTraverse(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    array = [
        [1, 21, -3, 4, 15, 6, -7, 88, 9],
        [10, 11, 112, 12, 20, -1, -2, -3, -4],
        [6, 8, 113, 19, 21, 0, 0, 0, 0],
        [7, 2, 18, 22, -27, 12, 32, -111, 66],
        [15, 17, 23, 226, 28, -28, -226, -23, -17],
        [16, 24, 27, 299, 30, 29, 32, 31, 88]
    ]
    assert zigzagTraverse(array) == [1, 10, 21, -3, 11, 6, 7, 8, 112, 4, 15, 12, 113, 2, 15, 16, 17, 18, 19, 20, 6, -7, -1, 21, 22, 23, 24, 27, 226, -27, 0, -2, 88, 9, -3, 0, 12, 28, 299, 30, -28, 32, 0, -4, 0, -111, -226, 29, 32, -23, 66, -17, 31, 88]