# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        n=len(nums)
        for i in range(n):
            if target-nums[i] in l:
                return l[target-nums[i]],i
            else:
                l[nums[i]]=i
