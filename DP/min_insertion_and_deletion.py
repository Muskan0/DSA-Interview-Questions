# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s1=word1
        s2=word2
        m=len(s1)
        n=len(s2)
        t=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    t[i][j]=t[i-1][j-1]+1
                else:
                    t[i][j]=max(t[i-1][j], t[i][j-1])
        return m-t[m][n] + n- t[m][n]
