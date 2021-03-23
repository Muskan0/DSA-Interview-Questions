# https://www.interviewbit.com/problems/evaluate-expression-to-true/

class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        n=len(A)
        d=dict()
        return solve(A,0,n-1, True,d)%1003
        

def solve(A,i,j,isTrue,d):
    key= str(i)+" "+str(j)+" "+str(isTrue)
    if key in d:
        return d[key]
    
    if i==j:
        if isTrue==True:
            if A[i]=='T':
                return 1
            else:
                return 0
        else:
            if A[i]=='F':
                return 1
            else:
                return 0
    
    ans=0
    k=i+1
    while k<=j-1:
    
        lT=solve(A,i,k-1,True,d)
        lF=solve(A,i,k-1,False,d)
        rT=solve(A,k+1,j,True,d)
        rF=solve(A,k+1,j,False,d)
        if A[k]=='&':
            if isTrue==True:
                ans=ans+(lT*rT)
            else:
                ans=ans+(lF*rT)+(lT*rF)+(lF*rF)
        elif A[k]=='^':
            if isTrue==True:
                ans=ans+(lF*rT)+(lT*rF)
            else:
                ans=ans+(lF*rF)+(lT*rT)
        elif A[k]=='|':
            if isTrue==True:
                ans=ans+(lF*rT)+(lT*rF)+(lT*rT)
            else:
                ans=ans+(lF*rF)
        k+=2
    d[key]=ans%1003
    return ans
