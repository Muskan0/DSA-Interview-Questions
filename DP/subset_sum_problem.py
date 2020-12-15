# https://www.interviewbit.com/problems/subset-sum-problem/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n=len(A)
        t=[[-1 for i in range(B+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(B+1):
                if i==0:
                    t[i][j] = 0
                if j==0:
                    t[i][j] = 1
                    
        for i in range(1, n+1):
            for j in range(1, B+1):
                if A[i-1] <= j:
                    t[i][j] = (t[i-1][j-A[i-1]]) or t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][B]
