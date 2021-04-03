#dijkstra's algorithm
import datetime
import time
n=int(input("Enter the number of vertices"))
# start=time.time()
V=set()
for i in range(1,n+1):
    V.add(i)
#input
l=[]
for i in range(n):
    temp=input().split()
    t=set()
    tp=[]
    tp.append(int(temp[0]))
    del temp[0]
    for j in temp:
        tp.extend([int(x) for x in j.split(",")])
        t.add(tuple(tp))
        tp=tp[0:1]
    l.append(t)
processed=set()
#source vertex 1
processed.add(1)
#processed path length
path=dict()
path[1]=0
#Djikstra's algorithm
while processed!=V:
    tpp=set()
    m,pr=-1,-1
    for p in V:
        if tpp==processed:
            break
        if p in processed:
            tpp.add(p)
            for q in l[p-1]:
                if q[1] not in processed:
                    if m==-1:
                        m=q[2]+path[q[0]]
                        pr=q[1]
                    elif m>q[2]+path[q[0]]:
                        m=q[2]+path[q[0]]
                        pr=q[1]
    path[pr]=m
    processed.add(pr)
print(path)
# print(time.time()-start)



########################################################################################

# using heap
# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        def dijkstra(graph, V):
            d=[float("inf") for i in range(V+1)]
            d[k]=0
            l=[[0]]
            l[0].append(k)
            while l:
                temp=heapq.heappop(l)
                u=temp[1]
                for i in graph[u]:
                    v=i[0]
                    w=i[1]
                    if d[v]> d[u]+w:
                        if d[v]!=float('inf'):
                            if [d[v],v] in l:
                                l.remove([d[v],v])
                        d[v]=d[u]+w
                        l.append([d[v],v])
           
            for i in d[1:]:
                if i==float('inf'):
                    return -1
            return max(d[1:])

        
        di={i:[] for i in range(1,n+1)}
        for i in times:
            u,v,w=i[0],i[1],i[2]
            di[u].append([v,w])

        return dijkstra(di,n)
# time complexity: O(ElogV)
# space complexity: E+V + V, E+V is to store the graph and V is worst case space complexity for heap= O(2*V + E)
