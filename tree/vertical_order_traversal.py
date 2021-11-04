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


=======================================================================================================

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[[root, 0, 0]]
        d=dict()
        while q:
            node=q.pop(0)
            x=node[1]
            y=node[2]
            if x not in d:
                d[x]=dict()
            if y not in d[x]:
                d[x][y]=[]
            
            d[x][y].append(node[0].val)
            
            if node[0].left!=None:
                q.append([node[0].left, x-1, y+1])
            if node[0].right!=None:
                q.append([node[0].right, x+1, y+1])
        ans=[]
        s=sorted(d.keys())
        for vertical in s:
            temp=[]
            for level in d[vertical].keys():
                temp.extend(sorted(d[vertical][level]))
            ans.append(temp)
        return ans
        
# Time Complexity: O(nlogn), where n is no of nodes in binary tree
# Space Complexity: O(n)
