# https://www.interviewbit.com/problems/0-1-knapsack/

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        N=len(A)
        l=[[-1 for i in range(C+1)] for j in range(N+1)]
        # initialisation
        for i in range(N+1):
            for j in range(C+1):
                if i==0 or j==0:
                    l[i][j]=0
        
        for i in range(1, N+1):
            for j in range(1, C+1):
                if B[i-1]<=j:
                    l[i][j] = max(A[i-1] + l[i-1][j-B[i-1]], l[i-1][j])
                else:
                    l[i][j] = l[i-1][j]
        return l[N][C]
