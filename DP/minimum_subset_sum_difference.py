# https://www.interviewbit.com/problems/minimum-difference-subsets/

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        range1=sum(A)
        s=range1
        n=len(A)
        if n==1:
            return s
        s=s//2
        t=[[0 for i in range(s+1)] for j in range(n+1)]
        for i in range(0,n+1):
            for j in range(0,s+1):
                if i==0:
                    t[i][j]= False
                if j==0:
                    t[i][j]= True
        
        for i in range(1, n+1):
            for j in range(1, s+1):
                if A[i-1]<=j:
                    t[i][j] = t[i-1][j-A[i-1]] or t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        m=2*s
        for i in range(s+1):
            if t[n][j] == True:
                m=j
        return range1 - 2*j
