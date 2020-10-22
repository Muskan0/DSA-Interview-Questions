# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0#

class Activity(object):
    def __init__(self, start, finish, index):
        self.start=start
        self.finish=finish
        self.index=index
for i in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    f=list(map(int, input().split()))
    l=[]
    for i in range(n):
        l.append(Activity(s[i],f[i],i))
    l.sort(key=lambda x: x.finish)   
    i=0
    print(l[i].index+1, end=" ")
    for j in range(1,n):
        if l[j].start>=l[i].finish:
            print(l[j].index+1,end=" ")
            i=j
    print()
