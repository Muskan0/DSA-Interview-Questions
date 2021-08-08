# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0
        # tot is no of oranges in grid
        tot=0
        n=len(grid)
        m=len(grid[0])
        
        # queue for all rotten oranges
        queue=[]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    tot+=1
                if grid[i][j]==2:
                    queue.append([i,j])
        if tot==0:
            return 0
        # to count how many oranges have been rotten by us
        count=0
        # to count no of minutes
        res=0
        
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]
        
        # bfs
        while queue:
            k=len(queue)
            count+=k
            res+=1
            for i in range(0,k):
                x,y=queue.pop(0)
                # for checking in all directions
                for j in range(4):
                    nx=x+dx[j]
                    ny=y+dy[j]
                    if nx>=0 and nx<n and ny>=0 and ny<m and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        queue.append([nx,ny])
        if count==tot:
            return res-1
        return -1
  '''
  In worst case time complexity: O((n*m)*4)
  when all of the cells are oranges and one of them is rotten,
  we will end up putting all the oranges in the queue.
  And for every cell, we check in four directions,
  that's why multiplied by 4.
  
  Space complexity: O(n*m), in case if all oranges are rotten.
  '''
