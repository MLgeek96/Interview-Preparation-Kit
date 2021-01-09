import pytest
from leetcode.problem_sets.Q11_container_with_most_water import container_with_most_water

def test_container_with_most_water():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ans = container_with_most_water(height)

    assert ans == 49

    height = [1, 1]
    ans = container_with_most_water(height)

    assert ans == 1

    height = [4,3,2,1,4]
    ans = container_with_most_water(height)

    assert ans == 16

    height = [1, 2, 1]
    ans = container_with_most_water(height)

    assert ans == 2


