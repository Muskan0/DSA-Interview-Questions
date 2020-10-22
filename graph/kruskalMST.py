# Kruskal's Algorithm

class Graph:
    def __init__(self,V):
        self.V=V
        self.g=[]
        
    def addEdge(self, a,b,c):
        self.g.append([a,b,c])
        
    def find(self, p, i):
        if p[i]==i:
            return i
        return self.find(p,p[i])
        
    def union(self, rank, p, x,y):
        xroot=self.find(p,x)
        yroot=self.find(p,y)
        if rank[xroot]>rank[yroot]:
            p[yroot]=xroot
        elif rank[xroot]<rank[yroot]:
            p[xroot]=yroot
        else:
            p[xroot]=yroot
            rank[yroot]+=1
            
    def kruskal(self):
        rank=[]
        p=[]
        edge=0
        for i in range(self.V):
            p.append(i)
            rank.append(0)
        self.g.sort(key=lambda x: x[2])
        i=0
        r=[]
        while edge<self.V-1:
            a,b,c=self.g[i]
            i=i+1
            k=self.find(p,a)
            m=self.find(p,b)
            if k!=m:
                r.append([a,b,c])
                edge+=1
                self.union(rank, p, k,m)
        r.sort(key=lambda x : x[2])
        return r

graph= Graph(4)
graph.addEdge(0, 1, 10) 
graph.addEdge(0, 2, 6) 
graph.addEdge(0, 3, 5) 
graph.addEdge(1, 3, 15) 
graph.addEdge(2, 3, 4) 
print(graph.kruskal())
