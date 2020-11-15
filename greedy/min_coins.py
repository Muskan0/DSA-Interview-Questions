# https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/
# my solution-

def minCoins(n):
    denomination=[1, 2, 5, 10, 20, 50, 100, 500, 1000]
    i=len(denomination)-1
    ans=[]
    while i>=0:
        while denomination[i]<=n:
            n-=denomination[i]
            ans.append(denomination[i])
        i-=1
    return ans


n=93
print(minCoins(n))

'''
Output:
[50, 20, 20, 2, 1]
'''
