# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        arr=[]
        # traverse the tree
        func(arr,root,0,0)
        # sort the array
        arr.sort(key= lambda x:[x[0],x[1],x[2]])
        
        n=len(arr)
        ans=[[arr[0][2]]]
        # vertical order traversal
        for i in range(1,n):
            if arr[i-1][0]==arr[i][0]:
                ans[-1].append(arr[i][2])
            else:
                ans.append([arr[i][2]])
        return ans
    
def func(arr,node,x,y):
    if node is None:
        return
    if node.left:
        func(arr,node.left,x+1,y-1)
    # store x, y and value of the node
    # x and y are the coordinates of the node
    arr.append([y,x,node.val])
    if node.right:
        func(arr,node.right,x+1,y+1)
    return
        
# Time complexity: O(nlogn)
# Space complexity: O(n)
