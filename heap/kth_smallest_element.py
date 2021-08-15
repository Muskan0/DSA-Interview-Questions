# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1

from heapq import heappop, heappush, heapify
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        
        heap=[]
        heapify(heap)
        
        for i in range(l,r+1):
            # pushing -1*element, so as to make it a max heap
            # and size of heap should not exceed k
            # so after traversing the whole array,
            # the top element of the heap will give kth smallest
            # element.
            
            heappush(heap, -1*arr[i])
            
            if len(heap)>k:
                heappop(heap)
        
        ans=heappop(heap)
        return ans*-1
      
# Time Complexity: O(n*logk)
# Space Complexity: O(k+1)
