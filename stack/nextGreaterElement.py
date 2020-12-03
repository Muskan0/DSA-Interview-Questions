# https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1#

'''
Function Arguments : 
		@param  : arr(given array), n(size of array)
		@return : An array of length n denoting the next greater elements 
		          for all the array elements
'''
def nextLargerElement(arr,n):
    #code here
    if n==1:
        return [-1]
    else:
        ans=[]
        stack=[]
        i=n-1
        while i>=0:
            if not stack:
                ans.append(-1)
            elif stack[-1]>arr[i]:
                ans.append(stack[-1])
            elif stack[-1]<arr[i]:
                while stack and stack[-1]<arr[i]:
                    m=stack.pop(-1)
                
                if stack:
                    ans.append(stack[-1])
                else:
                    ans.append(-1)
                    
            stack.append(arr[i])
            i-=1
    #print(ans)
    return ans[::-1]
