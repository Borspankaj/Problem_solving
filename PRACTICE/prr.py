def solve(grid):
    n=len(grid)
    m=len(grid[0])
    if grid[0][0]==1 or grid[n-1][n-1]==1:
        return -1
    if n==1:
        return 1
    q=[]
    q.append([0,0])
    distance=1
    grid[0][0]=2
    while q:
        l=len(q)
        while l>0:
            pair=q.pop(0)
            i=pair[0]
            j=pair[1]
            if i==n-1 and j==n-1:
                return distance
            if i-1>=0 and j-1>=0 and i-1<n and j-1<m and grid[i-1][j-1]==0:
                q.append([i-1,j-1])
                grid[i-1][j-1]=2
            if i-1>=0 and j>=0 and i-1<n and j<m and grid[i-1][j]==0:
                q.append([i-1,j])
                grid[i-1][j]=2                    
            if i-1>=0 and j+1>=0 and i-1<n and j+1<m and grid[i-1][j+1]==0:
                q.append([i-1,j+1])            
                grid[i-1][j+1]=2
            if i>=0 and j+1>=0 and i<n and j+1<m and grid[i][j+1]==0:
                
                q.append([i,j+1])            
                grid[i][j+1]=2
            if i+1>=0 and j+1>=0 and i+1<n and j+1<m and grid[i+1][j+1]==0:
                
                q.append([i+1,j+1])               
                grid[i+1][j+1]=2
            if i+1>=0 and j>=0 and i+1<n and j-1<m and grid[i+1][j]==0:
            
                q.append([i+1,j])               
                grid[i+1][j]=2  
            if i+1>=0 and j-1>=0 and i+1<0 and j-1<m and grid[i+1][j-1]==0:
                q.append([i+1,j-1])               
                grid[i+1][j-1]=2 
            if i>=0 and j-1>=0 and i<n and j-1<m and grid[i][j-1]==0:
                q.append([i,j-1])                
                grid[i][j-1]=2  
            l-=1 
        distance+=1        
    return -1

grid = [[0,0,1,0,0,0,0],[0,1,0,0,0,0,1],[0,0,1,0,1,0,0],[0,0,0,1,1,1,0],[1,0,0,1,1,0,0],[1,1,1,1,1,0,1],[0,0,1,0,0,0,0]]
print(solve(grid))