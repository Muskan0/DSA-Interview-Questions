# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k==0:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=cur=nex=dummy
        
        # count of length
        count= 0
        
        while cur.next != None:
            cur=cur.next
            count+=1
        
        while count>=k:    
            cur=pre.next # first node of size k group
            nex=cur.next # nex is second node of size k group
            # k-1 operations
            for i in range(0,k-1):
                # for reversing the links
                cur.next=nex.next
                nex.next=pre.next
                pre.next=nex
                nex=cur.next
            count-=k
            pre=cur # pre is made to last node of size k group
        return dummy.next
    
# Time complexity: O(N/K)*K  = O(N)
# ( N/K is the number of groups of size K and for every group we do K-1 iterations)
# Space complexity: O(1), for storing pointers
