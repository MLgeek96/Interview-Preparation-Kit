from typing import List

def apartmentHunting(blocks, reqs):
    """
    You're looking to move into a new apartment on specific street, and you're given a list of contiguous blocks on that street where each block contains an apartment that you could move into.

    You also have a list of requirements: a list of buildings that are important to you. For instance, you might value having a school and a gym near your apartment. The list of blocks that you have contains information at every blocks about all of the buildings that are present and absent at the block in question. For instance, for every block, you might know whether a school, a pool, and office, and a gym are present.

    In order to optimize your life, you want to pick an apartment block such that you minimize the farthest distance you'd have to walk from your apartment to reach any of your required buildings.

    Write a function that takes in a list of contiguous blocks on a specific street and a list of your required buildings and that returns the location (the index) of the block that's most optimal for you.

    If there are multiple most optional blocks, your function can return the index of any one of them.

    Sample Input:
    ```
    blocks = [
        {
            "gym": False,
            "school": True,
            "store": False,
        },
        {
            "gym": True,
            "school": False,
            "store": False,
        },
        {
            "gym": True,
            "school": True,
            "store": False,
        },
        {
            "gym": False,
            "school": True,
            "store": False,
        },
        {
            "gym": False,
            "school": True,
            "store": True,
        },
    ]
    reqs = ["gym", "school", "store"]
    ```

    Sample Output:
    ```
    3 // at index 3, the farthest you'd have to walk to reach a gym, a school, or a store is 1 block; at any other index, you'd have to walk farther
    ```

    Hints:
    1. For every block, you want to go through every requirement, and for every requirement, you want to find the closest otehr block with that requirement (or rather, the smallest distance to another block with that requirement). Once you've done that for every requirement and for every block, you want to pick, for every block, the distance of the farthest requirement. You can do this with three nested ""for" loops.
    2. Is there a way to optimize on the solution mentioned in Hint #1 (that uses three nested "for" loops) by pre-computing the smallest distances of every requirement from every block?
    3. For every requirement, you should be able to precompute its smallest distances from every block by doing two simple passes through the array of blocks: one pass from left to right and one pass from right to left. Once you have these precomputed values, you can iterate through all of the blocks and pick the biggest of all the precomputed distances at that block.

    Optimal Space & Time Complexity
    O(br) time | O(br) space - where b is the number of blocks and r is the number of requirements
    """
    # O(b^2 * r) time | O(b) space - where b is the number of blocks and r is the number of requirements
    def getIdxAtMinValue(array):
        idxAtMinValue = 0 
        minValue = float("inf")
        for i in range(len(array)):
            currentValue = array[i]
            if currentValue < minValue:
                minValue = currentValue 
                idxAtMinValue = i 
        return idxAtMinValue

    def distanceBetween(a, b):
        return abs(a - b)
    
    maxDistancesAtBlocks = [float("-inf") for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
            maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)
    return getIdxAtMinValue(maxDistancesAtBlocks)


    # O(br) time | O(br) space - where b is the number of blocks and r is the number of requirements
    def getMinDistances(blocks, req):
        minDistances = [0 for block in blocks]
        closestReqIdx = float("inf")
        for i in range(len(blocks)):
            if blocks[i][req]:
                closestReqIdx = i 
            minDistances[i] = distanceBetween(i, closestReqIdx)
        for i in reversed(range(len(blocks))):
            if blocks[i][req]:
                closestReqIdx = i 
            minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
        return minDistances 

    def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
        maxDistancesAtBlocks = [0 for _ in blocks]
        for i in range(len(blocks)):
            minDistancesAtBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
            maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
        return maxDistancesAtBlocks

    def getIdxAtMinValue(array):
        idxAtMinValue = 0 
        minValue = float("inf")
        for i in range(len(array)):
            currentValue = array[i]
            if currentValue < minValue:
                minValue = currentValue 
                idxAtMinValue = i 
        return idxAtMinValue 

    def distanceBetween(a, b):
        return abs(a - b)
    
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
    return getIdxAtMinValue(maxDistancesAtBlocks)

if __name__ == "__main__":
    blocks = [
        {
        "gym": False,
        "school": True,
        "store": False
        },
        {
        "gym": True,
        "school": False,
        "store": False
        },
        {
        "gym": True,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "school": True,
        "store": True
        }
    ]
    reqs = ["gym", "school", "store"]
    assert apartmentHunting(blocks, reqs) == 3

    blocks = [
        {
        "gym": False,
        "office": True,
        "school": True,
        "store": False
        },
        {
        "gym": True,
        "office": False,
        "school": False,
        "store": False
        },
        {
        "gym": True,
        "office": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "school": True,
        "store": True
        }
    ]
    reqs = ["gym", "office", "school", "store"]
    assert apartmentHunting(blocks, reqs) == 2

    blocks = [
        {
        "gym": False,
        "office": True,
        "school": True,
        "store": False
        },
        {
        "gym": True,
        "office": False,
        "school": False,
        "store": False
        },
        {
        "gym": True,
        "office": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "school": True,
        "store": True
        }
    ]
    reqs = ["gym", "office", "school", "store"]
    assert apartmentHunting(blocks, reqs) == 2

    blocks = [
        {
        "foo": True,
        "gym": False,
        "kappa": False,
        "office": True,
        "school": True,
        "store": False
        },
        {
        "foo": True,
        "gym": True,
        "kappa": False,
        "office": False,
        "school": False,
        "store": False
        },
        {
        "foo": True,
        "gym": True,
        "kappa": False,
        "office": False,
        "school": True,
        "store": False
        },
        {
        "foo": True,
        "gym": False,
        "kappa": False,
        "office": False,
        "school": True,
        "store": False
        },
        {
        "foo": True,
        "gym": True,
        "kappa": False,
        "office": False,
        "school": True,
        "store": False
        },
        {
        "foo": True,
        "gym": False,
        "kappa": False,
        "office": False,
        "school": True,
        "store": True
        }
    ]
    reqs = ["gym", "school", "store"]
    assert apartmentHunting(blocks, reqs) == 4

    blocks = [
        {
        "gym": True,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": True
        },
        {
        "gym": True,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "school": True,
        "store": False
        }
    ]
    reqs = ["gym", "school", "store"]
    assert apartmentHunting(blocks, reqs) == 2

    blocks = [
        {
        "gym": True,
        "pool": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "pool": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "pool": False,
        "school": False,
        "store": True
        },
        {
        "gym": True,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "pool": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "pool": True,
        "school": False,
        "store": False
        }
    ]
    reqs = ["gym", "pool", "school", "store"]
    assert apartmentHunting(blocks, reqs) == 7

    blocks = [
        {
        "gym": True,
        "office": False,
        "pool": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": True,
        "pool": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "office": True,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": False,
        "school": False,
        "store": True
        },
        {
        "gym": True,
        "office": True,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": True,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": False,
        "school": False,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": False,
        "school": True,
        "store": False
        },
        {
        "gym": False,
        "office": False,
        "pool": True,
        "school": False,
        "store": False
        }
    ]
    reqs = ["gym", "pool", "school", "store"]
    assert apartmentHunting(blocks, reqs) == 4