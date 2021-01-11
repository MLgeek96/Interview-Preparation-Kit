import pytest 
from leetcode.problem_sets.Q2_add_two_numbers import add_two_numbers, ListNode

print(add_two_numbers.__doc__)

def test_add_two_numbers():
    a = ListNode(2)
    a1 = ListNode(4)
    a2 = ListNode(3)

    a.next = a1
    a1.next = a2

    b = ListNode(5)
    b1 = ListNode(6)
    b2 = ListNode(4)

    b.next = b1
    b1.next = b2

    sol = ListNode(7)
    sol1 = ListNode(0)
    sol2 = ListNode(8)

    sol.next = sol1
    sol1.next = sol2

    ans = add_two_numbers(a, b)

    while ans != None:        
        assert ans.val == sol.val
        sol = sol.next 
        ans = ans.next

        

        
    
        
