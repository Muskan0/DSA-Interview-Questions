# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None       
'''
def merge(a,b):
    # dummy node
    res=Node(0)
    temp=res
    # merging the two linkedlists
    while a and b:
        if a.data> b.data:
            temp.bottom=b
            temp=temp.bottom
            b=b.bottom
        else:
            temp.bottom=a
            temp=temp.bottom
            a=a.bottom
    if a!=None:
        temp.bottom=a
    if b!=None:
        temp.bottom=b
    return res.bottom

def flatten(root):
    
    if root is None or root.next is None:
        return root
      
    # recur for linkedlist on right
    root.next=flatten(root.next)
    # merge
    root=merge(root,root.next)
    # return the root after merging
    # it will be merged with it's left linked list nodes
    return root
