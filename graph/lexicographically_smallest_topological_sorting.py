# https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/tutorial/

# Topological sorting for Directed Acyclic Graph is a linear ordering of vertices 
# such that for every directed edge uv, vertex u comes before v in the ordering
# Topological sorting for a graph is not possible if the graph is not a DAG.

# Topological sorting starts from node with no edges directed to it


from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self, u, v): 
        self.graph[u].append(v)
    def dfs(self, v,visited,stack):
        visited[v]=True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i,visited,stack)
        stack.append(v)
    def topoSort(self,n):
        visited=[False for i in range(n+1)]
        stack=[]
        i=n
        while i>=1:
            if not visited[i]:
                self.dfs(i,visited,stack)
            i-=1
        return stack[::-1] 

g=Graph()
n,m=list(map(int, input().split()))
k=[]
for i in range(m):
    x,y=list(map(int, input().split()))
    k.append([x,y])
k.sort(reverse=True)
for i in k:
    g.addEdge(i[0],i[1])
l=g.topoSort(n)
for i in l:
    print(i,end=" ")
print()

# https://discuss.codechef.com/t/find-lexicographically-smallest-topological-sort-of-a-directed-acyclic-graph/62690
