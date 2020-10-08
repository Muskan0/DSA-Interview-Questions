# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        n=len(prices)
        if n==0:
            return 0
        minPrice=prices[0]
        
        for i in range(1,n):
            if prices[i]<minPrice:
                minPrice=prices[i]
            ans=max(ans, prices[i]-minPrice)
        return ans
            
        
        
