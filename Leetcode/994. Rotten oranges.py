class Solution:
    def orangesRotting(self, grid) -> int:
        
        q=[]
        fresh=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((0,(i,j)))
                if grid[i][j]==1:
                    fresh+=1

        if fresh==0:
            return 0
        while q:
            minute,orange=q.pop(0)
           
            i,j=orange

            if m>i-1>=0 and n>j>=0 and grid[i-1][j]==1:
                grid[i-1][j]=2

                q.append((minute+1,(i-1,j)))
                fresh-=1
            if m>i>=0 and n>j-1>=0 and grid[i][j-1]==1:
                grid[i][j-1]=2
                q.append((minute+1,(i,j-1)))
                fresh-=1
            if m>i>=0 and n>j+1>=0 and grid[i][j+1]==1:
                grid[i][j+1]=2
                q.append((minute+1,(i,j+1)))
                fresh-=1
            if m>i+1>=0 and n>j>=0 and grid[i+1][j]==1:
                grid[i+1][j]=2
                q.append((minute+1,(i+1,j)))
                fresh-=1
        if fresh>0:
            return -1
        else:
            return minute
