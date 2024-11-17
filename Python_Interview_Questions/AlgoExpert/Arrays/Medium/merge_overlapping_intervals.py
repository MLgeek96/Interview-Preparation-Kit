from typing import List

def mergeOverlappingIntervals(intervals):
    """
    Write a function that takes in non-empty array of arbitrary intervals, merges any overlapping intervals, and returns the new intervals in no particular order.

    Each interval interval is an array of two integers, with interval[0] as the start of the interval and interval[1] as the end of the interval. 

    Note that back-to-back intervals aren't considered to be overlapping. For example, [1, 5] and [6, 7] aren't overlapping. However, [1, 6] and [6, 7] are indeed overlapping. 

    Also note that the start of any particular interval will always be less than or equal to the end of that interval.

    Sample Input:
    ```
    intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
    ```

    Sample Output:
    ```
    [[1, 2], [3, 8], [9, 10]]
    // Merge the intervals [3, 5], [4, 7] and [6, 8].
    // The intervals could be ordered differently.
    ```

    Hints:
    1. The problem asks you to merge overlapping intervals. How can you determine if the two intervals are overlapping?
    2. Sort the intervals with respect to their starting values. This will allow you to merge all overlapping intervals in a single traversal through the sorted intervals.
    3. After sorting the intervals with respect to their starting values, traverse them, and at each iteration, compare the start of the next interval to the end of the current interval to look for an overlap. If you find an overlap, mutate the current interval so as to merge the next interval into it.

    Optimal Space & Time Complexity
    O(nlog(n)) time | O(n) space - where n is the length of the input array 
    """
    sortedIntervals = sorted(intervals, key = lambda x: x[0])

    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval 
        nextIntervalStart, nextIntervalEnd = nextInterval 

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval 
            mergedIntervals.append(currentInterval)

    return mergedIntervals

if __name__ == "__main__":
    intervals = [
        [1, 2],
        [3, 5],
        [4, 7],
        [6, 8],
        [9, 10]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [1, 2],
        [3, 8],
        [9, 10]
    ]

    intervals = [
        [1, 3],
        [2, 8],
        [9, 10]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [1, 8],
        [9, 10]
    ]

    intervals =  [
        [1, 10],
        [10, 20],
        [20, 30],
        [30, 40],
        [40, 50],
        [50, 60],
        [60, 70],
        [70, 80],
        [80, 90],
        [90, 100]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [1, 100]
    ]

    intervals = [
        [1, 10],
        [11, 20],
        [21, 30],
        [31, 40],
        [41, 50],
        [51, 60],
        [61, 70],
        [71, 80],
        [81, 90],
        [91, 100]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [1, 10],
        [11, 20],
        [21, 30],
        [31, 40],
        [41, 50],
        [51, 60],
        [61, 70],
        [71, 80],
        [81, 90],
        [91, 100]
    ]

    intervals =  [
        [100, 105],
        [1, 104]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [1, 105]
    ]

    intervals = [
        [89, 90],
        [-10, 20],
        [-50, 0],
        [70, 90],
        [90, 91],
        [90, 95]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [-50, 20],
        [70, 95]
    ]

    intervals = [
        [-5, -4],
        [-4, -3],
        [-3, -2],
        [-2, -1],
        [-1, 0]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [-5, 0]
    ]

    intervals = [
        [43, 49],
        [9, 12],
        [12, 54],
        [45, 90],
        [91, 93]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [9, 90],
        [91, 93]
    ]

    intervals = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [0, 0]
    ]

    intervals =  [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 1]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [0, 1]
    ]

    intervals = [
        [1, 22],
        [-20, 30]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [-20, 30]
    ]

    intervals = [
        [20, 21],
        [22, 23],
        [0, 1],
        [3, 4],
        [23, 24],
        [25, 27],
        [5, 6],
        [7, 19]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [0, 1],
        [3, 4],
        [5, 6],
        [7, 19],
        [20, 21],
        [22, 24],
        [25, 27]
    ]

    intervals = [
        [2, 3],
        [4, 5],
        [6, 7],
        [8, 9],
        [1, 10]
    ]
    assert mergeOverlappingIntervals(intervals) == [
        [1, 10]
    ]