from typing import List

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    """
    A tandem bicycle is a bicycle that's operated by two people, person A and person B. Both people pedal the bicycle, but the person that pedals faster dictates the speed of the bicycle. So if person A pedals at a speed of 5, and person B pedals at a speed of 4, the tandem bicycle moves at a speed of 5 (i.e., tandemSpeed = max(speedA, speedB)).

    You're given two lists of positive integers: one that contains the speeds of riders wearing red shirts and one that contains the speeds of riders waearing blue shirts. Each rider is represented by a single positive integer, which is the speed that they pedal a tandem bicycle at. Both lists have the same length, meaning that there are as many red-shirt riders as there are blue-shirt riders. Your goal is to pair every rider wearing a red shirt with a rider wearing a blue shirt to operate a tandem bicycle.

    Write a function that returns the maximum possible total speed or the minimum possible total speed of all of the tandem bicycles beign ridden based on an input parameter, fastest. If fastest = true, your function should return the maximum possible total speed, otherwise it should return the minimum total speed.

    "Total speed" is defined as the sum of the speeds of all the tandem bicycles being ridden. For example, if there are 4 riders (2 red-shirt riders and 2 blue-shirt riders) who have speeds of 1, 3, 4, 5, and if they're paired on tandem bicycles as follows: [1, 4], [5, 3], then the total speed of these tandem bicycles is 4 + 5 = 9.

    Sample Input:
    ```
    redShirtSpeed = [5, 5, 3, 9, 2]
    blueShirtSpeeds = [3, 6, 7, 2, 1]
    fastest = True
    ```

    Sample Output:
    ```
    32
    ```

    Hints:
    1. The brute-force approach to solve this problem is to generate every possible set of pairs of riders and to determine the total speed that each of these sets generates. This solution does work but, it isn't optimal. Can you think of a better way to solve this problem?
    2. Try looking at the input arrays in sorted order. How might this help you solve the problem?
    3. When generating the maximum total speed, you want to pair the slowest red-shirt riders with the fastest blue-shirt riders and vice versa, so as to always take advantage of the largest speeds. When generating the minimum total speed, you want to pair the fastest red-shirt riders with the fastest blue-shirt riders, so as to "eliminate" a large speed by pairing it with a another large (larger) speed.
    4. Sort the input arrays in place, and follow the strategy discussed in Hint #3. With the inputs sorted, you can find the slowest and largest speeds from each shirt color in constant time.

    Optimal Space & Time Complexity
    O(nlog(n)) time | O(1) space - where n is the number of tandem bicycles
    """
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        reverseArrayInPlace(redShirtSpeeds)

    totalSpeed = 0 
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]
        totalSpeed += max(rider1, rider2)
    
    return totalSpeed

def reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    redShirtSpeeds = [5, 5, 3, 9, 2]
    blueShirtSpeeds = [3, 6, 7, 2, 1]
    fastest = True
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 32

    redShirtSpeeds = [5, 5, 3, 9, 2]
    blueShirtSpeeds = [3, 6, 7, 2, 1]
    fastest = False
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 25

    redShirtSpeeds = [1, 2, 1, 9, 12, 3]
    blueShirtSpeeds = [3, 3, 4, 6, 1, 2]
    fastest = False
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 30

    redShirtSpeeds = [1, 2, 1, 9, 12, 3]
    blueShirtSpeeds = [3, 3, 4, 6, 1, 2]
    fastest = True
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 37

    redShirtSpeeds = [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1]
    blueShirtSpeeds = [3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32]
    fastest = True
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 816

    redShirtSpeeds = [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1]
    blueShirtSpeeds = [3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32]
    fastest = False
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 484

    redShirtSpeeds = [1]
    blueShirtSpeeds = [5]
    fastest = True
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 5

    redShirtSpeeds = [1]
    blueShirtSpeeds = [5]
    fastest = False
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 5

    redShirtSpeeds = [1, 1, 1, 1]
    blueShirtSpeeds = [1, 1, 1, 1]
    fastest = True
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 4

    redShirtSpeeds = [1, 1, 1, 1]
    blueShirtSpeeds = [1, 1, 1, 1]
    fastest = False
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 4

    redShirtSpeeds = [1, 1, 1, 1, 2, 2, 2, 2, 9, 11]
    blueShirtSpeeds = [1, 1, 1, 1, 3, 3, 3, 3, 5, 7]
    fastest = True
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 48

    redShirtSpeeds = [1, 1, 1, 1, 2, 2, 2, 2, 9, 11]
    blueShirtSpeeds = [1, 1, 1, 1, 3, 3, 3, 3, 5, 7]
    fastest = False
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 36

    redShirtSpeeds = [9, 8, 2, 2, 3, 5, 6]
    blueShirtSpeeds = [3, 4, 4, 1, 1, 8, 9]
    fastest = True
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 49

    redShirtSpeeds = [9, 8, 2, 2, 3, 5, 6]
    blueShirtSpeeds = [3, 4, 4, 1, 1, 8, 9]
    fastest = False
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 35

    redShirtSpeeds = [5, 4, 3, 2, 1]
    blueShirtSpeeds = [1, 2, 3, 4, 5]
    fastest = False
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 15

    redShirtSpeeds = [5, 4, 3, 2, 1]
    blueShirtSpeeds = [1, 2, 3, 4, 5]
    fastest = True
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 21

    redShirtSpeeds = []
    blueShirtSpeeds = []
    fastest = True
    assert tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) == 0

