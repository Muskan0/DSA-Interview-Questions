# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1#

# using depth first search

# to detect cycle in subgraph reachable from node. 
def dfs(g,visited, node, parent):
    visited[node]=True
    # recur for it's adjacent vertices
    for i in g[node]:
        if not visited[i]:
            if(dfs(g,visited,i,node)):
                return True
        # if adjacency vertex is visited and not parent
        # then there is a cycle
        elif i!=parent:
            return True
    return False
            
def isCyclic(g,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    visited= [False for i in range(n)]
    # calling function to detect cycles in unconnected graph
    for i in range(n):
        if not visited[i]:
            if dfs(g,visited,i, -1):
                return 1
    return 0
