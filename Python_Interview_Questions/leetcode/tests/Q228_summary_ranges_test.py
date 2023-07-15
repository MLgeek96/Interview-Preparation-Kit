import pytest
from leetcode.problem_sets.Q228_summary_ranges import summaryRanges

print(summaryRanges.__doc__)

def test_summaryRanges():
    nums = [0,1,2,4,5,7]
    assert summaryRanges(nums) == ["0->2","4->5","7"]

    nums = [0,2,3,4,6,8,9]
    assert summaryRanges(nums) == ["0","2->4","6","8->9"]