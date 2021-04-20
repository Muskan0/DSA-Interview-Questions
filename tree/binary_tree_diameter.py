# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1#
# Dp on Trees

class Solution:
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        def solve1(root,res):
            if root is None:
                return 0
            
            l=solve1(root.left,res)
            r=solve1(root.right,res)
            
            temp=max(l,r)+1
            res[0]=max(res[0],1+l+r)        
            return temp
        res=[0]
        solve1(root,res)
        return res[0]
      
# Time complexity: O(N)
