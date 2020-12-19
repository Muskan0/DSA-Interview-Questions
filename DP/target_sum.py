# https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # count the number of subset of a given difference
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            if abs(nums[0])==abs(S):
                return 1
            else:
                return 0
        ls=sum(nums)
        if ls<abs(S) or (ls+S)%2!=0:
            return 0
        
        # handling zero in array
        c=0
        for i in nums:
            if i==0:
                c+=1
        ns=[]
        i=0
        while i<n:
            if nums[i]!=0:
                ns.append(nums[i])
            i+=1
        nums=ns
        
        n=len(nums)
        s1=(S+ls)//2
        # finding count of subset sum with a given sum
        t=[[0 for i in range(s1+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(s1+1):
                if i==0:
                    t[i][j]=0
                if j==0:
                    t[i][j]=1
        for i in range(1,n+1):
            for j in range(1, s1+1):
                if nums[i-1]==0:
                    t[i][j]=t[i-1][j]
                if nums[i-1]<=j:
                    t[i][j]=t[i-1][j-nums[i-1]]+t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        #print(t)
        return (2**c)*t[n][s1]
