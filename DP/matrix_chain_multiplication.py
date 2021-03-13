# https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1#

'''
Given a sequence of matrices, find the most efficient way to multiply these matrices together. 

Input: arr= [10, 20, 30, 40, 30]
Output: 30000 
There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30. 
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30
Note: The problem statement source is from geeksforgeeks
'''

class Solution:
    def matrixMultiplication(self, N, arr):
        def mcm(arr, i,j):
            # base condition
            if(i>=j):
                return 0
              
            if t[i][j]!=-1:
                return t[i][j]
              
            mn=float("inf")
            
            # calculate the count of multiplications
            # by placing the parenthesis at different places
            # i<=k<=j-1
            for k in range(i,j):
                temp= mcm(arr,i,k)+mcm(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
                mn=min(mn,temp)
            
            t[i][j]=mn
            
            return t[i][j]
        
        t=[[-1 for i in range(N)] for j in range(N)]
        return mcm(arr,1,N-1)
      
      
