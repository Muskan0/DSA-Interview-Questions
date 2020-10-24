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
