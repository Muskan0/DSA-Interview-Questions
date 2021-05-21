# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root.val==p.val or root.val==q.val:
            return root
          
        left= self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        
        if left is None:
            return right
        if right is None:
            return left
        return root
      
    # Time complexity: O(N) in worst case if we have to visit all the nodes
    # Space complexity: O(N) in worst case for recursion stack if the binary tree is skewed
