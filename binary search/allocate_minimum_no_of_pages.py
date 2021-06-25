# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1#

class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,arr, n, m):
        
        def allocatePages(no):
            allocSt=1
            pages=0
            for i in range(n):
                if pages+arr[i]>no:
                    pages=arr[i]
                    allocSt+=1
                else:
                    pages+=arr[i]
            #print(allocSt)
            if allocSt<=m:
                return True
            else:
                return False
                
        low=max(arr)
        high=sum(arr)
        while low<=high:
            mid=(low+high)//2
            if allocatePages(mid):
                
                high=mid-1
            else:
                low=mid+1
        return low
    
    # Time Complexity: O(n*logn),
    # binary search takes logn and allocatePages() take O(n)
    # Space complexity: O(1)
