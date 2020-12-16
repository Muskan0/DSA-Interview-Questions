# https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1#

class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		t= [[0 for i in range(sum+1)] for j in range(n+1)]
		
		for i in range(0, n+1):
		    for j in range(0, sum+1):
		        if i==0:
		            t[i][j]=0
		        if j==0:
		            t[i][j]=1
	    for i in range(1, n+1):
	        for j in range(1, sum+1):
	            if arr[i-1]<=j:
	                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]
	            else:
	                t[i][j] = t[i-1][j]
        return t[n][sum]%1000000007
