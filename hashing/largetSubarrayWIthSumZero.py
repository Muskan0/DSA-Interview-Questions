# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#
# https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/

def maxLen(n, arr):
    #Code here
    ans=0
    d=dict()
    s=0
    for i in range(n):
        s+=arr[i]
        if s==0:
            ans=i+1
        if s not in d:
            d[s]=i
        else:
            ans=max(i-d[s],ans)
    return ans
