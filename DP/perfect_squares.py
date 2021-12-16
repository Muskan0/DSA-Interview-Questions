# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        '''
        This question is similar to longest increasing subsequence.
        '''
        dp=[0 for i in range(n+1)]
        dp[0]=0;
        dp[1]=1;
        
        for i in range(2,n+1):
            j=1
            minValue=100000
            while j*j<=i:
                rem=i-j*j
                if minValue>dp[rem]:
                    minValue=dp[rem]
                j+=1
            dp[i]=minValue+1
    
        return dp[n]

# Time Complexity: O(n*sqrt(n))
# Space Complexity: O(n)
