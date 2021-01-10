# https://www.hackerearth.com/problem/algorithm/connected-components-in-a-graph/description/

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def DFS(self, visited, v):
        visited[v]=True
        for i in self.graph[v]:
            if not visited[i]:
                self.DFS(visited,i)
        return
        
g=Graph()
n,e=list(map(int, input().split()))
for i in range(e):
    a,b=list(map(int, input().split()))
    g.addEdge(a,b)
ans=0
visited=[False for i in range(0,n+1)]

for i in range(1,n+1):
    if not visited[i]:
        # no of connected components are just the
        # no of times Dfs function is called from here
        g.DFS(visited,i)
        ans+=1
print(ans)
