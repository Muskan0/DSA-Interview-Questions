# https://practice.geeksforgeeks.org/problems/word-boggle4143/1#

# DFS is used here. For a particular index, when the cell of the board is
# matched with the index of the word, we do DFS in all 8 directions 
# to check if character at index+1 also matches. 
# Base case: When index becomes equal to the length of the string
# that means that the word is found on the board.

class Solution:
    def wordBoggle(self,board,dictionary):
        # return list of words(str) found in the board
        res=[]
        # checking whether the word of the dictionary 
        # is on the board
        for i in dictionary:
            if isCheck(i, board)==True:
                res.append(i)
        return res

def isCheck(word, board):
    m=len(board)
    n=len(board[0])
    index=0
    visited=[[False for j in range(n)] for i in range(m)]
    # when the first index of the word matches the
    # (i,j) index of the board
    # if not found then return false
    for i in range(m):
        for j in range(n):
            if board[i][j]==word[index]:
                if dfs(visited, board, i, j, index, word):
                    return True
    return False

def dfs(visited, board, x, y, index, word):
    if index==len(word):
        return True
    if(x>=0 and x<len(board) and y>=0 and y<len(board[0]) and visited[x][y]==False and board[x][y]==word[index]):
        visited[x][y]=True
        if(dfs(visited,board,x-1,y-1,index+1,word) or dfs(visited,board,x-1,y,index+1,word) or dfs(visited,board,x-1,y+1,index+1,word) or dfs(visited,board,x,y-1,index+1,word) or dfs(visited,board,x,y+1,index+1,word) or dfs(visited,board,x+1,y-1,index+1,word) or dfs(visited,board,x+1,y,index+1,word) or dfs(visited,board,x+1,y+1,index+1,word)):
            return True
        visited[x][y]=False
    return False
