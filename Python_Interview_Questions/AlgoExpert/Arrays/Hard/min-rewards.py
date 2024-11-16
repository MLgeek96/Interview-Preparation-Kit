
def minRewards(scores):
    """
    Imagine that you're a teacher who's just graded the final exam in a class. 
    You have a list of student scores on the final exam in a particular order (not necessarily sorted), and you want to reward your students. 
    You decide to do so fairly by giving them arbitrary rewards following two rules:

    1. All students must receive at least one reward.
    2. Any given student must receive strictly more rewards than an adjacent student  (a student immediately to the left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score.

    Write a function that takes in a list of scores and returns the minimum number of rewards that you mist give out to students to satisfy the two rules.

    You can assume that all students have different scores; in other words, the scores are all unique.

    Sample Input:
    ```
    scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
    ```

    Sample Output:
    ```
    25 // you would give out the following rewards: [4, 3, 2, 1, 2, 3, 4, 5, 1]
    ```

    Hints:
    1. You could try iterating through the input list of scores and incrementing the number of rewards you give to each student if they have a greater score than the previous student's score. However, if you reach a student with a smaller score than the previous student's score, you'll have to backtrack through the array to fix previous reward assignments. During this backtrack, is it correct to simply increment the reward of a student whose score is greater than the next student's score?
    2. Notice that there are local mins and local maxes in the input list of scores: scores that are smaller than both scores next to them and scores that are greater than both scores next to them. Find the local mins, and try expanding away from them until you reach local maxes, assigning (and incrementing) rewards as you go.
    3. Do you actually need to find the local mins mentioned in Hint #2? Can you simply do two sweeps of the input list of scores, one from left to right, and one from right to left?

    Optimal Space & Time Complexity
    O(n) time | O(n) space - where n is the length of the input array
    """
    # # O(n^2) time | O(n) space - where n is the length of the input array 
    # rewards = [1 for _ in scores]
    # for i in range(1, len(scores)):
    #     j = i - 1
    #     if scores[i] > scores[j]:
    #         rewards[i] = rewards[j] + 1
    #     else:
    #         while j >= 0 and scores[j] > scores[j + 1]:
    #             rewards[j] = max(rewards[j], rewards[j + 1] + 1)
    #             j -= 1
    # return sum(rewards)

    # # O(n) time | O(n) space - where n is the length of the input array 
    # rewards = [1 for _ in scores]
    # localMinIdxs = getLocalMinIdxs(scores)
    # for localMinIdx in localMinIdxs:
    #     expandFromLocalMinIdx(localMinIdx, scores, rewards)
    # return sum(rewards)

    # def getLocalMinIdxs(array):
    #     if len(array) == 1:
    #         return [0]
    #     localMinIdxs = []
    #     for i in range(len(array)):
    #         if i == 0 and array[i] < array[i + 1]:
    #             localMinIdxs.append(i)
    #         if i == len(array) - 1 and array[i] < array[i + 1]:
    #             localMinIdxs.append(i)
    #         if i == 0 or i == len(array) - 1:
    #             continue 
    #         if array[i] < array[i + 1] and array[i] < array[i - 1]:
    #             localMinIdxs.append(i)
    #     return localMinIdxs

    # def expandFromLocalMinIdx(localMinIdx, scores, rewards):
    #     leftIdx = localMinIdx - 1
    #     while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
    #         rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
    #         leftIdx -= 1
    #     rightIdx = localMinIdx + 1
    #     while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
    #         rewards[rightIdx] = rewards[rightIdx - 1] + 1
    #     rightIdx += 1

    # O(n) time | O(n) space - where n is the length of the input array 
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)

if __name__ == "__main__":
    scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
    asset minRewards(scores) == 25

    scores = [1]
    asset minRewards(scores) == 1

    scores = [5, 10]
    asset minRewards(scores) == 3

    scores = [10, 5]
    asset minRewards(scores) == 3

    scores = [4, 2, 1, 3]
    asset minRewards(scores) == 8

    scores = [0, 4, 2, 1, 3]
    asset minRewards(scores) == 9

    scores = [2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0]
    asset minRewards(scores) == 52

    scores = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
    asset minRewards(scores) == 15

    scores = [800, 400, 20, 10, 30, 61, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53]
    asset minRewards(scores) == 93