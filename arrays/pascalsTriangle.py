# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r=[]
        for i in range(numRows):
            p=[0 for _ in range(i+1)]
            for j in range(i+1):
                if j==0 or j==i:
                    p[j]=1
                else:
                    p[j]=r[i-1][j]+r[i-1][j-1]
            r.append(p)
        return r
