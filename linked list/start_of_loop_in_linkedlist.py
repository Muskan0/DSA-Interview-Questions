# https://www.interviewbit.com/problems/list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        head=A
        if A is None or A.next is None:
            return None
        slow=head
        fast=head
        slow=slow.next
        fast=fast.next.next
        while slow!=fast:
            if fast is None or fast.next is None:
                return None
            slow=slow.next
            fast=fast.next.next
        
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
