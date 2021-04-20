# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Dp on trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def solve(root,res):
            if root is None:
                return 0
            l=solve(root.left,res)
            r=solve(root.right,res)
            
            temp=max(max(l,r)+root.val, root.val)
            ans=max(temp, l+r+root.val)
            res[0]=max(res[0], ans)
            
            return temp
          
        # initializing as a list for 
        # passing it as a reference, list is a mutable object
        res=[float("-inf")]
        solve(root, res)
        return res[0]
# Time complexity: O(N), one traversal through the tree
