# https://leetcode.com/problems/coin-change/
# compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        t=[[0 for j in range(amount+1)] for i in range(n+1)]
        
        # t[1][0]...t[n][0] already initialised to 0
        
        # initiaization for first row
        for i in range(amount+1):
            t[0][i]=float('inf')
            
        # initialisation of second row..
        for i in range(1,amount+1):
            if i%coins[0]==0:
                t[1][i]=i//coins[0]
            else:
                t[1][i]= float('inf')
        
        for i in range(2,n+1):
            for j in range(1, amount+1):
                if coins[i-1]<=j:
                    t[i][j]=min(t[i-1][j], 1+t[i][j-coins[i-1]])
                else:
                    t[i][j]=t[i-1][j]
        if t[n][amount]==float('inf'):
            t[n][amount]=-1
        return t[n][amount]
