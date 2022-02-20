class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        def dfs(grid,i,j):
            grid[i][j]=-1
            count=1
            n=len(grid)
            m=len(grid[0])
            indices=[(1,0),(-1,0),(0,1),(0,-1)]
            for val1,val2 in indices:
                newi=i+val1
                newj=j+val2
                if n>newi>=0 and m>newj>=0 and grid[newi][newj]==1:
                    count+=dfs(grid,newi,newj)

            return count
        n=len(grid)
        m=len(grid[0])
        maxx=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    maxx=max(dfs(grid,i,j),maxx)

        return maxx



# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# print(maxAreaOfIsland(grid))