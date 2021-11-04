# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1#

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        q=[[root, 0]]
        d=dict()
        while q:
            node, x= q.pop(0)
            if x not in d:
                d[x]= node.data
            if node.left:
                q.append([node.left, x-1])
            if node.right:
                q.append([node.right, x+1])
        ans=[]
        s=sorted(d.keys())
        for i in s:
            ans.append(d[i])
        return ans
# Time complexity: O(nlogn)
# Space complexity: O(2n)
# where n is the no of nodes in the given binary tree
