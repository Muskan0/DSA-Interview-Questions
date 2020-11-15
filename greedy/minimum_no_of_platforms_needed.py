# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    arr.sort()
    dep.sort()
    ans=0
    j=m=0
    i=0
    while i<n and j<n:
        if arr[i]<=dep[j]:
             i+=1
             m+=1
        else:
            j+=1
            m-=1
        ans=max(ans,m)
    return ans
