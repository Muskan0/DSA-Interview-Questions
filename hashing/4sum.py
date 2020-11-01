# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        if n==0:
            return []
        i=j=0
        left=0
        right=0
        l=[]
        nums.sort()
        while i<n:
            j=i+1
            while j<n:
                target2=target-nums[i]-nums[j]
                left=j+1
                right=n-1
                while left<right:
                    twosum=nums[left]+nums[right]
                    if twosum>target2:
                        right-=1
                    elif twosum<target2:
                        left+=1
                    else:
                        temp=[]
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[left])
                        temp.append(nums[right])
                        l.append(temp)
                        # increasing the left index so that we don't get nums[left] duplicate
                        while left<right and nums[left]==temp[2]:
                            left+=1
                        # processing the right index
                        while left<right and nums[right]==temp[3]:
                            right-=1
                while j+1<n and nums[j+1]==nums[j]:
                    j+=1
                j+=1
            while i+1<n and nums[i+1]==nums[i]:
                i+=1
            i+=1
        return l
