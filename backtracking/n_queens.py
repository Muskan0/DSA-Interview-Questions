# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queen=[]
        # we need to check only for queens attacking from left side
        def isSafe(board,row,col):
            # left side
            for i in range(col):
                if board[row][i]:
                    return False
            # check upper diagonal on left side
            i=row
            j=col
            while i>=0 and j>=0:
                if board[i][j]:
                    return False
                i-=1
                j-=1
            # check lower diagonal on right side
            i=row
            j=col
            while i<n and j>=0:
                if board[i][j]:
                    return False
                i+=1
                j-=1
            return True
        
        def NQUtil(board, col):
            # base case
            if col==n:
                returnSolution(board)
                return True
            res= False
            # Try placing queen in all rows in the column col
            for i in range(n):
                if isSafe(board,i,col):
                    # make a choice
                    board[i][col]=1
                    res= NQUtil(board, col+1) or res # explore with the choice
                    # undo choice
                    board[i][col]=0
            # if queen could not be placed in any row of this column return false
            return res
        
        def returnSolution(board):
    
            l=[]
            for i in range(n):
                s=''
                for j in range(n):
                    if board[i][j]==1:
                        s+='Q'
                    else:
                        s+='.'
                l.append(s)
            queen.append(l)
            return
                
        board=[[0 for i in range(n)] for j in range(n)]
        m=NQUtil(board,0)
        return queen
