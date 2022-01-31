class Solution:
    
    def solveNQueens(self, n: int):
        def arrange_board(board):
            new_board=[]
            for row in board:
                new_board.append("".join(row))
                
            return new_board
        
        
        def solve(row,cols,dia,anti,board):
            if row==n:
                ans.append(arrange_board(board))
                return
            for col in range(n):
                c_diag=row-col
                c_anti=row+col

                if col in cols or c_diag in dia or c_anti in anti:
                    continue

                cols.add(col)
                dia.add(c_diag)
                anti.add(c_anti)
                board[row][col]="Q"
                solve(row+1,cols,dia,anti,board)
                board[row][col]="."
                cols.remove(col)
                dia.remove(c_diag)
                anti.remove(c_anti)
        ans=[]
        initial=[["."] * n for i in range(n)]
        solve(0,set(),set(),set(),initial)
        return ans
        