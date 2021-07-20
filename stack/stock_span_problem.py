# https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1#

class Solution:
    
    #Function to calculate the span of stocks price for all n days.
    def calculateSpan(self,a,n):
        stack= list()
        res=list()
        i=0
        while i<n:
            if len(stack)==0:
                res.append(i+1)
            elif a[stack[-1]]>a[i]:
                k=stack[-1]
                res.append(i-k)
            elif a[stack[-1]]<=a[i]:
                while len(stack)>0 and a[stack[-1]]<=a[i]:
                    stack.pop()
                if len(stack)==0:
                    res.append(i+1)
                else:
                    res.append(i-stack[-1])
            stack.append(i)
            i+=1
        return res
  '''
  Time Complexity: O(N), as the array is travsersed only once.
  The worst case can only be O(2N).
  
  Space Complexity: O(N) in worst case.
  '''
