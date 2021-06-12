# https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time complexity: O(h), space complexity: O(h)
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if key<root.val:
            root.left=self.deleteNode(root.left, key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        # key found
        else:
            # no children
            if root.left is None and root.right is None:
                return None
            # no left child
            elif root.left is None:
                return root.right
            # no right child
            elif root.right is None:
                return root.left
            # both left and right child
            else:
                node=minValue(root.right) #finding the minimum value in the right subtree
                root.val=node.val
                root.right=self.deleteNode(root.right, root.val)
        return root
                
               
def minValue(node):
    current=node
    while current.left:
        current=current.left
    return current
