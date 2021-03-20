# https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1#

class Solution:
    def palindromicPartition(self, s):
        # code here
        
        def ispalindrome(arr,x,y):
            
            while x<y:
                if arr[x]!=arr[y]:
                    return False
                x+=1
                y-=1
            return True
          
        def solve(arr,i,j):
            if t[i][j]!=-1:
                return t[i][j]
            if i>=j:
                t[i][j]=0
                return 0
            if ispalindrome(arr,i,j):
                t[i][j]=0
                return 0
            mn=float('inf')
            # We can check if the partition for i to k is not a palindrome, then we continue in the for loop, 
            # otherwise we calculate the no of partitions in right partition from k+1 to j
            for k in range(i,j):
                right=0
                if(ispalindrome(arr,i,k)):
                    right=solve(arr,k+1,j)
                else:
                    t[i][k]=0
                    continue
                temp=1+right
                if temp<mn:
                    mn=temp
            t[i][j]=mn
            return t[i][j]
                
        n=len(s)
        t=[[-1 for i in range(n+1)] for j in range(n+1)]
        return solve(s,0,n-1)
