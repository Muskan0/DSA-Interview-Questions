# https://leetcode.com/problems/valid-sudoku/

# optimal approach- one pass
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows=[{} for i in range(9)]
        columns=[{} for i in range(9)]
        boxes=[{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num=int(board[i][j])
                    #print(num)
                    box_index=(i//3)*3 + (j//3)
                    if rows[i].get(num,0)==1 or columns[j].get(num,0)==1 or boxes[box_index].get(num,0)==1:
                        
                        return False
                    
                    rows[i][num]=1
                    columns[j][num]=1
                    boxes[box_index][num]=1
                    #print(rows)
        return True
'''
# approach using single set
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s=set()
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    r="R"+str(i)+board[i][j]
                    if r in s:
                        return False
                    s.add(r)
                    c="C"+str(j)+board[i][j]
                    if c in s:
                        return False
                    s.add(c)
                    box=(i // 3 ) * 3 + j // 3
                    b="B"+str(box)+board[i][j]
                    if b in s:
                        return False
                    s.add(b)
        return True
'''
       
'''
# naive approach in three passes
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidrow(board) and self.isValidcolumn(board) and self.isValidSquare(board)
        
    def isValidunit(self,unit):
        unit=[i for i in unit if i!="."]
        return len(unit)==len(set(unit))
              
    def isValidrow(self, board):
        for row in board:
            if not self.isValidunit(row):
                return False
        return True
    def isValidcolumn(self, board):
        for column in zip(*board):
            if not self.isValidunit(column):
                return False
        return True
    def isValidSquare(self,board):
        for i in (0,3,6):
            for j in (0,3,6):
                square=[board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not self.isValidunit(square):
                    return False
        return True
'''
