# https://www.geeksforgeeks.org/minimum-number-deletions-make-string-palindrome/

from sys import stdin, stdout
for _ in range(int(stdin.readline())):
    s1 = input()
    # reverse of s1
    s2 = s1[::-1]
    n=len(s1)
    # LCS for finding palindromic subsequence
    t = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = t[i-1][j-1] + 1
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    # min no deletions = 
    # length of string - longest palindromic subsequence
    stdout.write(str(n - t[n][n])+"\n")
