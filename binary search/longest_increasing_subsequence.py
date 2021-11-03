# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      
        n=len(nums)
        lis=[nums[0]]
        i=1
        while i<n:
            if lis[-1]<nums[i]:
                lis.append(nums[i])
            
            else:
                # find the immediate next neighbour of nums[i]
                ind=bisect_left(lis, nums[i])
                lis[ind]=nums[i]
            i+=1
        
        return len(lis)
# Time complexity: O(nlogn), where n is the length of the array
# Space complexity: O(n)
