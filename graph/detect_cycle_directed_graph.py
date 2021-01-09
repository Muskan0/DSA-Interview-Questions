# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1#

# We keep track of vertices currently in the recursion stack of function for DFS traversal. 
# If a vertex is reached that is already in the recursion stack, then there is a cycle in the tree.

# Time complexity: O(V+E), Space complexity: O(2*V)
import sys
sys.setrecursionlimit(10**6)
class Solution:
    def isCyclic(self, V, adj):
        visited=[False for i in range(V)]
        cycle=[False for i in range(V)]
        for j in range(0,V):
            if not visited[j]:
                if dfs(j, visited, cycle, adj)==True:
                    return True
        return False
        
def dfs(v, visited, cycle, graph):
    visited[v]=True
    cycle[v]=True
    for i in graph[v]:
        if not visited[i] and dfs(i, visited, cycle, graph):
            return True
        elif cycle[i]==True:
            return True
    cycle[v]=False
    return False
