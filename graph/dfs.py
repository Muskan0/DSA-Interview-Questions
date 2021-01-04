# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

'''
g : adjacency list of graph
N : number of vertices

return a list containing the DFS traversal of the given graph
'''
# dfs starting from node 0
def dfs(g,N):
    def dfsUtil(g,v,visited):
        visited[v]=True
        result.append(v)
        for i in g[v]:
            if not visited[i]:
                dfsUtil(g,i,visited)
                
    result=[]
    visited=[False for i in range(N)]
    dfsUtil(g,0,visited)
    return result


# TAKUFORWARD DFS video: https://youtu.be/_GstINcASBI
