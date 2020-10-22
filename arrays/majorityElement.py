# https://leetcode.com/problems/majority-element/

# using Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        ele=-1
        n=len(nums)
        for i in range(n):
            if cnt==0:
                ele=nums[i]
            if nums[i]==ele:
                cnt+=1
            else:
                cnt-=1
        return ele
