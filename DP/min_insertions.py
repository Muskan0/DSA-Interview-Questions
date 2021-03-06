# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution:
    def minInsertions(self, s: str) -> int:
        s1=s[::-1]
        n=len(s)
        
        t=[[0 for i in range(n+1)] for j in range(n+1)]
        # 0th row and 0th column already initialized with 0
        
        # Longest Palindromic Subsequence
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==s1[j-1]:
                    t[i][j]=t[i-1][j-1]+1
                else:
                    t[i][j]=max(t[i-1][j], t[i][j-1])
                    
        return n-t[n][n]
'''
This problem is same as the 
https://github.com/Muskan0/DSA-Interview-Questions/blob/master/DP/min_deletions.py

Minimum no of deletions= Minimum no of insertions = Length of string - Longest Palindromic Subsequence
'''
