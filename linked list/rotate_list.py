# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k==0 or head is None:
            return head
        curr=head
        # count the length of linked list
        count=1
        while curr.next:
            curr=curr.next
            count+=1
        
        # pointing the last node to the head
        curr.next=head
        # traversing count - k nodes and taking care if k>=count
        k=count-(k%count)
        while k>0:
            k-=1
            curr=curr.next
        # make the head
        head=curr.next
        # break the connection and point it to none
        curr.next=None
        return head
