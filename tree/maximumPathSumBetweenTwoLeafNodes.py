# https://practice.geeksforgeeks.org/problems/maximum-path-sum/1#

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
def solve(root,res):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
        
    left=solve(root.left, res)
    right=solve(root.right, res)
    
    if root.left and root.right:
        temp=max(left,right)+root.data
        res[0]=max(res[0],left+right+root.data)
        return temp
    # We will have to consider the cases of whether the left and right subtrees exist
    # otherwise consider left= 0(0 is returned when it is None), right= -5, this will case error in max(left, right)
    # where the left subtree doesn't even exists
    if root.left is None:
        return right+root.data
    elif root.right is None:
        return left+root.data
        
def maxPathSum(root):
    res=[float("-inf")]
    solve(root, res)
    
    return res[0]
  
# Time Complexity: O(n) where n is number of nodes in Binary Tree.
