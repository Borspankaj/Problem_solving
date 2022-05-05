board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def solve(board):
    rows = {i: set()  for i in range(9)}
    cols = {i: set()  for i in range(9)}
    box = {i: set()  for i in range(9)}


    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val != ".":
                if val in rows[i] or val in cols[j] or val in box[(j//3) + 3*(i//3)] :
                    return False
                rows[i].add(val)
                cols[j].add(val)
                box[(j//3) + 3*(i//3)].add(val)
    

    return True
                

print(solve(board))