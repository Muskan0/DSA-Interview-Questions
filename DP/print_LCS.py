# https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem

# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    m=len(a)
    n=len(b)
    # tabulate LCS
    t=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j], t[i][j-1])
    # print LCS
    i=m
    j=n
    ans=[]
    while i and j:
        if a[i-1]==b[j-1]:
            ans.append(a[i-1])
            i-=1
            j-=1
        else:
            if t[i-1][j]>t[i][j-1]:
                i-=1
            else:
                j-=1
    return ans[::-1]
