# https://leetcode.com/problems/binary-tree-inorder-traversal/

'''
# using recursion

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root,res):
            if root:
                if root.left:
                    helper(root.left, res)
                res.append(root.val)
                if root.right:
                    helper(root.right, res)    
        res=[]
        helper(root,res)
        return res
 '''
 '''
 # iterative method, using stack
 
 class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        stack=[]
        curr= root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            
            curr=stack.pop(-1)
            res.append(curr.val)
            curr=curr.right
            
        return res
'''

# Morris Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # O(n) time, O(1) space
        res=[]
        curr=root
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr=curr.right
            else:
                pre=curr.left
                while pre.right:
                    pre=pre.right
                pre.right=curr
                temp=curr
                curr=curr.left
                temp.left=None
        return res
        
 '''
 Inorder Morris Tree Traversal Algorithm
 
Step 1: Initialize current as root

Step 2: While current is not NULL,

If current does not have left child

    a. Add current’s value

    b. Go to the right, i.e., current = current.right

Else

    a. In current's left subtree, make current the right child of the rightmost node

    b. Go to this left child, i.e., current = current.left
 '''
