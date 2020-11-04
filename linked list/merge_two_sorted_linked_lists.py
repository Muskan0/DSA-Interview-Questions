# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # in place solution
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val>l2.val:
            l1,l2,=l2,l1
        res = l1
        while l1 !=None and l2!=None:
            temp=None
            while l1!=None and l1.val<=l2.val:
                temp=l1
                l1=l1.next
            temp.next=l2
            l1,l2=l2,l1
        return res
        '''
        # external space solution
        if None in (l1,l2):
            return l1 or l2
        temp=ListNode(0)
        curr=temp
        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                curr=curr.next
                l1=l1.next
            else:
                curr.next=l2
                curr=curr.next
                l2=l2.next
        if l1:
            curr.next=l1
        if l2:
            curr.next=l2
        return temp.next
        '''
