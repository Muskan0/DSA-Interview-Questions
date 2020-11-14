# https://www.interviewbit.com/problems/max-continuous-series-of-1s/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        wL=maxWindow=wR=bestL=zeroCount=0
	    n=len(A)
	    while wR<n:
	        if zeroCount<=B:
	            if A[wR]==0:
	                zeroCount+=1
	            wR+=1
	        if zeroCount>B:
	           if A[wL]==0:
	               zeroCount-=1
	           wL+=1
	        if wR-wL>maxWindow and zeroCount<=B:
	           maxWindow=wR-wL
	           bestL=wL
	    ans=[]
	    #print(maxWindow)
	    for i in range(0,maxWindow):
	        ans.append(bestL+i)
	    return ans
