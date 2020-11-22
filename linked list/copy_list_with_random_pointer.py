# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        # make copy of each node and link them side by side
        dummy=head
        while dummy:
            temp=Node(dummy.val)
            temp.next=dummy.next
            dummy.next=temp
            dummy=temp.next
        # assign random pointers to the copy node
        dummy=head
        while dummy:
            if dummy.random:
                dummy.next.random=dummy.random.next
            dummy=dummy.next.next
        # restore the original list
        # extract the copy list
        original=head
        copy=head.next
        dummy=copy
        while original and copy:
            if original.next:
                original.next=original.next.next
            if copy.next:
                copy.next=copy.next.next
            original=original.next
            copy=copy.next
        return dummy
