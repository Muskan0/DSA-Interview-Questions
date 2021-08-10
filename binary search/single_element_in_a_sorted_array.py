# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-2
        
        # binary search
        while low<=high:
          
            mid=(low+high)>>1
            
            # for checking the left half
            # of the breakpoint
            # first instance of the element should be even
            # second instance of the element should be odd
            if nums[mid]==nums[mid^1]:
                low=mid+1
                
            else:
                high=mid-1
                
        return nums[low]
      
# Time Complexity: O(logn) for binary search
# Space Complexity: O(1)
