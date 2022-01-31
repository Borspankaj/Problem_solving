class Solution:
    def totalNQueens(self, n: int) -> int:
        def solve(row,cols,dia,anti):
            ans=0
            if row==n:
                return 1
            for col in range(n):
                c_diag=row-col
                c_anti=row+col
                if col in cols or c_diag in dia or c_anti in anti:
                    continue
                cols.add(col)
                dia.add(c_diag)
                anti.add(c_anti)
                ans+=solve(row+1,cols,dia,anti)
                cols.remove(col)
                dia.remove(c_diag)
                anti.remove(c_anti)
            return ans
   
        return solve(0,set(),set(),set())