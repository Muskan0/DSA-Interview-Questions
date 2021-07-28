# https://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/

def printCloset(arr1, arr2, k):
  
    n=len(arr1)
    m=len(arr2)
    i=0
    j=m-1
    diff=float("inf")
    res=[]
    while i<n and j>=0:
        if abs(arr1[i]+arr2[j]-k)<diff:
            res=[arr1[i], arr2[j]]
            diff=abs(arr1[i]+arr2[j]-k)
        
        if arr1[i]+arr2[j]<k:
            i+=1
        else:
            j-=1
    return res

arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
k=int(input())
ans=printCloset(arr1,arr2,k)
print(ans[0], ans[1])

# Time Complexity: O(n)
# Space Complexity: O(1)
