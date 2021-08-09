# https://www.spoj.com/problems/AGGRCOW/

def canPlaceCowhere(stall,N,C,dist):
    co_ord=stall[0]
    count=1
    for i in range(1,N):
        if stall[i]-co_ord>=dist:
            count+=1
            co_ord=stall[i]
        if count==C:
            return True
    return False
    

for _ in range(int(input())):
    N,C=map(int, input().split())
    stall=[0 for i in range(N)]
    for i in range(N):
        stall[i]=int(input())
    
    stall.sort()
    
    minDist=1
    
    # binary search
    low=1
    high=stall[N-1]-stall[0]
    
    while low<=high:
        mid=(low+high)//2
        if(canPlaceCowhere(stall,N,C,mid)):
            minDist=mid
            low=mid+1
        else:
            high=mid-1
    print(minDist)
    
    
'''
Time complexity: O(N*logk), where k is search space 
of binary search from 1 to stall[N-1]-stall[0] 
and canPlaceCowhere function takes O(N) space.

Space Complexity: O(1)
'''
