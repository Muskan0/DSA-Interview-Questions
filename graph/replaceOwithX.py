# https://practice.geeksforgeeks.org/problems/replace-os-with-xs0052/1#
# It is based on flood fill algorithm.

class Solution:
    def fill(self, n, m, mat):
        for i in range(n):
            for j in range(m):
                if mat[i][j]=='O':
                    mat[i][j]='_'
        for i in range(0,n):
            if mat[i][0]=='_':
                floodfill(mat,i,0,'_', 'O')
        for i in range(0,n):
            if mat[i][m-1]=='_':
                floodfill(mat, i, m-1, '_', 'O')
        for j in range(0,m):
            if mat[0][j]=='_':
                floodfill(mat, 0, j, '_', 'O')
        for j in range(0,m):
            if mat[n-1][j]=='_':
                floodfill(mat, n-1, j, '_', 'O')
        
        for i in range(n):
            for j in range(m):
                if mat[i][j]=='_':
                    mat[i][j]='X'
        return mat

def floodfill(mat,x,y,prev,change):
    n=len(mat)
    m=len(mat[0])
    if x<0 or x>=n or y<0 or y>=m:
        return
    if mat[x][y]!=prev:
        return
    mat[x][y]=change
    
    floodfill(mat, x+1, y, prev, change)
    floodfill(mat, x-1, y, prev, change)
    floodfill(mat, x, y-1, prev, change)
    floodfill(mat, x, y+1, prev, change)
    return
