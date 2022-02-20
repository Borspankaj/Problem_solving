class Solution:
    def numIslands(self, grid) -> int:
        def dfs(grid,i,j):
            indices=[(1,0),(-1,0),(0,-1),(0,1)]
            grid[i][j]='-1'
            n=len(grid)
            m=len(grid[0])
            for val1,val2 in indices:
                newi=i+val1
                newj=j+val2
                if n>newi>=0 and m>newj>=0 and grid[newi][newj]=='1':
                    dfs(grid,newi,newj)

        n=len(grid)
        m=len(grid[0])
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    dfs(grid,i,j)
                    count+=1
        return count


# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# print(numIslands(grid))