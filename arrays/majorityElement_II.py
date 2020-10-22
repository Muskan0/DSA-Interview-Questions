# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=c2=0
        n1=n2='x'
        n=len(nums)
        for i in range(n):
            
            if nums[i]==n1:
                c1+=1
            elif nums[i]==n2:
                c2+=1
            elif c1==0:
                n1=nums[i]
                c1=1
            elif c2==0:
                n2=nums[i]
                c2=1
            
            else:
                c1-=1
                c2-=1
        s1=0
        s2=0
        for i in nums:
            if i == n1:
                s1+=1
            if i == n2:
                s2+=1
        ans=[]
        if s1>n//3:
            ans.append(n1)
        if s2>n//3:
            ans.append(n2)
        return ans
            
            
                
            
