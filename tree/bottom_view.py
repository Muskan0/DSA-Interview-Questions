# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1#

class Solution:
    def bottomView(self, root):
        q=[[root, 0]]
        d=dict()
        ans=[]
        while q:
            node, x= q.pop(0)
            d[x]=node.data
            if node.left:
                q.append([node.left, x-1])
            if node.right:
                q.append([node.right, x+1])
        
        s=sorted(d.keys())
        for i in s:
            ans.append(d[i])
        
        return ans
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
