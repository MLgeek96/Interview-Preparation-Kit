from typing import List

def taskAssignment(k: int, tasks: List[int]):
    """
    You're given an integer k representing a number of workers and an array of positive integers representign durations of tasks that must be completed by the workers. Specifically, each worker must complete two unique tasks and can only work on one task at a time. The number of tasks willa lways be equal to 2k such that each worker always has exactly two tasks to complete. All tasks are independent of one another and can be completed in any order. Workers will complete their assigned tasks in parallel, and the time taken to complete all tasks will be equal to the time taken to complete the longest pair of tasks (see the sample output for an explanation).

    Write a function that returns the optimal assignment of tasks to each worker such that the tasks are completed as fast as possible. Your function should return a list of pairs, where each pair stores the indices of the tasks that should be completed by one worker. The pairs should be in the following format: [task1, task2], where the order of task1 and task2 doesn't matter. Your function can return the pairs in any order. If multiple optimal assignments exist, any correct answer will be accepted.

    Note: you'll always be given at least one worker (i.e., k will always be greater than 0).

    Sample Input:
    ```
    k = 3
    tasks = [1, 3, 5, 3, 1, 4]
    ```

    Sample Output:
    ```
    [
        [0, 2], // tasks[0] = 1, tasks[2] = 5 | 1 + 5 = 6
        [4, 5], // tasks[4] = 1, tasks[5] = 4 | 1 + 4 = 5
        [1, 3], // tasks[1] = 3, tasks[3] = 3 | 3 + 3 = 6
    ]

    // Note: there are multiple correct answers for this sample input.
    // The following is an example of another correct answer:
    // [
    //    [2, 4],
    //    [0, 5],
    //    [1, 3],
    // ]
    ```

    Hints:
    1. Start by considering which pairs of tasks will lead to the longest possible time to complete all tasks.
    2. The amount of time it'll take to complete all tasks will be dictated by the pair of tasks that has the longest total duration. This means that you'll want to avoid pairing long tasks together.
    3. Since the pair of tasks with the longest total duration is the time it takes for us to finish all tasks, we want to minimize this pair's duration. To do this, we can simply pair the shortest-duration task with the longest-duration task and repeat the process with all other tasks.
    4. Start by sorting the tasks array in ascending order. Then, pair the shortest-duration task with the longest-duration task, and add that pair to some output array. Repeat this process until you've paired all tasks. This will lead to an optimal pairing, because your pair of tasks with the longest duration will have the shortest duration that it can possibly have.

    Optimal Space & Time Complexity
    O(nlog(n)) time | O(n) space - where n is the number of tasks
    """
    pairedTasks = []
    taskDurationToIndices = getTaskDurationToIndices(tasks)

    sortedTasks = sorted(tasks)
    for idx in range(k):
        task1Duration = sortedTasks[idx]
        indicesWithTask1Duration = taskDurationToIndices[task1Duration]
        task1Index = indicesWithTask1Duration.pop()

        task2SortedIndex = len(tasks) - 1 - idx 
        task2Duration = sortedTasks[task2SortedIndex]
        indicesWithTask2Duration = taskDurationToIndices[task2Duration]
        task2Index = indicesWithTask2Duration.pop()

        pairedTasks.append([task1Index, task2Index])

    return pairedTasks

def getTaskDurationToIndices(tasks):
    taskDurationsToIndices = {}

    for idx, taskDuration in enumerate(tasks):
        if taskDuration in taskDurationsToIndices:
            taskDurationsToIndices[taskDuration].append(idx)
        else:
            taskDurationsToIndices[taskDuration] = [idx]
    
    return taskDurationsToIndices

if __name__ == "__main__":
    k = 3
    tasks = [1, 3, 5, 3, 1, 4]
    assert taskAssignment(k, tasks) == [[4, 2],  [0, 5],  [3, 1]]

    k = 4
    tasks = [1, 2, 3, 4, 5, 6, 7, 8]
    assert taskAssignment(k, tasks) == [[0, 7],  [1, 6],  [2, 5],  [3, 4]]

    k = 5
    tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert taskAssignment(k, tasks) == [[9, 8],  [7, 6],  [5, 4],  [3, 2],  [1, 0]]

    k = 1
    tasks = [3, 5]
    assert taskAssignment(k, tasks) == [[0, 1]]

    k = 7
    tasks = [2, 1, 3, 4, 5, 13, 12, 9, 11, 10, 6, 7, 14, 8]
    assert taskAssignment(k, tasks) == [[1, 12],  [0, 5],  [2, 6],  [3, 8],  [4, 9],  [10, 7],  [11, 13]]

    k = 5
    tasks = [3, 7, 5, 4, 4, 3, 6, 8, 3, 3]
    assert taskAssignment(k, tasks) == [[9, 7],  [8, 1],  [5, 6],  [0, 2],  [4, 3]
]

    k = 10
    tasks = [5, 6, 2, 3, 15, 15, 16, 19, 2, 10, 10, 3, 3, 32, 12, 1, 23, 32, 9, 2]
    assert taskAssignment(k, tasks) == [[15, 17],  [19, 13],  [8, 16],  [2, 7],  [12, 6],  [11, 5],  [3, 4],  [0, 14],  [1, 10],  [18, 9]]

    k = 4
    tasks = [1, 2, 2, 1, 3, 4, 4, 4]
    assert taskAssignment(k, tasks) == [[3, 7],  [0, 6],  [2, 5],  [1, 4]]

    k = 3
    tasks = [87, 65, 43, 32, 31, 320]
    assert taskAssignment(k, tasks) == [[4, 5],  [3, 0],  [2, 1]]

    k = 2
    tasks = [3, 4, 5, 3]
    assert taskAssignment(k, tasks) == [[3, 2],  [0, 1]]

    k = 3
    tasks = [5, 2, 1, 6, 4, 4]
    assert taskAssignment(k, tasks) == [[2, 3],  [1, 0],  [5, 4]]

    k = 2
    tasks = [1, 8, 9, 10]
    assert taskAssignment(k, tasks) == [[0, 3],  [1, 2]]

