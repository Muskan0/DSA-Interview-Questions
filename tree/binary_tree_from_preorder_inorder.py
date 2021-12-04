# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(preorder)
        inDict= dict()
        for i in range(0,n):
            inDict[inorder[i]]=i
        return self.util(preorder, inorder, 0, n-1, 0, n-1, inDict)
    
    def util(self, preorder, inorder, preStart, preEnd, inStart, inEnd, inDict):
        if preStart>preEnd or inStart>inEnd:
            return None
        root=TreeNode(preorder[preStart])
        mid=inDict[root.val]
        numsLeft=mid-inStart
        root.left=self.util(preorder,inorder, preStart+1, preStart+numsLeft, inStart, inStart+numsLeft-1, inDict)
        root.right=self.util(preorder, inorder, preStart+numsLeft+1, preEnd  ,mid+1, inEnd, inDict )
        return root
      
# Time Complexity: O(N)
# Space Complexity: O(N)
