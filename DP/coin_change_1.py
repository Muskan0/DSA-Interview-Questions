# https://practice.geeksforgeeks.org/problems/coin-change2448/1
# Given a value N, find the number of ways to make change for N cents, 
# if we have infinite supply of each of S = { S1, S2, .. , SM } valued coins.

class Solution:
    def count(self, S, m, n): 
        t=[[0 for i in range(n+1)] for j in range(m+1)]
        # initialisation
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    t[i][j]=0
                if j==0:
                    t[i][j]=1
                    
        for i in range(1,m+1):
            for j in range(1,n+1):
                if S[i-1]<=j:
                    t[i][j]=t[i-1][j]+t[i][j-S[i-1]]
                else:
                    t[i][j]=t[i-1][j]
                    
        return t[m][n]
