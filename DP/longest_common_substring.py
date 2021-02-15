# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

'''
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1]
'''

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # same as longest common substring
        m=len(A)
        n=len(B)
        t=[[0 for i in range(n+1)] for j in range(m+1)]
        
        # 0th row and 0th column is already initiliazed
        
        # for max element
        max1=0
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1]==B[j-1]:
                    t[i][j]=t[i-1][j-1]+1
                else:
                    t[i][j]=0
                max1=max(max1, t[i][j])
        return max1
