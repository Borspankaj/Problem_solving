class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        n=len(grid)
        # base for impossible path & size 1
        if grid[0][0]==1 or grid[n-1][n-1]==1: 
            return -1
        if n==1:
            return 1
        q=[] #queue for BFS
         
        q.append((1,(0,0))) # pushed in queue , first vertex with level
        grid[0][0]=2 # marked visited
        while q:
            level,pair=q.pop(0) 
            i=pair[0]
            j=pair[1]
            if i==n-1 and j==n-1: # base for destination 
                return level # return level
            if n>i-1>=0 and n>j-1>=0 and grid[i-1][j-1]==0:  # all eight possible neighbors
                q.append((level+1,(i-1,j-1))) #pushed level with vertex
                grid[i-1][j-1]=2
            if n>i-1>=0 and n>j>=0 and grid[i-1][j]==0:
                q.append((level+1,(i-1,j)))
                grid[i-1][j]=2                    
            if n>i-1>=0 and n>j+1>=0 and grid[i-1][j+1]==0:
                q.append((level+1,(i-1,j+1)))            
                grid[i-1][j+1]=2
            if n>i>=0 and n>j+1>=0 and grid[i][j+1]==0:
                q.append((level+1,(i,j+1)))            
                grid[i][j+1]=2
            if n>i+1>=0 and n>j+1>=0 and grid[i+1][j+1]==0:
                q.append((level+1,(i+1,j+1)))               
                grid[i+1][j+1]=2
            if n>i+1>=0 and n>j>=0 and grid[i+1][j]==0:
                q.append((level+1,(i+1,j)))              
                grid[i+1][j]=2  
            if n>i+1>=0 and n>j-1>=0 and grid[i+1][j-1]==0:
                q.append((level+1,(i+1,j-1)))              
                grid[i+1][j-1]=2 
            if n>i>=0 and n>j-1>=0 and grid[i][j-1]==0:
                q.append((level+1,(i,j-1)))               
                grid[i][j-1]=2  
        return -1  #when didn't find the destination 