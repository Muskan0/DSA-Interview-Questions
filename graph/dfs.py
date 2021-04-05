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



############################################
# dfs using stack
# https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/

def dfs(V,g,x):
        
        result=[]
        visited=[False for i in range(V+1)]        
        st=[]
        st.append(x)

        while st:
            node=st[-1]
            st.pop(-1)
            if not visited[node]:
                result.append(node)
                visited[node]=True
            for i in g[node]:

                if not visited[i]:
                    st.append(i)
        return len(result)

n,m=list(map(int, input().split()))
g={i:[] for i in range(1,n+1)}
for i in range(m):
    a,b=map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    
x=int(input())
print(abs(dfs(n,g,x)-n))
