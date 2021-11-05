# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q=[root]
        parent=dict()
        parent[root]=None
        
        while q:
            node=q.pop(0)
            if node.left:
                q.append(node.left)
                parent[node.left]=node
                
            if node.right:
                q.append(node.right)
                parent[node.right]=node
                
        q=[target]
        visited=dict()
        visited[target]= True
        while k>0:
            k-=1
            size=len(q)
            
            for i in range(0, size):
                node=q.pop(0)
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited[node.left]=True
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited[node.right]=True
                if parent[node] and parent[node] not in visited:
                    q.append(parent[node])
                    visited[parent[node]]=True
        ans=[]
        while q:
            temp=q.pop(0)
            ans.append(temp.val)
        return ans
# Time Complexity: O(N), N is no of nodes in the binary tree
# Space Complexity: O(N)
