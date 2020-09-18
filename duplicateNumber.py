# https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise=nums[0]
        hare=nums[0]
        while True:
            tortoise=nums[tortoise]
            hare=nums[nums[hare]]
            if tortoise==hare:
                break
        hare=nums[0]
        while tortoise!=hare:
            tortoise=nums[tortoise]
            hare=nums[hare]
        return tortoise
