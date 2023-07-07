import pytest
from leetcode.problem_sets.Q21_merge_two_sorted_lists import mergeTwoLists, ListNode

print(mergeTwoLists.__doc__)

@pytest.mark.skip(reason="In Progress")
def test_mergeTwoLists():
    head_list1 = ListNode()
    cur_list1 = head_list1

    for i in [1, 2, 4]:
        cur_list1.next = ListNode(i)
        cur_list1 = cur_list1.next
    
    head_list2 = ListNode()
    cur_list2 = head_list2

    for i in [1, 3, 4]:
        cur_list2.next = ListNode(i)
        cur_list2 = cur_list2.next

    head = ListNode()
    cur = head

    for i in [1, 1, 2, 3, 4, 4]:
        cur.next = ListNode(i)
        cur = cur.next

    assert mergeTwoLists(head_list1.next, head_list2.next) == head.next