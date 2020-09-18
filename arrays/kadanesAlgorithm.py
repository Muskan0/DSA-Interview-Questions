# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxEndingHere=maxSoFar=nums[0]
        for i in nums[1:]:
            maxEndingHere=max(maxEndingHere+i, i)
            maxSoFar=max(maxSoFar, maxEndingHere)
        return maxSoFar
