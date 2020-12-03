# https://www.interviewbit.com/problems/nearest-smaller-element/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack=[]
        ans=[]
        n=len(A)
        if n==1:
            return [-1]
        i=0
        while i<n:
            if not stack:
                ans.append(-1)
            elif A[i]>stack[-1]:
                ans.append(stack[-1])
            elif A[i]<=stack[-1]:
                while stack and A[i]<=stack[-1]:
                    stack.pop(-1)
                if stack:
                    ans.append(stack[-1])
                else:
                    ans.append(-1)
            stack.append(A[i])
            i+=1
            #print(stack)
        #print(ans)
        return ans
