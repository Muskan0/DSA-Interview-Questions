# https://practice.geeksforgeeks.org/problems/negative-weight-cycle3504/1#

class Solution:
    def isNegativeWeightCycle(self, n, g):
        d=[float('inf') for i in range(n+1)]
        d[1]=0
        for i in range(n-1):
            for u,v,w in g:
                
                if d[u]+w<d[v]:
                    d[v]=d[u]+w
        
        for u,v,w in g:
            if  d[u]+w<d[v]:
                return 1
        
        return 0
        
# time complexity: O(NE)
# space complexity: O(N+E) for storing adjacency list
