# https://www.hackerearth.com/practice/algorithms/graphs/strongly-connected-components/tutorial/
# directed graph is strongly conected if there is a path between all pairs of vertices

'''
Step 1-
1. Sort them according to their finishing times
2. Do DFS, when the DFS is completed for a given node, push the node into a stack.
Step2 -
Transpose the graph
Step 3-
DFS Traversal for nodes in stack
'''

import sys
sys.setrecursionlimit(10**6)

n,m=list(map(int, input().split()))
g={i:[] for i in range(1,n+1)}
visited=[False for i in range(n+1)]
for i in range(m):
    a,b=map(int, input().split())
    g[a].append(b)
# step 1
st=[]
def dfs(node):
    visited[node]=True
    for i in g[node]:
        if not visited[i]:
            dfs(i)
    st.append(node)
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
#print(st)
# step 2
g1={i:[] for i in range(1,n+1)}
for i in range(1,n+1):
    for j in g[i]:
        g1[j].append(i)

# step 3
def dfs1(nd,k):
    visited[nd]=True
    k+=1
    for i in g1[nd]:
        if not visited[i]:
            return dfs1(i,k)
    return k
    
m=[]
visited=[False for i in range(n+1)]
while st:
    nd=st.pop(-1)
    if not visited[nd]:
        k=0
        k=dfs1(nd,k)
        m.append(k)

c=0
d=0
for i in m:
    if i%2==0:
        c+=i
    else:
        d+=i
print(d-c)

'''
Time complexity: O(V+E), for DFS traversals
Space Complexity: O(V+E)(for adjacency list) +O(V)(for stack)
'''
