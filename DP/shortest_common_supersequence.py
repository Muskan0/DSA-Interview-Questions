# https://practice.geeksforgeeks.org/problems/shortest-common-supersequence0322/1#
'''
Input:
X = abcd, Y = xycd
Output: 6
Explanation: Shortest Common Supersequence
would be abxycd which is of length 6 and
has both the strings as its subsequences.
'''

def shortestCommonSupersequence(X, Y, m, n):
    # return: the length of the required string.
    t=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j], t[i][j-1])
    # size of array X + size of array Y - LCS
    return m+n-t[m][n]
