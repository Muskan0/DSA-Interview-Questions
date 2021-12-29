# https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        n=len(nums)
        hashMap= dict()
        hashMap[0]=1
        
        sumSub=0
        countSubarray=0
        for i in range(n):
            sumSub+=nums[i]
            mod=(sumSub%k+k)%k
            
            if mod in hashMap:
                #print(hashMap)
                countSubarray+=hashMap[mod]
                hashMap[mod]+=1
            else:
                hashMap[mod]=1
            
        return countSubarray
        
  
