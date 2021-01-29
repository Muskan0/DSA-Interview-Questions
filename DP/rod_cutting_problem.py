# https://practice.geeksforgeeks.org/problems/rod-cutting/0#
# it's a similar problem like unbounded knapsack problem

for _ in range(int(input())):
    n=int(input())
    length=[i for i in range(1,n+1)]
    price=list(map(int, input().split()))
    t=[[-1 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if length[i-1]<=j:
                t[i][j]=max(price[i-1]+t[i][j-length[i-1]], t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    print(t[n][n])
