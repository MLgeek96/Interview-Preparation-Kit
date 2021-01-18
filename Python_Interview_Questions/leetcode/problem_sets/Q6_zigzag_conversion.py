def convert(s: str, numRows: int) -> str:
    """
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);

    Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

    Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

    Example 3:
    Input: s = "A", numRows = 1
    Output: "A"

    Constraints:
    • 1 <= s.length <= 1000
    • s consists of English letters (lower-case and upper-case), ',' and '.'.
    • 1 <= numRows <= 1000
    """
    assert 1 <= len(s) <= 1000, "Length of string must be strictly between 1 and 1000"
    assert 1 <= numRows <= 1000, "Number of rows must be between 1 and 1000"

    if numRows == 1: # base case
        return s
    ans = [[] for _ in range(numRows)]
    n = len(s)
    counter = 0
    sign = -1
    for i in range(n):
        if counter == numRows - 1 or counter == 0:
            sign *= -1
        ans[counter].append(s[i])
        counter += sign

    for index, char_list in enumerate(ans):
        ans[index] = "".join([char for char in char_list])

    return "".join([x for x in ans])
