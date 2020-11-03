# https://www.geeksforgeeks.org/count-number-subarrays-given-xor/
# https://www.interviewbit.com/problems/subarray-with-given-xor/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        d=dict()
        p=0
        i=0
        cnt=0
        n=len(A)
        while i<n:
            p=p^A[i]
            if p^B in d:
                cnt+=d[p^B]
            if p==B:
                cnt+=1
            if p in d:
                d[p]+=1
            else:
                d[p]=1
            i+=1
        return cnt
