# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return False
        s=sum(nums)
        if s%2!=0:
            return False
        else:
            s//=2
            t = [[-1 for i in range(s+1)] for j in range(n+1)]
            
            for i in range(0,s+1):
                t[0][i]= False
            
            for i in range(n+1):
                t[i][0] = True
                                
            for i in range(1,n+1):
                for j in range(1,s+1):
                    if nums[i-1] <=j:
                        t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]
                    else:
                        t[i][j] = t[i-1][j]
            return t[n][s]
        
