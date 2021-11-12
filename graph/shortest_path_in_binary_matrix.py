# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        visited=[[0 for j in range(n)] for i in range(n)]
        visited[0][0]=1
        x=[-1,-1,-1,0,1,1,1,0]
        y=[-1,0,1,1,1,0,-1,-1]
        q=[[0 , 0]]
        ans=0
        while q:
            size=len(q)
            ans+=1
            for _ in range(size):
                t=q.pop(0)
                a=t[0]
                b=t[1]
                if a==n-1 and b==n-1:
                    return ans
                for i in range(8):
                    dx=x[i]
                    dy=y[i]
                    if 0<=a+dx<n and 0<=b+dy<n and grid[a+dx][b+dy]==0 and visited[a+dx][b+dy]==0:
                        visited[a+dx][b+dy]=1
                        q.append([a+dx, b+dy])
        return -1
                    
# Time Complexity: O(N*N)
# Space Complexity: O(N*N)
# where N*N is the size of the matrix
