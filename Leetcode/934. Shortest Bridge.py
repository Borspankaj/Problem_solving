class Solution:
    def shortestBridge(self, grid) -> int:
            q=[]
            island=[]
            n=len(grid)
            flag=False
            indices=[(0,-1),(0,1),(-1,0),(1,0)]
            for i in range(n):
                for j in range(n):
                    if grid[i][j]==1:
                        q.append((i,j))
                        grid[i][j]=-1
                        flag=True   
                        break
                if flag:
                    break

            while q:

                i,j=q.pop(0)
                island.append((0,(i,j)))
                for id1,id2 in indices:
                    newi=i+id1
                    newj=j+id2
                    if 0<=newi<n and 0<=newj<n and grid[newi][newj]==1:
                        grid[newi][newj]=-1


                        q.append((newi,newj))

            while island:

                step,val=island.pop(0)
                i,j=val
                for id1,id2 in indices:
                    newi=i+id1
                    newj=j+id2
                    if 0<=newi<n and 0<=newj<n and grid[newi][newj]!=-1:
                        if grid[newi][newj]==1:
                            return step
                        grid[newi][newj]=-1       
                        island.append((step+1,(newi,newj)))
            return -1

# grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# print(shortestBridge(grid))