from typing import List

def arrayOfProducts(array):
    """
    Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.

    In other words, the value at output[i] is equal to teh product of every number in the input array other than input[i].

    Note that you're expected to solve this problem without using division.

    Sample Input:
    ```
    array = [5, 1, 4, 2]
    ```

    Sample Output:
    ```
    [8, 40, 10, 20]
    ```

    Hints:
    1. Think about the most naive approach to solving this problem. How can we do exactly what the problem wants us to do without focusing at all on time and space complexity?
    2. Understand how output[i] is being calculated. How can we calculate the product of every element other than the one at the current index? Can we do this with just one loop through the input array, or do we have to do multiple loops?
    3. For each index in the input array, try calculating the product of every elements to the left and the product of every element to the right. You can do this with two loops through the array: one from left to right and one from right to left. How can these products help us?

    Optimal Space & Time Complexity
    O(n) time | O(n) space - where n is the length of the input array
    """
    # O(n^2) time | O(n) space - where n is the length of the input array 
    products = [1 for _ in range(len(array))]

    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
        products[i] = runningProduct
    
    return products

    # O(n) time | O(n) space - where n is the length of the input array
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    leftRunningProducts = 1
    for i in range(len(array)):
        leftProducts[i] = leftRunningProducts
        leftRunningProducts *= array[i]
    
    rightRunningProducts = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProducts
        rightRunningProducts *= array[i]
    
    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]
    
    return products 

    # O(n) time | O(n) space - where n is the length of the input array
    products = [1 for _ in range(len(array))]

    leftRunningProducts = 1
    for i in range(len(array)):
        products[i] = leftRunningProducts
        leftRunningProducts *= array[i]

    rightRunningProducts = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProducts
        rightRunningProducts *= array[i]

    return products 

if __name__ == "__main__":
    array = [5, 1, 4, 2]
    assert arrayOfProducts(array) == [8, 40, 10, 20]

    array = [1, 8, 6, 2, 4]
    assert arrayOfProducts(array) == [384, 48, 64, 192, 96]

    array = [-5, 2, -4, 14, -6]
    assert arrayOfProducts(array) == [672, -1680, 840, -240, 560]

    array = [9, 3, 2, 1, 9, 5, 3, 2]
    assert arrayOfProducts(array) == [1620, 4860, 7290, 14580, 1620, 2916, 4860, 7290]

    array = [4, 4]
    assert arrayOfProducts(array) == [4, 4]

    array = [0, 0, 0, 0]
    assert arrayOfProducts(array) == [0, 0, 0, 0]

    array = [1, 1, 1, 1]
    assert arrayOfProducts(array) == [1, 1, 1, 1]

    array = [-1, -1, -1]
    assert arrayOfProducts(array) == [1, 1, 1]

    array = [-1, -1, -1, -1]
    assert arrayOfProducts(array) == [-1, -1, -1, -1]

    array = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert arrayOfProducts(array) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert arrayOfProducts(array) == [362880, 0, 0, 0, 0, 0, 0, 0, 0, 0]