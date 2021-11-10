# https://practice.geeksforgeeks.org/problems/burning-tree/1#

class Solution:
    def minTime(self, root,target):
        target=findNode(root, target)
        parent = dict()
        parent[root]=None
        q=[root]
        while q:
            node=q.pop(0)
            if node.left:
                parent[node.left]=node
                q.append(node.left)
            if node.right:
                parent[node.right]=node
                q.append(node.right)

        q=[target]
        time=0
        visited=dict()
        
        while q:
            size= len(q)
            time+=1
            for i in range(size):
                node=q.pop(0)
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited[node.left]=True
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited[node.right]=True
                if node != root:
                    if parent[node] not in visited:
                        q.append(parent[node])
                        visited[parent[node]]=True
     
        return time-1
                
def findNode(root, target):
    if root is None:
        return None
    
    if root.data==target:
        return root
    
    return findNode(root.left, target) or findNode(root.right, target)

# Time Complexity: O(N)
# Space Complexity: O(N)
