# O(w^2 * h) time | O(w) space - where w and h are the width and height of the input array 
def waterfallStreams(array, source):
    """
    You're given a two-dimensional array that represents the structure of an indoor waterfall and a positive integer that represents the column that the waterfall's water source will start at. More specifically, the water source will start directly above the structure and will flow downwards.

    Each row in the array contains 0s and 1s, where a 0 represents a free space and a 1 represents a block that water can't pass through. You can imagine that the last row of the array contains buckets that the water will eventually flow into; thus, the last row of the array will always contain only 0s. You can also imagine that there are walls on both sides of the structure, meaning that water will never leave the structure, it will either be trapped against a wall or flow into one of the buckets in teh last row.

    As water flows downwards, if it hits a block, it splits evenly to the left and right-hand side of that block. In other words, 50% of the water flows left and 50% of it flow right. If a water stream is unable to flow to the left or to the right (because of a block or a wall), the water stream in question becomes trapped and can no longer continue to flow in that direction; it effectively gets stuck in the structure and can no longer flow downwards, meaning that 50% of the previous water stream is forever lost.

    Lastly, the input array will always contain at least two rows and one column, and the space directly below the water source (in the first row of the array) will always be empty, allowing the water to start flowing downwards.

    Write a function that returns the percentage of water inside each of the bottom buckets after the water has flowed through the entire structure. 

    Sample Input:
    ```
    array = [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    source = 3
    ```

    Sample Output:
    ```
    [0, 0, 0, 25, 25, 0, 0]

    // The water will flow as follows:
    // [
    //   [0, 0, 0, ., 0, 0, 0],
    //   [1, ., ., ., ., ., 0],
    //   [0, ., 1, 1, 1, ., 0],
    //   [., ., ., ., ., ., .],
    //   [1, 1, 1, ., ., 1, 0],
    //   [0, 0, 0, ., ., 0, 1],
    //   [0, 0, 0, ., ., 0, 0],
    // ]
    ```

    Hints:
    1. Try not to overthink the solution to this problem. If you were to manually go through an example of water flowing downwards through the waterfall structure, what steps would you follow exactly? Can you simply transcribe these steps into code?
    2. To start simple, consider how would you solve this problem if there were only two rows. How would you make water flow from the first row to the second row with your code? Can you make a slight modification to this approach in order to solve this problem for any number of rows?
    3. You'll want to traverse through the input array, all the while keeping track of where and how much water flows. To do this, you'll need to represent water with some value (-1, for exmaple, to distinguish it from the otehr values in the array). Iterate through the input array, row by row, column by column, specifically looking at each current row and the row above it. When you see water in the row above, you'll ahve to reiterate through both the row above and the current row to see if where the water will flow to next (i.e., whether there are open spaces allowing the water to flow sideways and / or downwards), mutating these rows along the way whenever water does flow. You'll have to make sure to keep track of the percentage of water that's flowing whenever water gets split in half. 

    Optimal Space & Time Complexity
    O(w^2 * h) time | O(w) space - where w and h are the width and height of the input array 
    """
    rowAbove = array[0][:]
    rowAbove[source] = -1 

    for row in range(1, len(array)):
        currentRow = array[row][:]
        
        for idx in range(len(rowAbove)):
            valueAbove = rowAbove[idx]

            hasWaterAbove = valueAbove < 0 
            hasBlock = currentRow[idx] == 1 

            if not hasWaterAbove:
                continue 
            
            if not hasBlock:
                currentRow[idx] += valueAbove
                continue 
                
            splitWater = valueAbove / 2
            rightIdx = idx 

            while rightIdx + 1 < len(rowAbove):
                rightIdx += 1

                if rowAbove[rightIdx] == 1:
                    break 
                
                if currentRow[rightIdx] != 1:
                    currentRow[rightIdx] += splitWater 
                    break

            leftIdx = idx 

            while leftIdx - 1 >= 0:
                leftIdx -= 1

                if rowAbove[leftIdx] == 1:
                    break

                if currentRow[leftIdx] != 1:
                    currentRow[leftIdx] += splitWater
                    break 

        rowAbove = currentRow
    finalPercentage = list(map(lambda num: num * -100, rowAbove))
    return finalPercentage

if __name__ == "__main__":
    array = [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    source = 3
    assert waterfallStreams(array, source) == [0, 0, 0, 25, 25, 0, 0]

    array = [
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0]
    ]
    source = 0
    assert waterfallStreams(array, source) == [100]

    array = [
        [0],
        [0],
        [0],
        [0],
        [0],
        [1],
        [0]
    ]
    source = 0
    assert waterfallStreams(array, source) == [0]

    array = [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    source = 3
    assert waterfallStreams(array, source) == [0, 0, 0, 0, 0, 0, 0]

    array = [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    source = 3
    assert waterfallStreams(array, source) == [0, 0, 0, 0, 25, 0, 0]

    array = [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    source = 3
    assert waterfallStreams(array, source) == [25, 6.25, 0, 0, 0, 6.25, 0]

    array = [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    source = 6
    assert waterfallStreams(array, source) == [0, 0, 0, 0, 0, 0, 0]

    array = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    source = 8
    assert waterfallStreams(array, source) == [25, 0, 12.5, 0, 4.6875, 0, 0, 0, 0, 7.8125, 0, 0, 3.125, 37.5]

    array = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    source = 8
    assert waterfallStreams(array, source) == [25, 0, 12.5, 0, 0, 0, 12.5, 6.25, 0, 3.125, 0, 0, 3.125, 37.5]