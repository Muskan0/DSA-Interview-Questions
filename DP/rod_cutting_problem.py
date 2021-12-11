# https://practice.geeksforgeeks.org/problems/rod-cutting/0#
# it's a similar problem like unbounded knapsack problem

for _ in range(int(input())):
    n=int(input())
    length=[i for i in range(1,n+1)]
    price=list(map(int, input().split()))
    t=[[-1 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if length[i-1]<=j:
                t[i][j]=max(price[i-1]+t[i][j-length[i-1]], t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    print(t[n][n])
    
    
    
    
    
    
# ================================================================================================================================

class Solution:
    def cutRod(self, price, n):
        return self.maxCost(price, 0, n, {})
    
    def maxCost(self, price, currentIndex, length, memo):
        if length==0:
            return 0
        if currentIndex+1>length or currentIndex>=len(price):
            return 0
        
        currentKey=str(currentIndex)+" "+str(length)
        if currentKey in memo:
            return memo[currentKey]
        
        conider=0
        if currentIndex+1<=length:
            consider=price[currentIndex]+self.maxCost(price, currentIndex, length-(currentIndex+1), memo)
        notconsider=self.maxCost(price, currentIndex+1, length, memo)
        
        memo[currentKey]= max(consider, notconsider)
        return memo[currentKey]
# Time Complexity: O(length*N), where length is the total length of the rod 
# and N is the no of elements in price array
# Space Complexity: O(length*N)
