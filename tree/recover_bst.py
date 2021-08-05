# https://leetcode.com/problems/recover-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        global first
        global last
        global prev
        
        prev=None
        first=None
        last=None
        
        compute(root)
        
        # swapping the data of the nodes
        first.val, last.val = last.val, first.val
        return

# inorder traversal
def compute(root):
    global first
    global prev
    global last
    if root is None:
        return
    compute(root.left)
    
    if prev!=None:
        if prev.val>root.val:
            if first is None:
                # The first element is always larger than its next one
                first=prev 
            #the second element is always smaller than its previous one
            last=root
            
    prev=root
    compute(root.right)

# Time Complexity: O(n)
# Space complexity: O(h), h is height of the tree
