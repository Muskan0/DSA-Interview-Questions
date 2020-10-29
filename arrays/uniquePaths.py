# https://leetcode.com/problems/unique-paths/

# using combinatorics
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        l=m+n-2
        r=m-1
        res=1
        for  i in range(0,r):
            res*=(l-i)
            res//=i+1
        return res
# using recursion with memoization
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for i in range(n)] for j in range(m)]
        #print(n)
        #print(m)
        #print(dp)
        return uniquePaths1(0,0,m,n,dp )

def uniquePaths1(i,j,m,n,dp):
    if (i==m-1) and (j==n-1):
        return 1
    if i>=m or j>=n:
        return 0
    if dp[i][j]!=0:
        return dp[i][j]
    else:
        dp[i][j]= uniquePaths1(i+1, j, m,n, dp)+uniquePaths1(i,j+1, m,n, dp)
        return dp[i][j]
'''

