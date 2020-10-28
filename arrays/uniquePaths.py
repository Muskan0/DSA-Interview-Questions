# https://leetcode.com/problems/unique-paths/

# using combinatorics
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        l=m+n-2
        r=m-1
        res=1
        for  i in range(0,r):
            res*=(l-i)
            res//=i+1
        return res
