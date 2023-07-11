from typing import List

def maxPoints(points: List[List[int]]) -> int:
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

    Example 1:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: 3

    Example 2:
    Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4

    Constraints:
    • 1 <= points.length <= 300
    • points[i].length == 2
    • -10 ** 4 <= xi, yi <= 10 ** 4
    • All the points are unique.    
    """
    assert 1 <= len(points) <= 300, "Length of points must be between 1 and 300"
    for point in points:
        assert len(point) == 2, "points[i] = [xi, yi]"
        assert -10 ** 4 <= point[0] <= 10 ** 4
        assert -10 ** 4 <= point[1] <= 10 ** 4

    maxPoint = 1
    for i in range(len(points)):
        slopeDict = {}
        for j in range(i + 1, len(points)):
            if points[j][0] == points[i][0]:
                slope = float("inf")
            else:
                slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
            if slope in slopeDict:
                slopeDict[slope] += 1
            else:
                slopeDict[slope] = 1

            maxPoint = max(maxPoint, 1 + slopeDict[slope])
    return maxPoint