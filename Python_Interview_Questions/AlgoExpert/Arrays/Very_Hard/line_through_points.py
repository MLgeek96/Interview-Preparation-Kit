
# O(n^2) time | O(n) space - where n is the number of points 
def lineThroughPoints(points):
    """
    You're given an array of points plotted on a 2D graph (the xy-plane). Write a function that returns the maximum number of points that a single line (or potentially multiple lines) on the graph passes through.

    The input array will contain points represented by an array of two integers [x, y]. The input array will never contain duplicate points and will always contain at least one point.

    Sample Input:
    ```
    points = [
        [1, 1],
        [2, 2],
        [3, 3],
        [0, 4],
        [2, -6],
        [4, 0], 
        [2, 1]
    ]
    ```

    Sample Output:
    ```
    4 // A line passes through points: [-2, -6], [0, 4], [2, 2], [4, 0]
    ```

    Hints: 
    1. The brute-force approach to solve this problem is to consider every single pair of points and to form a line using them. Then for each line, you determine how many points lie on that line by using the equation of the line you formed and checking if each point's coordinates solve the equation. This solution runs in O(n^3) timel can you come up with a better approach?
    2. What does it mean if two lines have the same slope and share a point?
    3. If two lines have the same slope and share a point, they're the same line. Try using a hash table to store the slopes of lines that pass through certain points. How does this help you write an algorithm that runs in O(n^2) time?
    4. Loop through every single pair of points, picking a p2 for every p1 in order to form a line. For every pair (p1, p2), store the slope of the formed line in a hash talbe, and map it to the number of points on that line. If you ever find two identical slopes for lines that both use the same point p1, you can consider these lines to be one and the same, meaning that points p1, p2a and p2b are all on the same line; in those cases, update the number of points on the slope (the line) in the hash table accordingly. You'll need to reset the hash table at each change of p1. 

    Optimal Space & Time Complexity
    O(n^2) time | O(n) space - where n is the number of points 
    """
    maxNumberOfPointsOnLine = 1
    for idx1, p1 in enumerate(points):
        slopes = {}
        for idx2 in range(idx1 + 1, len(points)):
            p2 = points[idx2]
            rise, run = getSlopeOfLineBetweenPoints(p1, p2)
            slopeKey = createHashableKeyForRational(rise, run)
            if slopeKey not in slopes:
                slopes[slopeKey] = 1
            slopes[slopeKey] += 1
        
        maxNumberOfPointsOnLine = max(maxNumberOfPointsOnLine, max(slopes.values(), default = 0))

    return maxNumberOfPointsOnLine

def getSlopeOfLineBetweenPoints(p1, p2):
    p1x, p1y = p1 
    p2x, p2y = p2 
    slope = [1, 0] # slope of a vertical line 

    if p1x != p2x: # if line is not vertical
        xDiff = p1x - p2x 
        yDiff = p1y - p2y 
        gcd = getGreatestCommonDivisor(abs(xDiff), abs(yDiff))
        xDiff = xDiff // gcd 
        yDiff = yDiff // gcd 
        if xDiff < 0:
            xDiff *= -1 
            yDiff *= -1 
        slope = [yDiff, xDiff]

    return slope 

def createHashableKeyForRational(numerator, denominator):
    return str(numerator) + ":" + str(denominator)

def getGreatestCommonDivisor(num1, num2):
    a = num1
    b = num2 
    while True:
        if a == 0:
            return b 
        if b == 0:
            return a
        a, b = b, a % b 

if __name__ == "__main__":
    points = [
        [1, 1],
        [2, 2],
        [3, 3],
        [0, 4],
        [-2, 6],
        [4, 0],
        [2, 1]
    ]
    assert lineThroughPoints(points) == 4

    points = [
        [3, 3],
        [0, 4],
        [-2, 6],
        [4, 0],
        [2, 1],
        [3, 4],
        [5, 6],
        [0, 0]
    ]
    assert lineThroughPoints(points) == 3

    points = [
        [1, 4],
        [3, 5],
        [7, 1],
        [5, 4],
        [4, 5],
        [9, 2],
        [1, 3],
        [2, 8]
    ]
    assert lineThroughPoints(points) == 3

    points = [
        [1, 4],
        [4, 1],
        [3, 3]
    ]
    assert lineThroughPoints(points) == 2

    points = [
        [0, 0]
    ]
    assert lineThroughPoints(points) == 1

    points = [
        [1, 4],
        [4, 1],
        [1, 1],
        [4, 4],
        [2, 3],
        [3, 2],
        [3, 3],
        [2, 2],
        [0, 3]
    ]
    assert lineThroughPoints(points) == 4

    points = [
        [1, 4],
        [4, 1],
        [1, 1],
        [4, 4],
        [2, 3],
        [3, 2],
        [3, 3],
        [2, 2],
        [0, 3],
        [5, 3],
        [3, -1],
        [2, -3],
        [1, -5]
    ]
    assert lineThroughPoints(points) == 5

    points = [
        [-1, -1],
        [-3, -1],
        [-4, -1],
        [1, 1],
        [4, 1]
    ]
    assert lineThroughPoints(points) == 3

    points = [
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 1],
        [2, 2],
        [2, 3],
        [2, 4],
        [2, 5],
        [3, 1],
        [3, 2],
        [3, 4],
        [3, 5],
        [4, 1],
        [4, 2],
        [4, 3],
        [4, 4],
        [4, 5],
        [5, 1],
        [5, 2],
        [5, 3],
        [5, 4],
        [5, 5],
        [6, 6],
        [2, 6]
    ]
    assert lineThroughPoints(points) == 6

    points = [
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 1],
        [2, 2],
        [2, 4],
        [2, 5],
        [4, 1],
        [4, 2],
        [4, 4],
        [4, 5],
        [5, 1],
        [5, 2],
        [5, 4],
        [5, 5],
        [6, 6],
        [2, 6],
        [-1, -1],
        [0, 0],
        [-2, -2]
    ]
    assert lineThroughPoints(points) == 8

    points = [
        [-78, -9],
        [67, 87],
        [46, 87],
        [4, 5],
        [9, 83],
        [34, 47]
    ]
    assert lineThroughPoints(points) == 2

    points = [
        [1000000001, 1],
        [1, 1],
        [0, 0]
    ]
    assert lineThroughPoints(points) == 2