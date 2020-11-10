# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        fast=head
        slow=head
        while fast.next!=None and fast.next.next!=None:
            fast=fast.next.next
            slow=slow.next
        slow.next=reverse(slow.next)
        slow=slow.next
        dummy=head
        while slow is not None:
            if dummy.val!=slow.val:
                return False
            dummy=dummy.next
            slow=slow.next
        return True

def reverse(ptr):
    dummy=None
    while ptr:
        next=ptr.next
        ptr.next=dummy
        dummy=ptr
        ptr=next
    return dummy
