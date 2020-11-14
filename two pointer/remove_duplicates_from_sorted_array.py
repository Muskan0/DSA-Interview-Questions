# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Remove the duplicates in-place returns the new length
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
# It doesn't matter what you leave beyond the returned length.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        j=0
        i=1
        while i<n:
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]
            i+=1
        return j+1
