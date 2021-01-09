from typing import List

def container_with_most_water(height: List[int]) -> int :
    """"
    Given n non-negative integers a1, a2, ..., an ,
    where each represents a point at coordinate (i, ai).

    n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).

    Find two lines, which, together with the x-axis forms a container,
    such that the container contains the most water.

    Notice that you may not slant the container.

    Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
    In this case, the max area of water (blue section) the container can contain is 49.

    Example 2:
    Input: height = [1,1]
    Output: 1

    Example 3:
    Input: height = [4,3,2,1,4]
    Output: 16

    Example 4:
    Input: height = [1,2,1]
    Output: 2

    Constraints:
    n == height.length
    2 <= n <= 3 * 104
    0 <= height[i] <= 3 * 104

    """
    assert 2 <= len(height) <= 3 * 104, "Length of height is strictly between 2 and 3 * 104"
    for i in range(len(height)):
        assert 0 <= height[i] <= 3 * 104, "Length of height is strictly between 2 and 3 * 104"
    max_volume = 0
    n = len(height)
    i = 0
    j = n - 1
    while i < j:
        max_volume = max(max_volume, min(height[i], height[j]) * (j - i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_volume
