from typing import List

def trap(height: List[int]) -> int:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.

    Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
    In this case, 6 units of rain water (blue section) are being trapped.

    Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

    Constraints:
    • n == height.length
    • 0 <= n <= 3 * 104
    • 0 <= height[i] <= 105
    """
    assert 0 <= len(height) <= 3 ** 104, "Length of input array must be between 0 and 3 ** 104"
    for i in height:
        assert 0 <= i <= 105, "The height must be between 0 and 105"

    if len(height) < 3:
        return 0
    total_volume = 0
    l_max = [None for _ in range(len(height))]
    r_max = [None for _ in range(len(height))]

    l_max[0] = height[0]
    r_max[-1] = height[-1]
    for i in range(1, len(height)):
        l_max[i] = max(l_max[i - 1], height[i])

    for j in range(len(height) - 2, -1, -1):
        r_max[j] = max(height[j], r_max[j + 1])

    for i in range(len(l_max)):
        min_height = min(l_max[i], r_max[i])
        total_volume += min_height - height[i]

    return total_volume

