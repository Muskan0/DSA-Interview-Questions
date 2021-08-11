# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1#

class Solution:
    def findPath(self, mat, n):
        if mat[0][0]!=1:
            return []
        vis=[[0 for j in range(n)] for i in range(n)]
        ans=[]
        di=[1,0,0,-1]
        dj=[0,-1,1,0]
        solve(0,0,n,ans,"",vis,mat, di, dj)
        return ans

def solve(i,j,n,ans,move,vis,mat, di, dj):
    if i==n-1 and j==n-1:
        ans.append(move)
        return

    # D/L/R/U lexicographic order
    s=['D','L','R','U']
    
    for x in range(4):
        newi=i+di[x]
        newj=j+dj[x]
        if newi>=0 and newi<n and newj>=0 and newj<n and mat[newi][newj]==1 and not vis[newi][newj]:
            # mark (i,j) as visited
            vis[i][j]=1
            # try in all the directions which are feasible
            solve(newi,newj,n,ans,move+s[x],vis,mat, di, dj)
            # backtrack
            vis[i][j]=0
        
# Time complexity: 4^(n*n), on approximation, because in worst case
# we are trying 4 different ways for every cell.
# Space complexity: O(n*n)+O(n*n), for the visited matrix and auxiliary 
# space for recursion tree in worst case because at max the whole n*n
# elements can be in recursion tree if all the elements of matrix are 1.
