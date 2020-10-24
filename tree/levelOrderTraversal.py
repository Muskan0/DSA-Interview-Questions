# https://leetcode.com/problems/binary-tree-level-order-traversal/ 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return root
        q=[]
        q.append(root)
        ans=[]
        while q:
            m=len(q)
            level=[]
            for i in range(m):
                g=q.pop(0)
                level.append(g.val)
                if g.left:
                    q.append(g.left)
                if g.right:
                    q.append(g.right)
            ans.append(level)
        return ans
