# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1
# Merge two sorted Arrays without extra space
import math
from sys import stdin, stdout  
for _ in range(int(input())):
    x,y=[int(x) for x in stdin.readline().split()]
    p=[int(x) for x in stdin.readline().split()]
    q=[int(x) for x in stdin.readline().split()]
    gap=math.ceil((x+y)//2)
    
    while gap>0:
        i=0
        #print(gap)
        while i+gap<x:
            if p[i]>p[i+gap]:
                p[i+gap],p[i]=p[i],p[i+gap]
            i+=1
        #print(p)
        if gap>x:
            j=gap-x
        else:
            j=0
        while i<x and j<y:
            if p[i]>q[j]:
                p[i],q[j]=q[j],p[i]
            i+=1
            j+=1
        if j<y:
            j=0
            while j+gap<y:
                if q[j]>q[j+gap]:
                    q[j+gap],q[j]=q[j],q[j+gap]
                j+=1
        gap//=2
    #print(p)
    #print(q)
    for i in range(x):
        print(p[i],end=" ")
    for i in range(y):
        print(q[i],end=" ")
    print()
                
