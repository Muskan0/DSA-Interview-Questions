# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        a=headA
        b=headB
        # if a and b have different length
        # then loop will stop after second iteration
        while a!=b:
            # after end of first iteration, pointer is reset to head of another linkedlist
            if a is None:
                a=headB
            else:
                a=a.next
            if b is None:
                b=headA
            else:
                b=b.next
        return a
