# https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1#

class Solution:
    def knapSack(self, n, W, val, wt):
        t=[[0 for i in range(W+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(W+1):
                if i==0 or j==0:
                    t[i][j]=0
        for i in range(n+1):
            for j in range(W+1):
                if wt[i-1]<=j:
                    t[i][j]=max(val[i-1]+t[i][j-wt[i-1]], t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
        return t[n][W]
