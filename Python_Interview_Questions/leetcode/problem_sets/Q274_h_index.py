from typing import List

def hIndex(citations: List[int]) -> int:
    """
    Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

    According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

    Example 1:
    Input: citations = [3,0,6,1,5]
    Output: 3
    Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
    Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

    Example 2:
    Input: citations = [1,3,1]
    Output: 1
    
    Constraints:
    • n == citations.length
    • 1 <= n <= 5000
    • 0 <= citations[i] <= 1000
    """
    assert 1 <= len(citations) <= 5000
    for citation in citations:
        assert 0 <= citation <= 1000

    citations.sort(reverse=True)
    h = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h = i + 1
    return h

    # citations.sort(reverse=True)
    # if len(citations) == 1 and citations[0] > 0:
    #     return 1
    # if citations[-1] >= len(citations):
    #     return len(citations)
    # for i in range(len(citations)):
    #     if citations[i] < i + 1:
    #         return i
    # return 0