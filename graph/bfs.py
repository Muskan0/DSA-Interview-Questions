# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

'''
*  g[]: adj list of the graph
*  N : number of vertices
'''
# bfs starting from zero
def bfs(g,N):
    # code here
    # O(V+E) time complexity, O(V) space complexity
    bfs=[]
    visited=[False for i in range(N)]
    queue=[0]
    while queue:
        node=queue.pop(0)
        bfs.append(node)
        
        for i in g[node]:
            if not visited[i]:
                visited[i]= True
                queue.append(i)
    return bfs
